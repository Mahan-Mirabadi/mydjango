from django.urls import path

from products import views

app_name='products'
urlpatterns = [
    path('vp/', views.viewproduct, name='viewproduct'),
    path('vp/<slug:s>', views.ViewProductDetails, name='ViewProductDetails'),
    path('vt', views.ViewThanks, name='ViewThanks')
]
