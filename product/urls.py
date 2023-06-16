from django.urls import path
from .views import *

urlpatterns = [

    # path('electronics',Electronics,name="Electronics"),
    # path('groceries',Groceries,name="Groceries"),
    # path('clothes',Clothes,name="Cloths"),
    # path('home&kitchen',Home_Kitchen,name="Home_Kitchen"),
    path('product_all/<str:pname>',Product,name="product_all"),
    path('common/',Common,name="common"),
]