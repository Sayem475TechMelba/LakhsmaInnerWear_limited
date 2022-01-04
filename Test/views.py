from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages, auth
from Merchandise.forms import *
from Merchandise.models import *
from Merchandise.filters import *
from django.forms import inlineformset_factory
from django.urls import reverse

# Create your views here.
def edit_order(request,id):
    if request.method == "GET":
        obj = OrderEntryInfo.objects.get(id=id)
        form_smv_items = SmvItems.objects.filter(order_smv=obj)
        context = {
            'form_smv_item': form_smv_items,
        }
        return render(request, "Test/test.html", context)