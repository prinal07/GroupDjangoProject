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
            accommodation = form.cleaned_data.get('accommodation')
            new_user = User(username=username, password=password, accommodation=accommodation)
            new_user.save()
            form.save()
            messages.success(request, f'Account created for {username}')
            # change to player-page when implemented
            return redirect('site-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def register2(request):
    return render(request, 'users/register2.html')

