from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('mobile',views.mobile,name="mobile"),
    path('laptop',views.laptop,name="laptop"),
    path('television',views.television,name="television"),
    path('washing_machine',views.washing_machine,name="washing_machine"),
    path('refrigerator',views.refrigerator,name="refrigerator"),
    path('air_conditioners',views.air_conditioners,name="air_conditioners"),
    path('tablets',views.tablets,name="tablets"),
    path('camera',views.camera,name="camera"),
    path('fashion/<str:cat>',views.fashion,name="fashion"),
    path('books',views.books,name="books"),
    path('headphones',views.headphones,name="books"),
    path('mobilead',views.mobilead,name="mobilead"),
]