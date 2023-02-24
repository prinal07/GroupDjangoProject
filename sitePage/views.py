from django.shortcuts import render

# Create your views here.
def home(request):

    return render (request, 'sitePage/index.html')


def about(request):
    return render (request, 'sitePage/about.html', {'title': 'About'})
