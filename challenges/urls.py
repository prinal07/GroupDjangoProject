from django.urls import path, include

from challenges import views as challenge_views

urlpatterns = [path('collectibles/', challenge_views.collectibles, name="collectibles"),
               path('', challenge_views.challengeManager, name='challengeManager'),
               path('QR/', challenge_views.QR, name='QR'),
               ]
