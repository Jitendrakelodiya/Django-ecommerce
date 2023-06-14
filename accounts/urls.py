from django.urls import path
from .views import *

urlpatterns = [
    path('register/',Register_page,name="register"),
    path('login/',Login_page,name="login"),
    path('user_logout/',Logout_page,name="user_logout"),
    
]