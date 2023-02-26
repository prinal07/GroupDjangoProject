from django.shortcuts import render
from users.models import User
from django.db.models import Sum


# Create your views here.
def home(request):
    return render(request, 'player/overview.html', {'title': 'Overview'})


def leaderboard(request):
    # leaderboard of everyone in given accommodation
    # matching the username of Django User class with username our user class
    logged_username = request.user.username
    logged_user = User.objects.get(username=logged_username)
    print(logged_user.accommodation)

    all_users_accommodation = User.objects.all().filter(accommodation=logged_user.accommodation)
    all_users_accommodation = all_users_accommodation.order_by('-points')

    # annotate creates new field for each accomdation group
    # creating sum column for each accommodation
    all_accommodations = User.objects.values('accommodation').annotate(Sum('points')).order_by()
    print(all_accommodations)

    return render(request, 'player/leaderboard.html',
                  {'title': 'Leaderboard', 'user_acc_leaderboard': all_users_accommodation,
                   'acc_leaderboard': all_accommodations}
                  )


def profile(request):
    return render(request, 'player/profile.html')
