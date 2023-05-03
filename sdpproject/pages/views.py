from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
# Create your views here.


def home(request):
    return render(request,"pages/home.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        user = User()
        user.username = username
        user.email = email
        user.set_password(password1)
        user.save()
        return  redirect('login')
    return render(request,"pages/register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        return redirect('home')

    return render(request,"pages/login.html")
def logoutuser(request):
    logout(request)
    return redirect('home')

def buy(request):
    return render(request,"pages/buy.html")

def explorewc(request):

    return render(request,"pages/explorewc.html")

def exploremc(request):
    return render(request,"pages/exploremc.html")

def exploremfc(request):
    return render(request,"pages/exploremfc.html")

def explorewfc(request):
    return render(request,"pages/explorewfc.html")

def explorekids(request):
    return render(request,"pages/explorekids.html")

def explorebg(request):
    return render(request,"pages/explorebg.html")

def explorewj(request):
    return render(request,"pages/explorewj.html")

def explorepb(request):
    return render(request,"pages/explorepb.html")

def cart(request):
    return render(request,"pages/cart.html")

def contactus(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        mail=request.POST['mail']
        country=request.POST['country']
        para=request.POST['para']
        user = ContactPage()
        user.username=username
        user.first_name = first_name
        user.last_name = last_name
        user.mail=mail
        user.country=country
        user.para=para
        user.save()
        return  redirect('contactus')
    return render(request,"pages/contactus.html")

def checkout(request):
    return render(request,"pages/checkout.html")

def sell(request):
    if request.method=='POST':
        cname=request.POST['cname']
        pname=request.POST['pname']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        city=request.POST['city']
        zipcode=request.POST['zipcode']
        ptype=request.POST['ptype']
        price=request.POST['price']
        prange=request.POST['prange']
        comment=request.POST['comment']

        user=SellPage()

        user.cname=cname
        user.pname=pname
        user.email=email
        user.phone=phone
        user.address=address
        user.city=city
        user.zipcode=zipcode
        user.ptype=ptype
        user.price=price
        user.prange=prange
        user.comment=comment

        user.save()

    return render(request,"pages/sell.html")

def aboutus(request):
    return render(request,"pages/aboutus.html")









