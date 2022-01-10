from django.urls import path
from . import views

urlpatterns=[
    path('<int:sl>', views.test_mail)
]