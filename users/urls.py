
from django.urls import path

from users import views
from .views import geeks_view, nav_view 

urlpatterns = [
    path('ul', views.user_login, name='login'),
    path('pl', views.please_login, name='please_login'),
    path('2/', nav_view, name = "template2"),
    path('1/', geeks_view, name = "template1"), 
]
