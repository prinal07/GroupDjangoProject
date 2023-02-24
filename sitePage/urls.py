from django.urls import path
from . import views

urlpatterns = [path('', views.home, name="site-home"),
               # match with about
               path('about/', views.about, name="site-about"),

               ]
