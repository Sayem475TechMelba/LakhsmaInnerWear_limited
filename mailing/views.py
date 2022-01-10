from django.shortcuts import render
from django.http import HttpResponse
from . import helper
import datetime

# Create your views here.
def test_mail(request, sl):
    return HttpResponse(helper.test_data()[0].date)