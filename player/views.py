from django.shortcuts import render
from users.models import User


# Create your views here.
def home(request):
    return render(request, 'player/overview.html', {'title': 'Overview'})


def leaderboard(request):
    # leaderboard of everyone in given accommodation
    # matching the username of Django User class with username our user class
    logged_username = request.user.username
    logged_user = User.objects.get(username=logged_username)
    print(logged_user.accommodation)
    all_users = User.objects.all().filter(accommodation=logged_user.accommodation)
    all_users = all_users.order_by('-points')

    return render(request, 'player/leaderboard.html', {'title': 'Leaderboard', 'leaderboard': all_users}, )


def profile(request):
    return render(request, 'player/profile.html')
