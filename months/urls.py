from django.urls import path

from months import views


urlpatterns = [
        path('vm', views.viewmonths),
    path('vw', views.viewweek),
    path('vs', views.viewsample),
    path('va', views.viewadd),
    path('<int:num>', views.dynamic_int),
    path('', views.index),
    path('<m>', views.dynamic_str),
    path('vm1', views.viewmonths1),
]