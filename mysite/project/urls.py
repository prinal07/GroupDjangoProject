from django.urls import path

from . import views

app_name = 'project'

urlpatterns = [
    path('', views.index, name='index'),
    # path('register/add/', view.register, name = addUser)
    path('register/',views.registerPage.as_view(),name="register"),
    path('login/',views.loginPage,name="login")
]



