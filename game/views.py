from datetime import date

from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib import messages
import requests

from game.forms import UserUpdateForm, ProfileUpdateForm, AccountUpdateForm, DeleteAccountForm
from users.models import Account
from game.models import Bin
from .models import Fact
from django.contrib.auth.decorators import login_required


# Create your views here.
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


def map(request):
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
        'bin_info': bin_info
    }

    # Serve game/map.html 
    return render(request, 'game/map.html', context=context)


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
    return render(request, 'game/challengeManager.html')


def QR(request):
    return render(request, 'game/QR.html')


@login_required
def update_points(request):
    if request.method == 'POST' and 'update_points' in request.POST:
        # Get the current user and update their points field
        logged_username = request.user.username
        logged_user = Account.objects.get(username=logged_username)
        logged_user.points += 10
        logged_user.daily_points += 10
        logged_user.save()

        # Show a success message to the user
        messages.success(request, 'Points updated successfully!')

        # Redirect back to the current page
        return redirect(request.META.get('HTTP_REFERER', '/'))

    # If the form was not submitted, render a template with the form
    return render(request, 'update_points.html')

def unity(request):
    return render(request, template_name="game/unity.html")