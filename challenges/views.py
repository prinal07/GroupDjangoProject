from django.shortcuts import render

from challenges.templates import *
from users.models import User, Account


# Create your views here.

def challengesBase(request):
    return render(request, 'challenges/challengeBase.html')

def challengeManager(request):
    return render(request, 'challenges/challengeManager.html')

def collectibles(request):
    return render(request, 'challenges/collectibles.html')

def QR(request):
    return render(request, 'challenges/QR.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
