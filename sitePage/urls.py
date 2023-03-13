from django.urls import path
from . import views

# Refers to url patterns for <url>/sitePage/*.html
# Url patterns point to functions in ./views.py to serve webpages
urlpatterns = [path('', views.home, name="site-home"),
               # match with about
               path('about/', views.about, name="site-about"),
               ]
