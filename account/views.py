from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from income.models import Income
from expense.models import Expense
from .models import UserInfo, UserInfoForm,UserForm
def home(request):
    uid=request.session.get('uid')
    incl=Income.objects.filter(user=uid)
    expl=Expense.objects.filter(user=uid)
    total_incom=0
    total_expense=0
    for i in incl:
        total_incom=total_incom+i.income
    
    for i in expl:
        total_expense=total_expense+i.expense
    balance=total_incom-total_expense
    context={'bal':balance}
    return render(request,"home.html",context)

def register(request):
    if request.method=='POST':
        f=UserForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context={'form':UserForm}
        return render(request,'adduser.html',context)

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)

        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            context={'lmsg':"UserName And Passwprd is Not Valid"}
            return render(request,"login.html",context)
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def edit_profile(request):
    uid=request.session.get('uid')
    user=UserInfo.objects.get(user_ptr=uid)
    if request.method=='POST':
        u=UserInfoForm(request.POST,instance=user)
        u.save()
        return redirect('/')

    else:
        f=UserInfoForm(instance=user)
        context={'form':f}
        return render(request,'updateuser.html',context)