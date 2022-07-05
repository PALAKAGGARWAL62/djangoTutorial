from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from .models import Fruit

# Create your views here.
def home(request):
    context = {'Name': 'Esha', 'date':datetime.now(),}
    if request.method == 'POST':
        y = request.POST.get('year')
        s = ''
        if y is not None:
            y = int(y)
            if y%100==0:
                if y%400==0:
                    s = 'Leap year'
                else: s = 'Non Leap year'

            elif y%100!=0:
                if y%4 == 0:
                    s = 'Leap year'
                else: s = 'Non Leap year'
        context['year']=y 
        context['leap']=s
        print(context)
        return render(request, 'poll/home.html', context=context)
    if request.method=='GET':
        return render(request, 'poll/home.html', context=context)
    # return HttpResponse('<h1>Hello There</h1>')


def page1(request):
    if request.method=='POST':
        # print(request.POST)
        kw = {
            'name':request.POST.get('name'),
            'color':request.POST.get('color'),
            'taste':request.POST.get('taste'),
            'price':request.POST.get('price'),
            'quantity':request.POST.get('quantity'),
        }
        f = Fruit.objects.filter(name__iexact=kw['name'])
        if not f.exists():
            f = Fruit.objects.create(**kw)
            # f.price=100
            # f.save()
        return redirect('/page1', permanent=True)
    elif request.method=='GET':
        print(request.GET)

    # select * from fruit where color = 'red'
    f = Fruit.objects.all()
    f1 = Fruit.objects.filter(color__iexact='yellow')
    # print(f.values())
    # print(f.values()[0])
    context = {'fruits':f.values(), 'yf':f1.values()}
    return render(request, 'poll/page1.html', context)

'''
DDL - creation of tables, alter table structure, delete tables
DML - insertion, deletion, read, update (CRUD) 
DCL - grant, revoke, roles
Tcl - commit, rollback, savepoint 
'''