
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('income',v.add_income,name="addincome"),
    path('list',v.income_list,name="inclist"),
    path('delete/<int:id>',v.delete_income,name="dincome"),
    path('by-incom/<int:income>',v.getBy_income,name="income"),
    path('by-date/<str:bdate>',v.getBy_date,name="bdate"),
    path('by-type/<str:type>',v.getBy_type,name="type"),
]

