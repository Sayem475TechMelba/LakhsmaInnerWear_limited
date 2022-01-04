from django.urls import path
from . import views

urlpatterns=[
    path('test/<int:id>', views.edit_order, name= 'edit')
]