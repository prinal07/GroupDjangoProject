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

# views.py

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def scan_again(request):
    account = request.account
    points =  account.points
    points = points + 10
    account.save()
    return HttpResponse('Counter incremented!')
