from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

def index(request):
    return HttpResponse("hello world")


dict_months = {
    'january':"this is the first month",
    "february":"This is the second month",
    "march":"this is the third month",
    "april":"this is the fourth month",
    "may":"this is the fifth month",
    "june":"this is the sixth month",
    "july":"this is the seventh month",
    "august":"this is the eighth month",
    "september":"this is the ninth month",
    "october":"this is the tenth month",
    "november":"this is the eleventh month",
    "december":"this is the twelveth month",
}
#..........................................
dict_weekdays = {
    "sunday":"this is the first day of the week",
    "monday":"this is the second day of the week",
    "tuesday":"this is the third day of the week",
    "wednesday":"this the fourth day of the week",
    "thursday":"this the fifth day of the week",
    "friday":"this is the sixth day of the week",
    "saturday":"this is the seventh day of the week",
}


#.....................................................
def dynamic_int(request, num):
    lst_keys = list(dict_months.keys())
    if num>len(lst_keys) or num==0:
        return HttpResponseNotFound('please enter a valid number')

#...........................................................
def dynamic_str(request, m):
    data= dict_months.get(m)
    if data:
        return HttpResponse(f'{m} : {data}')
    return HttpResponseNotFound(f"no such month {m}")
#---------------------------------------------------
def viewmonths (request):
    lst_months=list(dict_months.keys())
    lst_items=''
    for i in lst_months:
        lst_items+=f"<ul><li><a href='{i}'>{i}</a></li></ul>"
    return HttpResponse(lst_items)
#---------------------------------------------------
def viewsample(request):
    context = {'name': 'World'}  # Provide a default value for 'name'
    return render(request, 'months/homepage.html', context)
#...............................................................
def viewmonths1 (request):
    listofmonths = list(dict_months.keys())
    return render (request, 'months/homepage2.html', {'context': listofmonths})
#.................................
def viewadd (request):
    d={'a':120 , 'b':320}
    return render(request, 'months/math.html',d)
#.........................................
def viewweek (request):
    listofweek = list(dict_weekdays.keys())
    return render(request, 'months/weekdays.html', {'context': listofweek})