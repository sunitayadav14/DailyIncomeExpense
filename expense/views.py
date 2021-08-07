from django.shortcuts import render,redirect
from .models import  Expense,ExpenseForm

def add_expense(request):
    if request.method=="POST":
        f=ExpenseForm(request.POST)
        f.save()
        return redirect('/') 
    else:
        context={'form':ExpenseForm}
        return render(request,"addexpense.html",context)


def expense_list(request):
    uid = request.session.get("uid")
    expl=Expense.objects.filter(user=uid)
    context={'expl':expl}
    return render(request,"expenselist.html",context)


def expenses_search(request):
    data=request.POST.get('search')
    uid=request.session.get("uid")
    expl=Expense.objects.filter(user=uid,description__contains=data)
    context={'expl':expl}
    return render(request,"expenselist.html",context)
