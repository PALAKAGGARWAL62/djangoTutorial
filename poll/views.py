from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import Fruit

# Create your views here.
def home(request):
    print('------->', request.GET)
    y = request.GET.get('year')
    context = {'Name': 'Esha', 'date':datetime.now(), 'year':y, }

    return render(request, 'poll/home.html', context=context)
    return HttpResponse('<h1>Hello There</h1>')


def page1(request):
    # select * from fruit
    f = Fruit.objects.all()
    # print(f.values())
    # print(f.values()[0])
    context = {'fruits':f.values()}
    return render(request, 'poll/page1.html', context)