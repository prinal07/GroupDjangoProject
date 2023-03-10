from django.urls import path, include
from game import views as player_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [path('', player_views.home, name='overview'), 
               path('your_view/', views.your_view, name='your_view'),
               path('leaderboard/', player_views.leaderboard, name="leaderboard"),
               path('profile/', player_views.profile, name='profile'),
               path('map/', player_views.map, name='map'),
               path('news/', player_views.news, name='news'),
               path('challenges/', player_views.challengeManager, name='challengeManager'),
               path('QR/', player_views.QR, name='QR'),
               path('update_points/', player_views.update_points, name='update_points'),
               ]
