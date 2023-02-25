from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from users import views as user_views
from player import views as player_views


urlpatterns = [path('', player_views.home, name="overview")]