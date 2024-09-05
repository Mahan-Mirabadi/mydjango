from django.urls import path
from . import views
app_name = 'contact_us'
urlpatterns=[
    path("",views.ViewContactUs,name="contact_us"),
    path('Login',views.ViewLogin,name="Login"),
    path('cp',views.ViewchangePassword,name='change_password'),
]