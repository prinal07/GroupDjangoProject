import re

from django.shortcuts import render, redirect
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
                # Saves user to Users section of database
                new_user.save()
                #Saves user to Django validation and verification
                form.save()

                messages.success(request, f'Account created for {username} Staff status {localStaffBool}')
                # change to player-page when implemented
                return redirect('site-home')
            else:
                messages.warning(request, f'Please enter an email address with exeter domain (XYZ.exeter.ac.uk)')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


