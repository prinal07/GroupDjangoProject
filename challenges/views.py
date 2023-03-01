from django.shortcuts import render

from challenges.templates import *
from users.models import User



# Create your views here.

def challengesBase(request):
    return render(request, 'challenges/challengeBase.html')

def challengeManager(request):
    return render(request, 'challenges/challengeManager.html')

def collectibles(request):
    return render(request, 'challenges/collectibles.html')

def QR(request):
    return render(request, 'challenges/QR.html')
