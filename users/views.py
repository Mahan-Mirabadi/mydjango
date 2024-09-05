from django.shortcuts import render
from users.models import User


# Create your views here.
def nav_view(request):
  return render(request, "users/nav.html") 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def geeks_view(request): 
    # return response 
    return render(request, "users/geeks.html") 
  #??????????????????????????????????????
def user_login(request):
  """Renders the search form with an additional field."""
  context = {}  # Empty context dictionary
  return render(request, 'users/user_login.html', context)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def please_login(request):
  return render(request, 'users/please_login.html', {})
