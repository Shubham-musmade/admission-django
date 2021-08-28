from home.models import High_admission, Re_admission, Pri_admission
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, redirect
from datetime import datetime

def pri_admission(request):
    if request.user.is_anonymous:
        return redirect("login_user")
    if request.method =='POST':
        student_name=request.POST.get('student_name')
        student_email=request.POST.get('student_email')
        student_phone_no=request.POST.get('student_phone_no')
        student_class=request.POST.get('student_class')
        student_text_area=request.POST.get('student_text_area')
        pri_admission=Pri_admission(student_name=student_name, student_email=student_email, student_phone_no=student_phone_no,student_class=student_class, student_text_area=student_text_area, date=datetime.today())
        pri_admission.save()
        messages.success(request,'Your admission request has been send!')
    return render(request, 'pri_admission.html')

def high_admission(request):
    if request.user.is_anonymous:
        return redirect("login_user")
    if request.method =='POST':
        student_name=request.POST.get('student_name')
        student_email=request.POST.get('student_email')
        student_phone_no=request.POST.get('student_phone_no')
        student_class=request.POST.get('student_class')
        student_text_area=request.POST.get('student_text_area')
        high_admission=High_admission(student_name=student_name, student_email=student_email, student_phone_no=student_phone_no,student_class=student_class, student_text_area=student_text_area, date=datetime.today())
        high_admission.save()
        messages.success(request,'Your admission request has been send!')
    return render(request, 'high_admission.html')

def reclass(request):
    if request.user.is_anonymous:
        return redirect("login_user")
    if request.method =='POST':
        student_name=request.POST.get('student_name')
        student_email=request.POST.get('student_email')
        student_phone_no=request.POST.get('student_phone_no')
        student_class=request.POST.get('student_class')
        student_text_area=request.POST.get('student_text_area')
        re_admission=Re_admission(student_name=student_name, student_email=student_email, student_phone_no=student_phone_no,student_class=student_class, student_text_area=student_text_area, date=datetime.today())
        re_admission.save()
        messages.success(request,'Your re-admission message has been send!')
    return render(request, 'reclass.html')