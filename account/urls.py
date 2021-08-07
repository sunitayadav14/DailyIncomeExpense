

from django.urls import path
from .import views as v
urlpatterns = [
    path('register',v.register,name='adduser'),
    path('login',v.login_view,name="login"),
    path('logout',v.logout_view,name="logout"),
    path('-edit-profile',v.edit_profile,name='editprofile'),
]

 # 11 to 1

 

