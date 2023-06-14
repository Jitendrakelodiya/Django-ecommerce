from django.urls import path
from .views import *

urlpatterns = [

    path('electronics',Electronics,name="electronics"),
    path('groceries',Groceries,name="groceries"),
    path('clothes',Clothes,name="clothes"),
    path('home&kitchen',Home_Kitchen,name="home&kitchen"),
    path('common',Common,name="common"),
]