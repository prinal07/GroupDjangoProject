from django.urls import path, include

from challenges import views as challenge_views

urlpatterns = [path('', challenge_views.challengesOverview, name='challenge_overview'),
               path('collectibles/', challenge_views.collectibles, name="collectibles"),
               path('QRscanner/', challenge_views.QRscan, name='QR Scanner')
               ]
