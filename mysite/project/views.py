from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'project/index.html')

def registerPage(request):
    form = UserCreationForm()
    context = {}
    return render(request, 'project/register.html',context)


