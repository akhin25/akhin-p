from django.shortcuts import render
from django.http import HttpResponse

from .models import Departments
from .models import Doctors
from .forms import BookingForm
from .models import Contact

# Create your views here.
def index(request):
    numbers={
        'fruits':['apple','banana']
    }


    return render(request, 'index.html',numbers)

def about (request):
    return render(request, 'about.html')


def booking (request):
    if request.method == "POST":
        form= BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',dict_form)

def doctors (request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)

def contact (request):
    dict_contact={
        'contact':Contact.objects.all()
    }
    return render(request, 'contact.html',dict_contact)

def department (request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request, 'department.html',dict_dept)
