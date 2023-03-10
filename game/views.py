from datetime import date

import math
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib import messages
import requests
import json
from django.http import JsonResponse

from game.forms import UserUpdateForm, ProfileUpdateForm, AccountUpdateForm, DeleteAccountForm
from users.models import Account
from game.models import Bin
from .models import Fact
from django.contrib.auth.decorators import login_required

from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, MultiPolygon, Feature


# Create your views here.
def home(request):
    # leaderboard of everyone in given accommodation
    # matching the username of Django User class with username our user class
    logged_username = request.user.username
    logged_user = Account.objects.get(username=logged_username)
    # collect time accessed

    if logged_user.last_day_accessed != date.today():
        logged_user.daily_points = 0
        logged_user.save()

    logged_user.last_day_accessed = date.today()
    logged_user.save()

    all_users_accommodation = Account.objects.all().filter(accommodation=logged_user.accommodation)
    all_users_accommodation = all_users_accommodation.order_by('-points')[:5]

    # annotate creates new field for each accommodation group
    # creating sum column for each accommodation
    all_accommodations = Account.objects.values('accommodation').annotate(Sum('points')).order_by('-points__sum')[:5]
    print(all_accommodations)

    # get fact of day
    date_today = date.today()
    # database object, not fact
    fact_today = "There are no facts in DB"
    fact_today_object = Fact.objects.filter(date=date_today).first()
    if fact_today_object is not None:
        fact_today = fact_today_object.fact

    print(fact_today)

    # get user points

    logged_username = request.user.username
    logged_account = Account.objects.get(username=logged_username)
    user_points = logged_account.points

    # get daily user points

    daily_points = logged_account.daily_points

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
                   'current_level': logged_account.current_level(),
                   'level_progress': logged_account.level_progress(),
                   'fact_today': fact_today,
                   'blur_strength': blur_strength,
                   'fact_progress': fact_progress})


def leaderboard(request):
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
    logged_username = request.user.username
    logged_account = Account.objects.get(username=logged_username)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        # Find account in database to update it
        a_form = AccountUpdateForm(request.POST, instance=Account.objects.get(username=request.user.username))

        if u_form.is_valid() and p_form.is_valid() and a_form.is_valid():
            u_form.save()
            p_form.save()
            # uses info from u_form passed to profile.html; a_form is same as u_form
            a_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    d_form = DeleteAccountForm()

    if 'delete' in request.POST:
        d_form = DeleteAccountForm(request.POST)
        if d_form.is_valid() and d_form.cleaned_data['confirm_delete'] == True:
            user = request.user
            # delete account entity
            logged_account.delete()
            # delete django account, linked to profile
            user.delete()
            messages.success(request, f'Your account has been deleted!')
            return redirect('site-home')

        # u_form is django user update
        # p_form is image update
        # a_form is user account update
        # d_form is delete user from db

    # ensure new level stored in account db each time
    logged_account.level = logged_account.current_level()
    logged_account.save()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'd_form': d_form,
        'user_points': logged_account.points,
        'current_level': logged_account.current_level(),
        'level_progress': logged_account.level_progress()
    }

    return render(request, 'game/profile.html', context)


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
            [([(lat + 1, lon + 1), (lat - 1, lon - 1), (lat - 1, lon + 1), (lat + 1, lon - 1)],),
             ([(50.7393587, -3.54012113), (50.7381304, -3.5382954), (50.7394105, -3.537208)],),
             (
             [(50.7418840, -3.5341631), (50.7403587, -3.5335790), (50.7410841, -3.5312515), (50.7422746, -3.5324632)],),
             ([(50.7364445, -3.5293083), (50.7358839, -3.5291410), (50.7360017, -3.5298109),
               (50.7363348, -3.5299208)],)]))

        # [-3.5293083, 50.7364445],
        # [-3.5291410, 50.7358839],
        # [-3.5298109, 50.7360017],
        # [-3.5299208, 50.7363348]

        print(boolean_point_in_polygon(point, polygon))
        if (boolean_point_in_polygon(point, polygon)):
            logged_user.points += 10
            logged_user.save()
            message = {'message': 'You have entered green area!'}
            return JsonResponse(message)

    # 50.7283775,-3.5228209
    # 50.7283775,-3.5228209

    # 50.7283568, -3.5229058

    # 50.7282447,-3.522881

    bins = Bin.objects.all()
    bin_info = []
    for o in bins:
        bin_info.append([o.latitude, o.longitude, o.bin_number])

    context = {
        'bin_info': bin_info,
        'message': message
    }

    return render(request, 'game/map.html', context=context)


def news(request):
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
