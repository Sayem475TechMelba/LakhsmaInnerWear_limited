from django.contrib.auth import get_user_model

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

from django.db.models import Sum
from Merchandise.models import *
from django.db.models.functions import TruncMonth, TruncYear
from django.db.models import Count

from Merchandise import models as mer_models

from django.forms import inlineformset_factory
from django.urls import reverse
from django import views
from django.views import View
from django.contrib import messages, auth
from Purchase.filters import PurchaseFilter, ChalanFilter
import datetime
import json
from . import helper
from datetime import date

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required, user_passes_test


User = get_user_model()
# Create your views here.
user_login_required = user_passes_test(lambda user: user.is_active, login_url='/')

def active_user_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func

@active_user_required
def home(request):
    if request.method == 'GET':
        if len(request.GET) == 0:
            return render(request, 'Home/home.html', {
                'api_ov' : json.dumps(helper.graphAPI(mer_models.OrderEntryInfo.objects, mer_models.PO_Details.objects, date.today().year))
            })
        else:
            print(request.GET.get('year'))
            return render(request, 'Home/home.html', {
                'api_ov' : json.dumps(helper.graphAPI(mer_models.OrderEntryInfo.objects, mer_models.PO_Details.objects, int(request.GET.get('year'))))
            })

# START ====API FOR GRAPH - USING SERIALIZERS - DJANGO REST FRAMEWORKS====
def get_data(request, *args, **kwargs):
    data ={
        "sales":100,
        "customers":10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = []
        datas = []
        today = datetime.datetime.now()
        queryset = PO_Details.objects.annotate(month=TruncMonth('pub_shipment_date')).values('month').annotate(total_amount=Sum('amount')).values('month', 'total_amount').filter(pub_shipment_date__year=today.year) 
        # print(queryset)
        for entry in queryset:
            labels.append(entry['month'])
            datas.append(entry['total_amount'])
        data ={
        "labels":labels,
        "datas":datas,
        }
        return Response(data)

# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         # qs_count =User.objects.all().count()
#         # label= [month]
#         # data= [orderValue]
#         # labels = ['USERS','JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
#         # default = [qs_count, 5, 10, 15, 20, 25, 30, 5, 40, 30, 30,36, 3 ]
#         data ={
#         "labels":labels,
#         "default":default,
#         }
#         return Response(data)
# FINISH ==== API FOR GRAPH - USING SERIALIZERS - DJANGO REST FRAMEWORKS====


def login(request):
    return render(request, 'Accounts/login.html')

def lib_bank(request):
    banks = Bank.objects.all()
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library Bank info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = BankForm()
    context ={
        'form':form,
        'banks':banks,
    }
    return render(request, 'Purchase/Library/lib_bank.html', context)

def edit_bank(request, id):
    bank = Bank.objects.get(id = id)
    form = BankForm(instance=bank)
    if request.method == 'POST':
        form = BankForm(request.POST,  instance = bank)
        if form.is_valid():
            form.save()
            messages.success(request, "Your bank info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Purchase/Library/edit_lib_bank.html',context)

def delete_bank(request,id):
    bank = Bank.objects.get(id = id)
    bank.delete()
    return redirect('lib_bank')

def lib_branch(request):
    branch = BankBranch.objects.all()
    if request.method == 'POST':
        form = BankBranchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library Bank Branch info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = BankBranchForm()
    context ={
        'form':form,
        'branch':branch,
    }
    return render(request, 'Purchase/Library/bank_branch.html', context)

def edit_branch(request, id):
    branch = BankBranch.objects.get(id = id)
    form = BankBranchForm(instance=branch)
    if request.method == 'POST':
        form = BankBranchForm(request.POST,  instance = branch)
        if form.is_valid():
            form.save()
            messages.success(request, "Your bank branch info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Purchase/Library/edit_lib_branch.html',context)

def delete_branch(request,id):
    branch = BankBranch.objects.get(id = id)
    branch.delete()
    return redirect('lib_branch')

def lib_bank_address(request):
    bank_address = BankAddress.objects.all()
    if request.method == 'POST':
        form = BankAddressForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library Bank Address info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = BankAddressForm()
    context ={
        'form':form,
        'bank_address':bank_address,
    }
    return render(request, 'Purchase/Library/branch_address.html', context)

def edit_address(request, id):
    bank_address = BankAddress.objects.get(id = id)
    form = BankAddressForm(instance=bank_address)
    if request.method == 'POST':
        form = BankAddressForm(request.POST,  instance = bank_address)
        if form.is_valid():
            form.save()
            messages.success(request, "Your bank address info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Purchase/Library/edit_address.html',context)

def delete_address(request,id):
    bank_address = BankAddress.objects.get(id = id)
    bank_address.delete()
    return redirect('lib_bank_address')

def purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            data = form.save()
            check = Chechboxes(
                fc = data,
                btb = helper.conv2b(request, "lc"),
                pc = helper.conv2b(request, "pc"),
                snd = helper.conv2b(request, "snd"),
                term = helper.conv2b(request, "term"),
                time = helper.conv2b(request, "time"),
                od = helper.conv2b(request, "od"),
                edf = helper.conv2b(request, "edf"),
                buying = helper.conv2b(request, "buying"),
                tax = helper.conv2b(request, "tax")
            )
            check.save()
            # Generate purchase number
            purchase_no = str('LAK-EXP-PUR-' + str(data.id))
            inserted_by = request.user
            form.instance.inserted_by = inserted_by
            form.instance.purchase_no = purchase_no
            form.save()
            messages.success(request, "Your bank purchase info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = PurchaseForm()
    purchase_list = PurchaseBank.objects.all().order_by('-id')[:1]
    
    return render(request, 'Purchase/purchase.html', {'form':form, 'purchase_list':purchase_list})

def bank(req):
    bank = BankAddress.objects.all()
    bank_dict = {}
    for i in bank:
        if i.branch.bank.bank_name not in bank_dict:
            bank_dict[i.branch.bank.bank_name] = helper.temp_dict(i)
        else:
            bank_dict[i.branch.bank.bank_name][i.branch.branch_name] = i.address_name

    return HttpResponse(json.dumps(bank_dict))


def view_purchase(request, id):
    item = PurchaseBank.objects.get(id = id)
    context = {
        'item': item
    }
    return render(request, 'Purchase/view_purchase.html', context)

def update_purchase(request,id):
    item = PurchaseBank.objects.get(id = id)
    form = PurchaseForm(instance=item)
    pre_check = Chechboxes.objects.get(fc=item)
    if request.method == 'POST':
        form = PurchaseForm(request.POST,  instance = item)
        if form.is_valid():
            form.save()
            pre_check.delete()
            check = Chechboxes(
                fc = item,
                btb = helper.update(request, "btb_lc_check"),
                pc = helper.update(request, "pc_amount_check"),
                snd = helper.update(request, "snd_amount_check"),
                term = helper.update(request, "term_loan_check"),
                time = helper.update(request, "time_load_check"),
                od = helper.update(request, "od_load_check"),
                edf = helper.update(request, "edf_interest_check"),
                buying = helper.update(request, "buying_com_check"),
                tax = helper.update(request, "tax_other_check")
            )
            check.save()
            print(request.POST.get('btb_lc_check'))
            messages.success(request, "Your Purchase info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    final = Chechboxes.objects.get(fc=item)
    context = {'form':form, "cb":final}
    return render(request, "Purchase/edit_purchase.html",context)


def print_purchase(request, id):
    item = PurchaseBank.objects.get(id = id)
    context ={
        'item':item,
        }
    return render(request, "Purchase/print_purchase.html", context)


def delete_purchase(request, id):
    item = PurchaseBank.objects.get(id = id)
    item.delete()
    return redirect('purchase_report')

def purchase_report(request):
    purchase_list = PurchaseBank.objects.all().order_by('-id')
    myFilter = PurchaseFilter(request.GET , queryset = purchase_list)
    purchase_list = myFilter.qs
    context = {
        'purchase_list': purchase_list,
        'myFilter':myFilter,
        
    }
    return render(request, 'Purchase/purchase_report.html', context)
    
def deliveryChalan(request):
    chalan = ShipmentChalan.objects.all().order_by('-id')[:1]
    if request.method == "GET":
        form = Sh_Form()
        items_factory = inlineformset_factory(ShipmentChalan, ShipmentChalanItems, form=Sh_ItemsForm, extra=1)
        form_item = items_factory()
        context = {
            'form': form,
            'form_item': form_item,
            'chalan': chalan,
        }
        return render(request, "Chalan/deliveryChalan.html", context)

    elif request.method == "POST":
        form = Sh_Form(request.POST, request.FILES)
        items_factory = inlineformset_factory(ShipmentChalan, ShipmentChalanItems, form=Sh_ItemsForm)
        form_item = items_factory(request.POST)
        if form.is_valid() and form_item.is_valid():
            breakdown = form.save()
            form_item.instance = breakdown
            form_item.save()
            
            # Generate challan number
            chalan_no = str('LAK-CHA-SHI-' + str(breakdown.id))
            inserted_by = request.user
            form.instance.chalan_no = chalan_no
            form.instance.inserted_by = inserted_by
            form.save()
            messages.success(request, 'Your delivery chalan info has been Added Successfully...')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
            # chalan = ShipmentChalan.objects.all().order_by('-id')[:1]
            chalan = ShipmentChalan.objects.latest('id')
            context = {
                        'form': form,
                        'form_item': form_item,
                        'chalan': chalan,
                    }
            return render(request, 'Chalan/deliveryChalan.html', context)

def editChalan(request, id):
    if request.method == "GET":
        obj = ShipmentChalan.objects.filter(id=id).first()
        if obj is None:
            return redirect(reverse('deliveryChalan'))
        form = Sh_Form(instance=obj)
        items_factory = inlineformset_factory(ShipmentChalan, ShipmentChalanItems, form=Sh_ItemsForm, extra=0)
        form_item = items_factory(instance=obj)
        context = {
            'form': form,
            'form_item': form_item,
        }
        return render(request, "Chalan/editChalan.html", context)

    elif request.method == "POST":
        obj = ShipmentChalan.objects.filter(id=id).first()
        if obj is None:
            return redirect(reverse('deliveryChalan'))
        form = Sh_Form(request.POST, request.FILES, instance=obj)
        items_factory = inlineformset_factory(ShipmentChalan, ShipmentChalanItems, form=Sh_ItemsForm, extra=1)
        form_item = items_factory(request.POST, instance=obj)
        if form.is_valid() and form_item.is_valid():
            breakdown = form.save()
            form_item.instance = breakdown
            form_item.save()
            messages.success(request, 'Your delivery chalan info has been updated Successfully...')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
            print(form_item.errors)
            context = {
                        'form': form,
                        'form_item': form_item,
                    }
            return render(request, "Chalan/editChalan.html", context)
        
def delivery_chalan_report(request):
    chalan = ShipmentChalan.objects.all().order_by('-id')
    myFilter = ChalanFilter(request.GET , queryset = chalan)
    chalan = myFilter.qs
    context = {
        'myFilter': myFilter,
        'chalan': chalan,
    }
    return render(request, 'Chalan/delivery_chalan_report.html', context)

def viewChalan(request, id):
    item = ShipmentChalan.objects.get(id=id)
    context = {
        'item': item,
    } 
    return render(request, 'Chalan/viewChalan.html', context)

def print_Challan(request, id):
    item = ShipmentChalan.objects.get(id=id)
    context = {
        'item': item,
    } 
    return render(request, 'Chalan/print_Challan.html', context)

def delete_Challan(request, id):
    item = ShipmentChalan.objects.get(id=id)
    item.delete()
    return redirect('delivery_chalan_report')

