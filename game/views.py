from datetime import date
import math
from math import radians
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib import messages
from game.models import Story, Suspect
import requests
from django.http import HttpResponse, JsonResponse

from game.forms import UserUpdateForm, ProfileUpdateForm, AccountUpdateForm, DeleteAccountForm
from users.models import Account
from game.models import Bin
from .models import Fact
from django.contrib.auth.decorators import login_required

import json
from django.http import JsonResponse
from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, MultiPolygon, Feature


def green_checker(request):
    """ Uses green counter to set status of incomplete Green activities to done

     Args:
        request (_type_): _description_

         Returns:
             None

    """

    logged_username = request.user.username
    logged_user = Account.objects.get(username=logged_username)

    # Get the challenges list for the logged in user
    challenges_tracker_list = logged_user.challengetracker_set.filter(completed=False)

    # Loop through the challenges and check if any challenge is related to green areas
    for challenge_tracker in challenges_tracker_list:
        challenge = challenge_tracker.challenge
        if challenge.challengeType == 'Green Areas':
            # Check if the green counter matches the target for this challenge
            target = int(challenge.challengeDesc.split(' ')[1])  # Get the target number of green areas
            if logged_user.greenCounter >= target:
                # Update the challenge tracker status to completed
                challenge_tracker.completed = True
                challenge_tracker.save()

                #Number of clues is increased, as a challenge has been completed
                logged_user.cluesUnlocked += 1

# Create your views here.

@login_required
def home(request):
    """Serves the homepage for <url>/game/
    
    Collects and sorts competition information for Users in the same accomodation as the current user
    Finds the current Fact of the Day for Display
    Determines the blur strength of the Fact of the Day
    
    Pass all information determined as Context to the webpage for representation

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: Serves the webpage stored at ./templates/game/index.html because of Django's file structure
        Passes context to the webpage in JSON format, to record values for use in JavaScript or HTML formatting
    """

    # leaderboard of everyone in given accommodation
    # matching the username of Django User class with username our user class
    logged_username = request.user.username
    logged_user = Account.objects.get(username=logged_username)
    # collect time accessed

    # Resets a User's Daily points if accessing on a different day
    if logged_user.last_day_accessed != date.today():
        logged_user.daily_points = 0
        logged_user.save()

    # Resets the value of last_day_accessed to prevent Daily points resets until tomorrow
    logged_user.last_day_accessed = date.today()
    logged_user.save()

    # Collects all stored accounts that share the current user's accomodation cell value
    all_users_accommodation = Account.objects.all().filter(accommodation=logged_user.accommodation)

    # Sorts the accomodations collected on the line above by the points cell value
    all_users_accommodation = all_users_accommodation.order_by('-points')[:5]

    # annotate creates new field for each accommodation group
    # creating sum column for each accommodation
    all_accommodations = Account.objects.values('accommodation').annotate(Sum('points')).order_by('-points__sum')[:5]
    print(all_accommodations)

    # Gets today's date for fetching today's fact
    date_today = date.today()

    # Default fact value
    fact_today = "There are no facts in DB"

    # Fetch the Fact Record from the Database with shared date
    fact_today_object = Fact.objects.filter(date=date_today).first()

    # Replaces default fact with any found fact
    if fact_today_object is not None:
        fact_today = fact_today_object.fact

    print(fact_today)

    # get user points
    user_points = logged_user.points

    # get daily user points

    daily_points = logged_user.daily_points

    # Calculate blur based on daily points

    blur_strength = 0
    if daily_points < 100:
        blur_strength = 10
        # blur_strength = math.floor(10 - daily_points / 10)

    # Compute progress bar for daily fact of day
    fact_progress = daily_points
    # Fact progress remains at 100 once 100 daily points acquired
    if fact_progress > 100:
        fact_progress = 100

    return render(request, 'game/overview.html',
                  {'title': 'Overview',
                   'user_points': user_points,
                   'daily_points': daily_points,
                   'user_acc_leaderboard': all_users_accommodation,
                   'acc_leaderboard': all_accommodations,
                   'current_level': logged_user.current_level(),
                   'level_progress': logged_user.level_progress(),
                   'fact_today': fact_today,
                   'blur_strength': blur_strength,
                   'fact_progress': fact_progress})

