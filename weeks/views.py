from django.shortcuts import render
dict_weekdays = {
    "sunday":"this is the first day of the week",
    "monday":"this is the second day of the week",
    "tuesday":"this is the third day of the week",
    "wednesday":"this the fourth day of the week",
    "thursday":"this the fifth day of the week",
    "friday":"this is the sixth day of the week",
    "saturday":"this is the seventh day of the week",
}

# Create your views here.
def viewweek (request):
    listofweek = list(dict_weekdays.keys())
    return render(request, 'weeks/weekdays.html', {'context': listofweek})
#..........................................
def home (request):
    return render(request, 'weeks/home.html' )