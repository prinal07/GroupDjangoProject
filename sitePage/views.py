from django.shortcuts import render

# Create your views here.
def home(request):
    """Servers the homepage for <url>/sitePage/

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: Serves the webpage stored at ./templates/sitePage/index.html because of Django's file structure
    """
    return render (request, 'sitePage/index.html')


def about(request):
    """Serves the page for <url>/sitePage/about/

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: Serves the webpage stored at ./templates/sitePage/about.html because of Django's file structure 
    """
    # Render about.html with Context
    # Context is a JSON format to pass information into a webpage for use in Javascript or HTML formatting
    return render (request, 'sitePage/about.html', {'title': 'About'})
