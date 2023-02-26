from django.shortcuts import render
from users.models import User


# # Create your views here.
# def home(request):
#     return render(request, 'player/overview.html', {'title': 'Overview'})


# def leaderboard(request):
#     # leaderboard of everyone in given accommodation
#     accommodation = request.user.accommodation
#     all_users = User.objects.all().filter(accommodation=request.user.accommodation)
#     all_users = all_users.order_by('-points')

#     return render(request, 'player/leaderboard.html', {'title': 'Leaderboard', 'leaderboard': all_users}, )


# def profile(request):
#     return render(request, 'player/profile.html')
