from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def apointment(request):
    if request.user.is_anonymous:
        return redirect("login_user")
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        text_area=request.POST.get('text_area')
        contact=apointment(name=name, email=email, phone_no=phone_no, text_area=text_area, date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been send!')
    return render(request, 'apointment.html')