from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm
# Create your views here.


def index(request):
    person={
        'name':'Blessy Cheriyan',
        'age':25,
        'place':'Dubai'
    }
    nums={
        'num1':-2
    }
    Numbers={
        'num2':[1,2,3,4,5,6,7,8,9,10]
    }
    Fruits={
        'fruits_list':['banana','Apple','orange','pineapple','mango']
    }
    return render(request, 'index.html',Fruits)


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')   
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',dict_form)


def doctors(request):
    dict_doct={
        'doctors':Doctors.objects.all()
    }
    print("data:",dict_doct)
    return render(request, 'doctors.html',dict_doct)


def contacts(request):
    return render(request, 'contact.html')


def department(request):
    dict_dep={
        'dept':Departments.objects.all()
    }
    print("data:",dict_dep)
    return render(request, 'department.html',dict_dep)
