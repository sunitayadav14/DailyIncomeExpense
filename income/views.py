from django.shortcuts import render,redirect
from .models import Income,IncomeForm
def add_income(request):
    if request.method=="POST":
        f=IncomeForm(request.POST)
        f.save()
        return redirect('/')
    else:
        context={'form':IncomeForm}
        return render(request,"addincome.html",context)
 
def income_list(request):
    uid=request.session.get("uid")
    incl=Income.objects.filter(user=uid)
    inc_amount=set()
    inc_type=set()
    inc_date=set()
    for i in incl:
        inc_amount.add(i.income)
        inc_date.add(i.incomeDate)
        inc_type.add(i.incomeType)
    context={'incl':incl,'inc_amount':inc_amount,'inc_type':inc_type,'inc_date':inc_date}
    return render(request,"incomelist.html",context)

def delete_income(request,id):
    inc=Income.objects.get(id=id)
    inc.delete()
    return redirect('/')

def getBy_income(request,income):
    uid=request.session.get("uid")
    
    incl1=Income.objects.filter(user=uid,income=income)
    incl=Income.objects.filter(user=uid)
    inc_amount=set()
    inc_type=set()
    inc_date=set()
    for i in incl:
        inc_amount.add(i.income)
        inc_date.add(i.incomeDate)
        inc_type.add(i.incomeType)
    context={'incl':incl1,'inc_amount':inc_amount,'inc_type':inc_type,'inc_date':inc_date}
    return render(request,"incomelist.html",context)

def getBy_date(request,bdate):
    uid=request.session.get("uid")
    
    incl1=Income.objects.filter(user=uid,incomeDate=bdate)
    incl=Income.objects.filter(user=uid)
    inc_amount=set()
    inc_type=set()
    inc_date=set()
    for i in incl:
        inc_amount.add(i.income)
        inc_date.add(i.incomeDate)
        inc_type.add(i.incomeType)
    context={'incl':incl1,'inc_amount':inc_amount,'inc_type':inc_type,'inc_date':inc_date}
    return render(request,"incomelist.html",context)

def getBy_type(request,type):
    uid=request.session.get("uid")
    
    incl1=Income.objects.filter(user=uid,incomeType=type)
    incl=Income.objects.filter(user=uid)
    inc_amount=set()
    inc_type=set()
    inc_date=set()
    for i in incl:
        inc_amount.add(i.income)
        inc_date.add(i.incomeDate)
        inc_type.add(i.incomeType)
    context={'incl':incl1,'inc_amount':inc_amount,'inc_type':inc_type,'inc_date':inc_date}
    return render(request,"incomelist.html",context)