@login_required
def leaderboard(request):
    """Serves the Leadboard webpage for <url>/game/leaderboard

    Collects and passes the sorted points of all users within the same accomodation as Current User
    Collects and passes the sorted point totals for all accomodations

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: Serves ./templates/game/leaderboard.html due to Django's file structure
        Passes context of acquired information, the Title of the Page, the User and Global Accomodation Leaderboards
    """
    # leaderboard of everyone in given accommodation
    # matching the username of Django User class with username our user class
    logged_username = request.user.username
    logged_user = Account.objects.get(username=logged_username)
    print(logged_user.accommodation)

    all_users_accommodation = Account.objects.all().filter(accommodation=logged_user.accommodation)
    all_users_accommodation = all_users_accommodation.order_by('-points')

    # annotate creates new field for each accomdation group
    # creating sum column for each accommodation
    all_accommodations = Account.objects.values('accommodation').annotate(Sum('points')).order_by()
    print(all_accommodations)

    return render(request, 'game/leaderboard.html',
                  {'title': 'Leaderboard', 'user_acc_leaderboard': all_users_accommodation,
                   'acc_leaderboard': all_accommodations}
                  )

@login_required
def profile(request):
    """Serves the Profile webpage for <url>/game/profile/

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: Serves one of three options:
            - A redirect to <url>/game/profile/ , upon updating User information
            - A redirect to <url>/sitePage/ , upon deleting User information
            - A Profile overview page stored at ./templates/game/profile.html due to Django's file structure
                Pass the context of all possible forms, to be issued on button request
    """

    # Fetches current username and account record
    logged_username = request.user.username
    logged_account = Account.objects.get(username=logged_username)

    # Receives a POST request sent by a UserUpdateForm 
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        picture_update_form = ProfileUpdateForm(request.POST,
                                                request.FILES,
                                                instance=request.user.profile)
        # Find account in database to update it
        account_update_form = AccountUpdateForm(request.POST,
                                                instance=Account.objects.get(username=request.user.username))

        if user_update_form.is_valid() and picture_update_form.is_valid() and account_update_form.is_valid():
            user_update_form.save()
            picture_update_form.save()
            # uses info from user_update_form passed to profile.html; account_update_form is same as user_update_form
            account_update_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        picture_update_form = ProfileUpdateForm(instance=request.user.profile)

    user_delete_form = DeleteAccountForm()

    if 'delete' in request.POST:
        user_delete_form = DeleteAccountForm(request.POST)
        if user_delete_form.is_valid() and user_delete_form.cleaned_data['confirm_delete'] == True:
            user = request.user
            # delete account entity
            logged_account.delete()
            # delete django account, linked to profile
            user.delete()
            messages.success(request, f'Your account has been deleted!')
            return redirect('site-home')

        # user_update_form is django user update
        # picture_update_form is image update
        # account_update_form is user account update
        # user_delete_form is delete user from db

    # ensure new level stored in account db each time
    logged_account.level = logged_account.current_level()
    logged_account.save()

    context = {
        'user_update_form': user_update_form,
        'picture_update_form': picture_update_form,
        'user_delete_form': user_delete_form,
        'user_points': logged_account.points,
        'current_level': logged_account.current_level(),
        'level_progress': logged_account.level_progress()
    }

    return render(request, 'game/profile.html', context)

