from django.shortcuts import render

from challenges.templates import *


# Create your views here.

def challengesOverview(request):
    return render(request, 'challenges/challengeBase.html')


def collectibles(request):
    return render(request, 'challenges/collectibles.html')


def QRscan(request):
    return render(request, 'challenges/QRscan.html')
