from django.urls import path, include
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('', users_views.home, name='overview'),
               path('leaderboard/', users_views.leaderboard, name="leaderboard"),
               path('profile/', users_views.profile, name='profile'),
               ]