@login_required
def map(request):
    message = ""

    logged_username = request.user.username
    logged_user = Account.objects.get(username=logged_username)

    if request.method == 'POST':
        data = json.loads(request.body)
        lat = data.get("lat")
        lon = data.get("lon")
        print(data)

        print(lat, lon)

        point = Feature(geometry=Point([lat, lon]))
        polygon = Feature(geometry=MultiPolygon(
            [([(50.7393587, -3.54012113), (50.7381304, -3.5382954), (50.7394105, -3.537208)],),
             (
                 [(50.7418840, -3.5341631), (50.7403587, -3.5335790), (50.7410841, -3.5312515),
                  (50.7422746, -3.5324632)],),
             (
                 [(50.7364445, -3.5293083), (50.7358839, -3.5291410), (50.7360017, -3.5298109),
                  (50.7363348, -3.5299208)],),
             (
                 [(50.7287101, -3.5374679), (50.7280259, -3.5364497), (50.7280361, -3.5353282),
                  (50.7289626, -3.5356284)],),
             ([(50.7341617, -3.5319415), (50.7340736, -3.5314349), (50.7332753, -3.5324445),
               (50.7330960, -3.5319436)],),
             ([(50.7359873845501, -3.532288932448523), (50.73694531506939, -3.5334667225815792),
               (50.736653497251154, -3.5340531117119554)],)

             ]))
        # ([(lat + 1, lon + 1), (lat - 1, lon - 1), (lat - 1, lon + 1), (lat + 1, lon - 1)],),

        print(boolean_point_in_polygon(point, polygon))

        if boolean_point_in_polygon(point, polygon):
            # Increase counter
            logged_user.greenCounter += 1

            # Add points
            logged_user.points += 10
            logged_user.save()

            message = {'message': 'You have entered green area! 10 points awarded'}
            return JsonResponse(message)

    bins = Bin.objects.all()
    """Supplies coordinates of bins to the mapbxo representation in <url>/game/map/
    
    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: Serves ./templates/map.html due to Django's file structure
        Passes a JSON structure as context, holding a 2D Array of Bin Lat/Lon Coordinates and ID Number
    """

    # Collect all Bin records from the Database Table
    bins = Bin.objects.all()

    # Collect all Bin Coordinate pairs and ID number into a list 
    bin_info = []
    for o in bins:
        bin_info.append([o.latitude, o.longitude, o.bin_number])

    context = {
        'bin_info': bin_info,
        'message': message
    }

    # Serve game/map.html 
    return render(request, 'game/map.html', context=context)

