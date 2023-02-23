from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'project/index.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'project/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'project/login.html', context)
