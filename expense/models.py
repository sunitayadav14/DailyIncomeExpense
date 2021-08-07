from django.db import models
from django import forms
from django.contrib.auth.models import User

class Expense(models.Model):
    expense=models.IntegerField()
    expenseType=models.CharField(max_length=50)
    expenseDate=models.DateField()
    description=models.TextField(max_length=400)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="expense"


class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields='__all__'