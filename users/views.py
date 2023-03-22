import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Account

# Create your views here.

def register(request):
    """Serves the webpage for <url>/register.html

    Handles a POST request, submitted from the Form passed in the context to the site
    POST request handles:
        - Cleaning data for Username, Password, Email, and Accomodation
        - Validating the provided email is of domain @exeter.ac.uk
        - Validates if the user is staff using Regular Expressions
        
        - If Validation is Complete, create a new record for the Registration and save the User to the table

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: Serves ./templates/users/register.html due to Django's file structure
        Passes context of an instantiation of the UserRegistrationForm class located in ./forms.py if GET request
    """

    if request.method == 'POST':
        # Create a form instance with the submitted data.
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Collect cleaned data submitted in the UserRegistrationForm
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            accommodation = form.cleaned_data.get('accommodation')

            # Initialise values to compare collected data against
            # Regex expression deciding if an email is staff (Only Alphabetical, not Alphaneumeric)
            staff_pattern = r'^[A-Za-z]\.'
            # The expected domain for provided email addresses
            expected_suffix = "exeter.ac.uk"

            local_part, domain_part = email.split("@")

            # Check if the domain part matches the expected suffix
            if domain_part.endswith(expected_suffix):
                exeterCheck = True
            # Can add a list of allowed domains to be checked.
            else:
                exeterCheck = False

            # Check if the email username provided matches the staff_pattern regular expression
            if re.match(staff_pattern, local_part):
                localStaffBool = True
            else:
                localStaffBool = False

            if exeterCheck:
                # Instantiate new user object
                new_user = Account(username=username, password=password, email=email, accommodation=accommodation,
                                   staffCheck=localStaffBool)
                # Saves user to Users section of database
                new_user.save()
                #Saves user to Django validation and verification
                form.save()

                messages.success(request, f'Account created for {username}')
                # change to game-page when implemented
                return redirect('site-home')
            else:
                messages.warning(request, f'Please enter an email address with exeter domain (XYZ.exeter.ac.uk)')

    else:
        # Create a blank form instance for rendering the registration page.
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

    
