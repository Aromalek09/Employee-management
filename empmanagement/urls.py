from django.urls import path
from .views import *

urlpatterns=[
    path('home',HomeView.as_view(),name='home'),
    path('add',AddEmployee.as_view(),name='add'),
    path('edit/<int:id>',editemployeeview.as_view(),name='edit'),
    path('del/<int:id>',deleteemployee.as_view(),name='del'),
    path('changepswd',changepassword,name='changepswd'),
    path('search',SearchEmployee,name='search'),
]