from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact, Apointment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    # context={
    #     'var': a  #""""this is the value of var thankyou son much """"
    # } this is for inputing some values 
    return render(request, 'index.html')
    # return HttpResponse("hi this is shubham musmade") """this is for non html templates"

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        #to check the user habing same credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request,'loginuser.html')
    return render(request,'loginuser.html')

def logout_user(request):
    logout(request)
    return redirect('/login_user')

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        text_area=request.POST.get('text_area')
        contact=Contact(name=name, email=email, phone_no=phone_no, text_area=text_area, date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been send!')
    return render(request, 'contact.html')

def apointment(request):
    if request.user.is_anonymous:
        return redirect("login_user")
    if request.method =='POST':
        a_name=request.POST.get('a_name')
        a_email=request.POST.get('a_email')
        a_phone_no=request.POST.get('a_phone_no')
        a_text_area=request.POST.get('a_text_area')
        apointment=Apointment(a_name=a_name, a_email=a_email, a_phone_no=a_phone_no, a_text_area=a_text_area, date=datetime.today())
        apointment.save()
        messages.success(request,'Your message has been send!')
    return render(request, 'apointment.html')

def about_us(request):
    return render(request, 'about_us.html')


def sign_up(request):
    if request.method =='POST':
        username = request.POST['username']
        email= request.POST['email']
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        password1= request.POST['password1']
        # password2= request.POST['password2']

        #creating user 
        myuser = User.objects.create_user(username,email,password1)
        myuser.firstname=firstname
        myuser.lastname=lastname
        myuser.save()
        messages.success(request,"Your acount has been created successfully")
        return redirect('login_user')
    else:
        return render(request,'signup_user.html')

