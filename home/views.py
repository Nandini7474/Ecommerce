
from pyexpat.errors import messages
from django.shortcuts import render #render for temp
from django.http import HttpResponse
from home import admin 
from datetime import datetime
from home.models import contact

# Create your views here.
def index(request ,template='index.html'):  #bug no 5 by requesting template
    return render(request,template)
def about(request ):  #bug no 5 by requesting template
    return render(request,'about.html ')
def services(request ,template='services.html'):  #bug no 5 by requesting template
    return render(request,template)
def contact(request ,template='contact.html'): #bug no 5 by requesting template
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact= contact (name=name , email=email, phone=phone, desc=desc,date=datetime.tpday())
        contact.save()
        messages.success(request,'Your message has been sent!')
    return render(request,template)
 