@login_required
def news(request):
    """Serves a news 

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    url = 'https://www.climateark.org/api/searchv1/?search=latest&size=3&feed=climate'
    environment_news = requests.get(url).json()
    articles = environment_news['ecosearch_results']
    summary = []
    title = []
    link = []
    date = []
    for i in range(len(articles)):
        x = source = articles[i]['_source']
        summary.append(x['news_summary'])
        title.append(x['title'])
        link.append(x['link'])
        date.append(x['retrieveddate'])
    newsList = zip(title, summary, date, link)
    context = {'newsList': newsList}

    return render(request, 'game/news.html', context)


def challengeManager(request):
    logged_username = request.user.username
    logged_user = Account.objects.get(username=logged_username)

    completed_green_tasks = logged_user.greenCounter
    completed_bin_tasks = logged_user.binCounter
    completed_walk_tasks = logged_user.walkCounter

    green_checker(request)

    challenge_list = []
    for challenge_info in logged_user.challengetracker_set.all():
        challenge_dict = {}
        challenge_dict['description'] = challenge_info.challenge.challengeDesc
        challenge_dict['status'] = challenge_info.checkStatus()
        challenge_list.append(challenge_dict)

    print(challenge_list)

    return render(request, 'game/challengeManager2.html', {'challenge_list': challenge_list,
                                                           'green_counter': completed_green_tasks,
                                                           'bin_counter': completed_bin_tasks,
                                                           'walk_counter': completed_walk_tasks})

@login_required
def QR(request):
    return render(request, 'game/QR.html')


@login_required
def update_points(request):
    """Update the Database record for the current User

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: Serves two different options:
            - A redirect to page <url>/
            - A webpage to page <url>/game/ 
    """

    if request.method == 'POST' and 'update_points' in request.POST:
        # Get the current user and update their points field in the Database record
        logged_username = request.user.username
        logged_user = Account.objects.get(username=logged_username)

        #Bin counter of the user is incremented
        logged_user.binCounter += 1

        logged_user.cluesUnlocked += 1
        logged_user.points += 10
        logged_user.daily_points += 10
        logged_user.save()

        # Show a success message to the user
        messages.success(request, 'Points updated successfully!')

        # Redirect back to the current page
        return redirect(request.META.get('HTTP_REFERER', '/'))

    # If the form was not submitted, render a template with the form
    return render(request, 'update_points.html')

@login_required

def unity(request):
    """Serves the Unity Game at <url>/game/unity>
    Uses the pre-built Unity WebGL html file to load a gameInstance and serve a project to the user

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: Webpage at ./templates/game/unity.html
    """

    STORY_POINT_REWARD = 100
    
    if request.method == "POST":
        data = json.loads(request.body)
        give_points = data.get("give_points")

        # check that story has been completed
        if give_points == "true":
            # give points to logged in user
            user = Account.objects.get(username=request.user.username)
            user.gameCompleted = True
            user.points += STORY_POINT_REWARD
            user.daily_points += STORY_POINT_REWARD 

            user.save()

        # redirect to the overview
        return redirect("game")
        
    else:
        # construct all information to pass to the unity game
        description = []
        culprit = ""
        clues = []

        story = Story.objects.get(story_number = 1)
        suspects = story.suspects.all()
        #stores all clues of the story
        allClues = [story.clue1, story.clue2, story.clue3, story.clue4, story.clue5, story.clue6, story.clue7, story.clue8, story.clue9, story.clue10]

        #fetches current user and the number of clues the user has unlocked
        logged_username = request.user.username
        logged_user = Account.objects.get(username = logged_username)
        cluesUnlocked = logged_user.cluesUnlocked
        notUnlocked = "Complete a Challenge to unlock next clue"

        #Make the number of unlocked clues viewable in Unity
        for ctr in range(cluesUnlocked):
            clues.append(allClues[ctr])

        #Make the number of not unlocked clues viewable as 'Complete a Challenge to unlock next clue'
        for ctr2 in range(10 - cluesUnlocked):
            clues.append(notUnlocked)

        # get information from a stored Story model
        for suspect in suspects:
            description.append(suspect.brief)
        desc_str = "[SPLIT]".join(description) # [SPLIT] recognised by the Unity C# Script as the delimiter
        culprit = story.culprit
        clues_str = "[SPLIT]".join(clues)
        sprites = [story.sprite_1, story.sprite_2, story.sprite_3, story.sprite_4, story.sprite_5]

        context = {
            "spriteCodes": sprites,
            "culprit": culprit,
            "descriptions": desc_str,
            "clues": clues_str
        }    
    
        return render(request, template_name="game/unity.html", context=context)
@csrf_exempt
def Receiver(request):
    """
    A sample view that receives a POST request with 'latitude' and 'longitude' parameters.
    This view is CSRF exempt.

    Args:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A simple response confirming that data was received.
    """
    if request.method == 'POST':

        logged_username = request.user.username
        logged_account = Account.objects.get(username=logged_username)


        # Get the 'latitude' and 'longitude' parameters from the POST request
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')


        logged_account.startingLat = latitude
        logged_account.startingLng = longitude  # set the startingLocation field to latitude
        logged_account.save()  # save the Account object to the database


        # Return a simple response confirming that data was received
        return HttpResponse('success')

    else:
        # Return an error message if the request method is not POST
        return HttpResponse('Invalid request method')
def get_Directions(request):
    """
    This function takes in a POST request object and calculates the distance 
    between two latitude-longitude coordinates using the Haversine formula. 
    It then saves the distance to the database and returns a rendered template.
    """
    if request.method == 'POST':
        # Get the username and account object for the logged-in user
        logged_username = request.user.username
        logged_account = Account.objects.get(username=logged_username)

        # Retrieve the final latitude and longitude from the POST request and save them to the user's account
        logged_account.finalLat = request.POST.get('latitude')
        logged_account.finalLng = longitude = request.POST.get('longitude')
        logged_account.save() 

        # Convert the starting and final latitude-longitude coordinates to radians
        startingLat = float(logged_account.startingLat)
        startingLng = float(logged_account.startingLng)
        finalLat = float(logged_account.finalLat)
        finalLng = float(logged_account.finalLng)
        lat1 = radians(startingLat)
        lon1 = radians(startingLng)
        lat2 = radians(finalLat)
        lon2 = radians(finalLng)


        # Calculate the distance between the two coordinates using the Haversine formula
        d_lat = lat2 - lat1
        d_lon = lon2 - lon1
        a = math.sin(d_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        R = 6371 # Earth's radius in km
        distance = R * c

        # Save the calculated distance to the user's account
        logged_account.distanceTraveled = distance
        logged_account.save()

        # Render the map template
        return render(request, "game/map.html")

    else:
        # Render the map template
        return render(request, "game/map.html")