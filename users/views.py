import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Account

def register(request):
    """
    Renders the user registration page and handles form submission.

    GET: Renders the registration page with a blank form.
    POST: Validates the submitted form and creates a new user account if the form is valid.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered registration page or a redirect to the home page upon successful account creation.
    """
    if request.method == 'POST':
        # Create a form instance with the submitted data.
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Extract data from the valid form.
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
                # Create a new user instance with the extracted data.
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
