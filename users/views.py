import re

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import User



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            accommodation = form.cleaned_data.get('accommodation')

            staff_pattern = r'^[A-Za-z]\.'
            expected_suffix = "exeter.ac.uk"

            local_part, domain_part = email.split("@")

            # Check if the domain part matches the expected suffix
            if domain_part.endswith(expected_suffix):
                exeterCheck = True
            # Can add a list of allowed domains to be checked.
            else:
                exeterCheck = False

            if re.match(staff_pattern, local_part):
                localStaffBool = True
            else:
                localStaffBool = False

            if exeterCheck:
                new_user = User(username=username, password=password, accommodation=accommodation, staffCheck = localStaffBool)
                new_user.save()
                form.save()

                messages.success(request, f'Account created for {username} Staff status {localStaffBool}')
                # change to player-page when implemented
                return redirect('site-home')
            else:
                messages.warning(request, f'Please enter an email address with exeter domain (XYZ.exeter.ac.uk)')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def register2(request):
    return render(request, 'users/register2.html')

def profile(request):
    return render(request, 'users/profile.html')

# Create your views here.
def home(request):
    return render(request, 'player/overview.html', {'title': 'Overview'})


def leaderboard(request):
    # leaderboard of everyone in given accommodation
    accommodation = request.user.accommodation
    all_users = User.objects.all().filter(accommodation=request.user.accommodation)
    all_users = all_users.order_by('-points')

    return render(request, 'player/leaderboard.html', {'title': 'Leaderboard', 'leaderboard': all_users}, )

