from datetime import date

import math
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib import messages
import requests

from player.forms import UserUpdateForm, ProfileUpdateForm, AccountUpdateForm
from users.models import Account
from challenges.models import Bin
from .models import Fact


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
    fact_today = Fact.objects.filter(date=date_today).first().fact
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
        blur_strength = math.floor(10 - daily_points / 10)

    # Compute progress bar for daily fact of day
    fact_progress = daily_points
    if fact_progress > 100:
        fact_progress = 100

    return render(request, 'player/overview.html',
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

    return render(request, 'player/leaderboard.html',
                  {'title': 'Leaderboard', 'user_acc_leaderboard': all_users_accommodation,
                   'acc_leaderboard': all_accommodations}
                  )


def profile(request):
    if request.method == 'POST':
        #u_form is django user update
        # p_form is image update
        #a_form is user account update
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        # Find account in database to update it
        a_form = AccountUpdateForm(request.POST, instance=Account.objects.get(username=request.user.username))
        if u_form.is_valid() and p_form.is_valid() and a_form.is_valid():
            u_form.save()
            p_form.save()
            a_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'player/profile.html', context)


def map(request):
    bins = Bin.objects.all()
    
    bin_info = []
    for o in bins:
        bin_info.append([o.latitude, o.longitude, o.bin_number])
    
    context = {
        'bin_info': bin_info
    }
    
    return render(request, 'player/map.html', context=context)

              
def news(request): 
    url = 'https://www.climateark.org/api/searchv1/?search=latest&size=3&feed=climate'    
    environment_news = requests.get(url).json()
    articles= environment_news['ecosearch_results']
    summary= []
    title =[]
    link =[]
    date=[]
    for i in range(len(articles)):
         x = source = articles[i]['_source']
         summary.append(x['news_summary'])
         title.append(x['title'])
         link.append(x['link'])
         date.append(x['retrieveddate'])
    newsList = zip(title,summary,date,link)
    context= {'newsList':newsList}
    
    
    return render(request,'player/news.html',context)  
