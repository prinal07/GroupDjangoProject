from django.urls import path, include
from player import views as player_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('', player_views.home, name='overview'),
               path('leaderboard/', player_views.leaderboard, name="leaderboard"),
               path('profile/', player_views.profile, name='profile'),
               path('challenges/', include('challenges.urls')),
               path('map/', player_views.map, name='map'),
               path('news/', player_views.news, name='news'),
               ]
