from django.urls import path

from weeks import views


urlpatterns = [
    path('vw', views.viewweek),
    path('home', views.home),
]