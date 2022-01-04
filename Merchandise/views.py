from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages, auth
from .forms import *
from .models import *
from Merchandise.filters import *
from django.forms import inlineformset_factory
from django.urls import reverse
from . import helper
from django.db.models import Sum, Avg, F, FloatField

# Create your views here.
################## ALL Library Forms Views ###############
def lib_buyer(request):
    buyers = LibraryBuyer.objects.all()
    if request.method == 'POST':
        form = LibBuyerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library buyer info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibBuyerForm()
    context ={
        'form':form,
        'buyers':buyers,
    }
    return render(request, 'Merchandising/Library/lib_buyer.html', context)

def lib_company(request):
    company = LibraryCompany.objects.all()
    if request.method == 'POST':
        form = LibCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your company info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibCompanyForm()
    context ={
        'form':form,
        'company':company,
    }
    return render(request, 'Merchandising/Library/lib_company.html', context)

def lib_company_address(request):
    if request.method == 'POST':
        form = LibCompAddressForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library company address info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibCompAddressForm()
    return render(request, 'Merchandising/Library/lib_company_address.html', {'form':form})

def lib_product_cate(request):
    productCat = LibraryProductCate.objects.all()
    if request.method == 'POST':
        form = LibProductCateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library product department info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibProductCateForm()
    context ={
        'form':form,
        'productCat':productCat,
    }
    return render(request, 'Merchandising/Library/lib_product_cate.html', context)

def lib_prod_dept(request):
    productDept = LibraryProdDept.objects.all()

    if request.method == 'POST':
        form = LibProdDeptForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library product department info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibProdDeptForm()
    context ={
        'form':form,
        'productDept':productDept,
    }
    return render(request, 'Merchandising/Library/lib_prod_dept.html', context)

def lib_prod_subdept(request):
    productSubDept = LibraryProdSubDept.objects.all()
    if request.method == 'POST':
        form = LibProdSubDeptForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library product sub department info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibProdSubDeptForm()
    context ={
        'form':form,
        'productSubDept':productSubDept,
    }
    return render(request, 'Merchandising/Library/lib_prod_subdept.html', context)

# def lib_product_cate(request):
#     if request.method == 'POST':
#         form = LibProductCateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your library product category info has been recorded!")
#             return HttpResponseRedirect(request.path_info)
#         else:
#             messages.error(request , "Something went wrong!")
#             print(form.errors)
#     form = LibProductCateForm()
#     return render(request, 'Merchandising/Library/lib_product_cate.html', {'form':form})

def lib_team_leader(request):
    teamleader = LibraryTeamLeader.objects.all()

    if request.method == 'POST':
        form = LibTeamLeaderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library team leader info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibTeamLeaderForm()
    context ={
        'form':form,
        'teamleader':teamleader,
    }
    return render(request, 'Merchandising/Library/lib_team_leader.html',context)

def lib_dealing_merchant(request):
    dealMerchant = LibraryDealingMerchant.objects.all()

    if request.method == 'POST':
        form = LibDealingMerchantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library dealing merchant info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibDealingMerchantForm()
    context ={
        'form':form,
        'dealMerchant':dealMerchant,
    }
    return render(request, 'Merchandising/Library/lib_dealing_merchant.html', context)

def lib_factory_merchant(request):
    factMerchant = LibraryFactoryMerchant.objects.all()

    if request.method == 'POST':
        form = LibFactoryMerchantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library factory merchant info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibFactoryMerchantForm()
    context ={
        'form':form,
        'factMerchant':factMerchant,
    }
    return render(request, 'Merchandising/Library/lib_factory_merchant.html',context)

# def lib_season( request):
#     seasons = LibrarySeason.objects.all()
#     if request.POST:
#         form = LibSeasonForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.save()
#         else:
#             messages.error(request , "Something went wrong!")
#             print(form.errors)
        
#     else:
#         default_value= 0
#         id =request.POST.get('id')
#         query = LibrarySeason.objects.filter(pk=id).first()
#         form = LibSeasonForm(instance=query)
#     return render(request, 'Merchandising/Library/lib_season.html', {'form':form, 'seasons':seasons})

def lib_season(request):
    seasons = LibrarySeason.objects.all()

    if request.method == 'POST':
        form = LibSeasonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library season info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibSeasonForm()
    context ={
        'form':form,
        'seasons':seasons,
    }
    return render(request, 'Merchandising/Library/lib_season.html', context)

def lib_region(request):
    regions = LibraryRegion.objects.all()

    if request.method == 'POST':
        form = LibRegionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library region info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibRegionForm()
    context ={
        'form':form,
        'regions':regions,
    }
    return render(request, 'Merchandising/Library/lib_region.html', context)

def lib_agent(request):
    agent = LibraryAgent.objects.all()
    if request.method == 'POST':
        form = LibAgentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library agent info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibAgentForm()
    context ={
        'form':form, 
        'agent':agent,
    }
    return render(request, 'Merchandising/Library/lib_agent.html',context)

def lib_client(request):
    clients = LibraryClient.objects.all()

    if request.method == 'POST':
        form = LibClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library client info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibClientForm()
    context ={
        'form':form, 
        'clients':clients,
    }
    return render(request, 'Merchandising/Library/lib_client.html', context)

def lib_currency(request):
    currency = LibraryCurrency.objects.all()

    if request.method == 'POST':
        form = LibCurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library currency info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibCurrencyForm()
    context ={
        'form':form, 
        'currency':currency,
    }
    return render(request, 'Merchandising/Library/lib_currency.html', context)

def lib_packing(request):
    packing = LibraryPacking.objects.all()

    if request.method == 'POST':
        form = LibPackingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library Packing info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibPackingForm()
    context ={
        'form':form, 
        'packing':packing,
    }
    return render(request, 'Merchandising/Library/lib_packing.html', context)

def lib_shipmode(request):
    shipping = LibraryShipMode.objects.all()

    if request.method == 'POST':
        form = LibShipModeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library Ship Mode info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibShipModeForm()
    context ={
        'form':form, 
        'shipping':shipping,
    }
    return render(request, 'Merchandising/Library/lib_shipmode.html', context)

def lib_qualitylabel(request):
    quality = LibraryQualityLabel.objects.all()

    if request.method == 'POST':
        form = LibQualityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library Quality info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibQualityForm()
    context ={
        'form':form, 
        'quality':quality,
    }
    return render(request, 'Merchandising/Library/lib_qualitylabel.html', context)

def lib_unit(request):
    order_unit = LibraryUnit.objects.all()

    if request.method == 'POST':
        form = LibUnitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library order unit info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibUnitForm()
    context ={
        'form':form, 
        'order_unit':order_unit,
    }
    return render(request, 'Merchandising/Library/lib_unit.html', context)

def lib_shipment_term(request):
    term = LibraryShipmentTerm.objects.all()

    if request.method == 'POST':
        form = LibShipmentTermForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library shipment term info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibShipmentTermForm()
    context ={
        'form':form, 
        'term':term,
    }
    return render(request, 'Merchandising/Library/lib_shipment_term.html', context)

def lib_design_source(request):
    source = LibraryDesignSource.objects.all()

    if request.method == 'POST':
        form = LibDesignSourceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library design source info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibDesignSourceForm()
    context ={
        'form':form, 
        'source':source,
    }
    return render(request, 'Merchandising/Library/lib_design_source.html', context)

def lib_country(request):
    country = LibraryCountry.objects.all()

    if request.method == 'POST':
        form = LibCountryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library country info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibCountryForm()
    context ={
        'form':form, 
        'country':country,
    }
    return render(request, 'Merchandising/Library/lib_country.html', context)

def lib_country_type(request):
    country_type = LibraryCountryType.objects.all()

    if request.method == 'POST':
        form = LibCountryTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library country type info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibCountryTypeForm()
    context ={
        'form':form, 
        'country_type':country_type,
    }
    return render(request, 'Merchandising/Library/lib_country_type.html', context)

def lib_cut_off(request):
    cutoff = LibraryCutOff.objects.all()

    if request.method == 'POST':
        form = LibCutOffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library cut-off info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibCutOffForm()
    context ={
        'form':form, 
        'cutoff':cutoff,
    }
    return render(request, 'Merchandising/Library/lib_cut_off.html', context)
def lib_gmt_prod(request):
    prods = LibraryProduct.objects.all()

    if request.method == 'POST':
        form = LibProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library product info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibProductForm()
    context ={
        'form':form, 
        'prods':prods,
    }
    return render(request, 'Merchandising/Library/lib_product.html', context)

def lib_payment_term(request):
    payment_term = LibraryPaymentTerm.objects.all()

    if request.method == 'POST':
        form = LibPaymentTermForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library payment term info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibPaymentTermForm()
    context ={
        'form':form, 
        'payment_term':payment_term,
    }
    return render(request, 'Merchandising/Library/lib_payment_term.html', context)

def lib_fabrication(request):
    fabrications = LibraryFabrication.objects.all()

    if request.method == 'POST':
        form = LibFabricationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library fabrication info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibFabricationForm()
    context ={
        'form':form, 
        'fabrications':fabrications,
    }
    return render(request, 'Merchandising/Library/lib_fabrications.html', context)

########### EDIT LIBRARY FORMS ##########
def edit_agent(request,id):
    agent = LibraryAgent.objects.get(id = id)
    form = LibAgentForm(instance=agent)
    if request.method == 'POST':
        form = LibAgentForm(request.POST,  instance = agent)
        if form.is_valid():
            form.save()
            messages.success(request, "Your agent info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_lib_agent.html',context)

def delete_agent(request,id):
    agent = LibraryAgent.objects.get(id = id)
    agent.delete()
    return redirect('lib_agent')


def edit_buyer(request,id):
    buyer = LibraryBuyer.objects.get(id = id)
    form = LibBuyerForm(instance=buyer)
    if request.method == 'POST':
        form = LibBuyerForm(request.POST,  instance = buyer)
        if form.is_valid():
            form.save()
            messages.success(request, "Your buyer info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_buyer.html',context)

def delete_buyer(request,id):
    buyer = LibraryBuyer.objects.get(id = id)
    buyer.delete()
    return redirect('lib_buyer')

def edit_client(request,id):
    client = LibraryClient.objects.get(id = id)
    form = LibClientForm(instance=client)
    if request.method == 'POST':
        form = LibClientForm(request.POST,  instance = client)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Client info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_client.html',context)

def delete_client(request,id):
    client = LibraryBuyer.objects.get(id = id)
    client.delete()
    return redirect('lib_client')

def edit_company(request,id):
    company = LibraryCompany.objects.get(id = id)
    form = LibCompanyForm(instance=company)
    if request.method == 'POST':
        form = LibCompanyForm(request.POST,  instance = company)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Company info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_company.html',context)

def delete_company(request,id):
    cmp = LibraryCompAddress.objects.get(id = id)
    cmp.delete()
    return redirect('lib_company')

# def edit_companyAddress(request,id):
#     cmpadd = LibraryCompAddress.objects.get(id = id)
#     form = LibCompAddressForm(instance=cmpadd)
#     if request.method == 'POST':
#         form = LibCompAddressForm(request.POST,  instance = cmpadd)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your Company Address info has been updated!")
#             return HttpResponseRedirect(request.path_info)
#         else:
#             messages.error("Something went wrong!")
#             print(form.errors)
#     context = {'form':form}
#     return render(request, 'Merchandising/Library/Edit_Library/edit_compAddress.html',context)

# def delete_compAddress(request,id):
#     cmpadd = LibraryCompAddress.objects.get(id = id)
#     cmpadd.delete()
#     return redirect('lib_company_address')

def edit_prodDept(request,id):
    prodDept = LibraryProdDept.objects.get(id = id)
    form = LibProdDeptForm(instance=prodDept)
    if request.method == 'POST':
        form = LibProdDeptForm(request.POST,  instance = prodDept)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Department info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_prodDept.html',context)

def delete_prodDept(request,id):
    prodDept = LibraryProdDept.objects.get(id = id)
    prodDept.delete()
    return redirect('lib_prod_dept')

def edit_prodSubDept(request,id):
    prodSubDept = LibraryProdSubDept.objects.get(id = id)
    form = LibProdSubDeptForm(instance=prodSubDept)
    if request.method == 'POST':
        form = LibProdSubDeptForm(request.POST,  instance = prodSubDept)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Sub Department info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_prodSubDept.html',context)

def delete_prodSubDept(request,id):
    prodDept = LibraryProdDept.objects.get(id = id)
    prodDept.delete()
    return redirect('lib_prod_subdept')

def edit_prodcate(request,id):
    prodcate = LibraryProductCate.objects.get(id = id)
    form = LibProductCateForm(instance=prodcate)
    if request.method == 'POST':
        form = LibProductCateForm(request.POST,  instance = prodcate)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Category info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_prodCate.html',context)

def delete_prodcate(request,id):
    prodcate = LibraryProductCate.objects.get(id = id)
    prodcate.delete()
    return redirect('lib_product_cate')

def edit_teamleader(request,id):
    teamleader = LibraryTeamLeader.objects.get(id = id)
    form = LibTeamLeaderForm(instance=teamleader)
    if request.method == 'POST':
        form = LibTeamLeaderForm(request.POST,  instance = teamleader)
        if form.is_valid():
            form.save()
            messages.success(request, "Team Leader info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_teamleader.html',context)

def delete_teamleader(request,id):
    teamleader = LibraryTeamLeader.objects.get(id = id)
    teamleader.delete()
    return redirect('lib_team_leader')

def edit_dealMerchant(request,id):
    dealMerch = LibraryDealingMerchant.objects.get(id = id)
    form = LibDealingMerchantForm(instance=dealMerch)
    if request.method == 'POST':
        form = LibDealingMerchantForm(request.POST,  instance = dealMerch)
        if form.is_valid():
            form.save()
            messages.success(request, "Dealing Merchant info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_dealMerchant.html',context)

def delete_dealMerchant(request,id):
    dealMerch = LibraryDealingMerchant.objects.get(id = id)
    dealMerch.delete()
    return redirect('lib_dealing_merchant')

def edit_factMerchant(request,id):
    factMerch = LibraryFactoryMerchant.objects.get(id = id)
    form = LibFactoryMerchantForm(instance=factMerch)
    if request.method == 'POST':
        form = LibFactoryMerchantForm(request.POST,  instance = factMerch)
        if form.is_valid():
            form.save()
            messages.success(request, "Factory Merchant info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_factMerchant.html',context)

def delete_factMerchant(request,id):
    factMerch = LibraryFactoryMerchant.objects.get(id = id)
    factMerch.delete()
    return redirect('lib_factory_merchant')

def edit_season(request,id):
    season = LibrarySeason.objects.get(id = id)
    form = LibSeasonForm(instance=season)
    if request.method == 'POST':
        form = LibSeasonForm(request.POST,  instance = season)
        if form.is_valid():
            form.save()
            messages.success(request, "Season info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_season.html',context)

def delete_season(request,id):
    season = LibrarySeason.objects.get(id = id)
    season.delete()
    return redirect('lib_season')

def edit_region(request,id):
    region = LibraryRegion.objects.get(id = id)
    form = LibRegionForm(instance=region)
    if request.method == 'POST':
        form = LibRegionForm(request.POST,  instance = region)
        if form.is_valid():
            form.save()
            messages.success(request, "Region info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_region.html',context)

def delete_region(request,id):
    region = LibraryRegion.objects.get(id = id)
    region.delete()
    return redirect('lib_region')

def edit_currency(request,id):
    currency = LibraryCurrency.objects.get(id = id)
    form = LibCurrencyForm(instance=currency)
    if request.method == 'POST':
        form = LibCurrencyForm(request.POST,  instance = currency)
        if form.is_valid():
            form.save()
            messages.success(request, "Currency info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_currency.html',context)

def delete_currency(request,id):
    currency = LibraryCurrency.objects.get(id = id)
    currency.delete()
    return redirect('lib_currency')

def edit_packing(request,id):
    packing = LibraryPacking.objects.get(id = id)
    form = LibPackingForm(instance=packing)
    if request.method == 'POST':
        form = LibPackingForm(request.POST,  instance = packing)
        if form.is_valid():
            form.save()
            messages.success(request, "Packing info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_packing.html',context)

def delete_packing(request,id):
    packing = LibraryPacking.objects.get(id = id)
    packing.delete()
    return redirect('lib_packing')

def edit_shipmode(request,id):
    shipmode = LibraryShipMode.objects.get(id = id)
    form = LibShipModeForm(instance=shipmode)
    if request.method == 'POST':
        form = LibShipModeForm(request.POST,  instance = shipmode)
        if form.is_valid():
            form.save()
            messages.success(request, "ShipMode info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_shipmode.html',context)

def delete_shipmode(request,id):
    shipmode = LibraryPacking.objects.get(id = id)
    shipmode.delete()
    return redirect('lib_shipmode')

def edit_qualitylabel(request,id):
    qualitylabel = LibraryQualityLabel.objects.get(id = id)
    form = LibQualityForm(instance=qualitylabel)
    if request.method == 'POST':
        form = LibQualityForm(request.POST,  instance = qualitylabel)
        if form.is_valid():
            form.save()
            messages.success(request, "Quality Label info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_qualitylabel.html',context)

def delete_qualitylabel(request,id):
    qualitylabel = LibraryQualityLabel.objects.get(id = id)
    qualitylabel.delete()
    return redirect('lib_qualitylabel')

def edit_unit(request,id):
    unit = LibraryUnit.objects.get(id = id)
    form = LibUnitForm(instance=unit)
    if request.method == 'POST':
        form = LibUnitForm(request.POST,  instance = unit)
        if form.is_valid():
            form.save()
            messages.success(request, "Order Unit info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_unit.html',context)

def delete_unit(request,id):
    unit = LibraryUnit.objects.get(id = id)
    unit.delete()
    return redirect('lib_unit')

def edit_shipment_term(request, id):
    shipment_term = LibraryShipmentTerm.objects.get(id = id)
    form = LibShipmentTermForm(instance=shipment_term)
    if request.method == 'POST':
        form = LibShipmentTermForm(request.POST,  instance = shipment_term)
        if form.is_valid():
            form.save()
            messages.success(request, "Shipment term info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_shipment_term.html',context)

def delete_shipment_term(request,id):
    shipment_term = LibraryShipmentTerm.objects.get(id = id)
    shipment_term.delete()
    return redirect('lib_shipment_term')

def edit_design_source(request, id):
    design_source = LibraryDesignSource.objects.get(id = id)
    form = LibDesignSourceForm(instance=design_source)
    if request.method == 'POST':
        form = LibDesignSourceForm(request.POST,  instance = design_source)
        if form.is_valid():
            form.save()
            messages.success(request, "Design source info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_design_source.html',context)

def delete_design_source(request,id):
    design_source = LibraryDesignSource.objects.get(id = id)
    design_source.delete()
    return redirect('lib_design_source')

def edit_country(request, id):
    country = LibraryCountry.objects.get(id = id)
    form = LibCountryForm(instance=country)
    if request.method == 'POST':
        form = LibCountryForm(request.POST,  instance = country)
        if form.is_valid():
            form.save()
            messages.success(request, "Country Library info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_country.html',context)

def delete_country(request,id):
    country = LibraryCountry.objects.get(id = id)
    country.delete()
    return redirect('lib_country')
    
def edit_country_type(request, id):
    country_type = LibraryCountryType.objects.get(id = id)
    form = LibCountryTypeForm(instance=country_type)
    if request.method == 'POST':
        form = LibCountryTypeForm(request.POST,  instance = country_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Country Type Library info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_country_type.html',context)

def delete_country_type(request,id):
    country_type = LibraryCountryType.objects.get(id = id)
    country_type.delete()
    return redirect('lib_country_type')

def edit_cut_off(request, id):
    cutoff = LibraryCutOff.objects.get(id = id)
    form = LibCutOffForm(instance=cutoff)
    if request.method == 'POST':
        form = LibCutOffForm(request.POST,  instance = cutoff)
        if form.is_valid():
            form.save()
            messages.success(request, "Cut Off Library info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_cut_off.html',context)

def delete_cut_off(request,id):
    cutoff = LibraryCutOff.objects.get(id = id)
    cutoff.delete()
    return redirect('lib_cut_off')

def edit_product(request, id):
    prods = LibraryProduct.objects.get(id = id)
    form = LibProductForm(instance=prods)
    if request.method == 'POST':
        form = LibProductForm(request.POST,  instance = prods)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Library info has been updated!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_product.html',context)

def delete_product(request,id):
    prods = LibraryProduct.objects.get(id = id)
    prods.delete()
    return redirect('lib_gmt_prod')

def edit_payment_term(request, id):
    payment_term = LibraryPaymentTerm.objects.get(id = id)
    form = LibPaymentTermForm(instance=payment_term)
    if request.method == 'POST':
        form = LibPaymentTermForm(request.POST,  instance = payment_term)
        if form.is_valid():
            form.save()
            messages.success(request, "Payment term info has been updated!")
            return redirect('lib_payment_term')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_payment_term.html',context)

def delete_payment_term(request,id):
    payment_term = LibraryPaymentTerm.objects.get(id = id)
    payment_term.delete()
    return redirect('lib_payment_term')

def edit_fabrication(request, id):
    fabrications = LibraryFabrication.objects.get(id = id)
    form = LibFabricationForm(instance=fabrications)
    if request.method == 'POST':
        form = LibFabricationForm(request.POST,  instance = fabrications)
        if form.is_valid():
            form.save()
            messages.success(request, "Fabrication info has been updated!")
            return redirect('lib_fabrication')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_fabrication.html',context)

def delete_fabrication(request,id):
    fabrications = LibraryFabrication.objects.get(id = id)
    fabrications.delete()
    return redirect('lib_fabrication')

################## ALL Main Forms Views ###############

def order_entry(request):
    job = helper.job_no(OrderEntryInfo.objects.all())
    form = OrderEntryForm(request.POST, request.FILES)
    #for smv
    smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form, extra=1)
    form_smv_items = smv_factory(request.POST)
    po_form = PoDeatilsForm(request.POST, request.FILES)
    items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm, extra=1)
    form_items = items_factory(request.POST, request.FILES)
    
    if request.method == "POST":
        if request.POST.get('_task') == "form":
            if request.method == "GET":
                form = OrderEntryForm()
                smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form, extra=1)
                form_smv_items = smv_factory()
            elif request.method == "POST":
                form = OrderEntryForm(request.POST, request.FILES)
                smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form)
                form_smv_items = smv_factory(request.POST, request.FILES)
                if form.is_valid() and form_smv_items.is_valid():
                    data = form.save()
                    job_no = str('LAK-O' + str(data.id))
                    inserted_by = request.user
                    form.instance.job_no = job_no
                    form.instance.inserted_by = inserted_by
                    job = job_no
                    form.save()
                    form_smv_items.instance = data
                    form_smv_items.save()
                    # messages.success(request, "Your Order Entry information has been recorded!")
                    return HttpResponseRedirect(request.path_info)
                    # return JsonResponse({'error': False})
                else:
                    messages.error(request , "Something went wrong!")
                    print(form.errors)
 
        elif request.POST.get('_task') == 'PO':
            if request.method == "GET":
                po_form = PoDeatilsForm()
                items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm, extra=1)
                form_items = items_factory()
            elif request.method == "POST":
                po_form = PoDeatilsForm(request.POST, request.FILES)
                items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm)
                form_items = items_factory(request.POST, request.FILES)
                if po_form.is_valid() and form_items.is_valid():
                    breakdown = po_form.save()
                    inserted_by = request.user
                    po_form.instance.inserted_by = inserted_by
                    po_form.instance.po_job_no = OrderEntryInfo.objects.get(id=helper.po_no(OrderEntryInfo.objects.filter(inserted_by=inserted_by)))
                    po_form.save()
                    form_items.instance = breakdown
                    form_items.save()
                    messages.success(request, 'Your PO info has been Added Successfully...')
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(po_form.errors)
                    print(form_items.errors)
                    # print(f"data received")
    #for smv
    form = OrderEntryForm(request.POST, request.FILES)
    smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form, extra=1)
    form_smv_items = smv_factory()

    po_form = PoDeatilsForm()
    items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm, extra=1)
    form_items = items_factory()
    
    context = {
        'form': form,
        'po_form': po_form,
        'job': 'LAK-O' + str(job),
        'form_items': form_items,
        'form_smv_items': form_smv_items,
    }
    return render(request, 'Merchandising/Order/order_entry.html', context)

def order_report(request):
    orders = OrderEntryInfo.objects.all().prefetch_related('order_entry').order_by('-id')
    po_details = PO_Details.objects.all().order_by('-id')
    # orders = OrderEntryInfo.objects.all().order_by('-id')
    order_count = orders.count()
    myFilter = OrderFilter(request.GET , queryset = orders)
    orders = myFilter.qs
    context = {
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter,
        'po_details':po_details,
    }
    return render(request, 'Merchandising/Order/order_report.html', context)

def view_order(request, id):
    view_po = PO_Details.objects.get(id=id)
    context = {
        'view_po':view_po,
    }
    return render(request, 'Merchandising/Order/view_order.html', context )

def edit_order(request, id):
    po = PO_Details.objects.get(id=id)
    obj = OrderEntryInfo.objects.get(job_no=po.po_job_no)
    form = OrderEntryForm(instance=obj)
    smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form, extra=0)
    form_smv_items = smv_factory(instance=obj)
    po_form = PoDeatilsForm(instance=po)
    
    if request.method == "POST":
        if request.POST.get('_task') == "form":
            if request.method == "GET":
                obj = OrderEntryInfo.objects.get(job_no=po.po_job_no)
                if obj is None:
                    return redirect(reverse('order_entry'))

                form = OrderEntryForm(instance=obj)
                smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form, extra=0)
                form_smv_items = smv_factory(instance=obj)
            elif request.method == "POST":
                obj = OrderEntryInfo.objects.get(job_no=po.po_job_no)
                if obj is None:
                    return redirect(reverse('order_entry'))
                form = OrderEntryForm(request.POST, request.FILES, instance=obj)
                smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form)
                form_smv_items = smv_factory(request.POST, instance=obj)
                if form.is_valid() and form_smv_items.is_valid():
                    data = form.save()
                    form_smv_items.instance = data
                    form_smv_items.save()
                    messages.success(request, "Your Order Entry information has been updated!")
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(form.errors)
                    print(form_smv_items.errors)
 
        elif request.POST.get('_task') == 'PO':
            if request.method == "GET":
                po = PO_Details.objects.get(id=id)
                if po is None:
                    return redirect(reverse('order_entry'))
                po_form = PoDeatilsForm(instance=po)
                items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm, extra=0)
                form_items = items_factory(instance=po)
            elif request.method == "POST":
                po = PO_Details.objects.get(id=id)
                if po is None:
                    return redirect(reverse('order_entry'))
                po_form = PoDeatilsForm(request.POST, request.FILES, instance=po)
                items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm)
                form_items = items_factory(request.POST, instance=po)
                if po_form.is_valid() and form_items.is_valid():
                    breakdown = po_form.save()
                    form_items.instance = breakdown
                    form_items.save()
                    messages.success(request, 'Your PO info has been updated Successfully...')
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(po_form.errors)
                    print(form_items.errors)
                    # print(f"data received")
    #for smv
    form = OrderEntryForm(instance=obj)
    smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form, extra=0)
    form_smv_items = smv_factory(instance=obj)

    po_form = PoDeatilsForm(instance=po)
    items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm, extra=0)
    form_items = items_factory(instance=po)
    same_po = PO_Details.objects.filter(po_job_no__job_no=obj)
    
    context = {
        'obj':obj,
        'po':po,
        'form': form,
        'po_form': po_form,
        'form_items': form_items,
        'form_smv_items': form_smv_items,
        'same_po': same_po,
    }
    return render(request, "Merchandising/Order/edit_order.html", context)


def delete_order(request, id):
    po = PO_Details.objects.get(id=id)
    po.delete()
    return redirect('order_report')

def pre_costing(request):
    return render(request, 'Merchandising/Order/pre_costing.html')

def shipment_schedule(request):
    orders = OrderEntryInfo.objects.all().prefetch_related('order_entry').order_by('-id')
    myFilter = OrderFilter(request.GET , queryset = orders)
    orders = myFilter.qs
    context = {
        'orders': orders,
        'myFilter': myFilter,
    }
    return render(request, 'Merchandising/Order/shipment_schedule.html', context)

def capacity_booked(request):
    orders = OrderEntryInfo.objects.all().prefetch_related('order_entry').order_by('-id')
    # con_and_pro = PO_Details.objects.values_list( 'po_job_no__buyer_name__buyer_name').annotate(avg_smv=Avg('po_job_no__smv'), tt_qty=(Sum('po_quantity'))).values('po_job_no__company_name__company_name','po_job_no__buyer_name__buyer_name', 'avg_smv', 'tt_qty')
    # con_order = PO_Details.objects.values_list( 'po_job_no__buyer_name__buyer_name').annotate(avg_smv=Avg('po_job_no__smv'), tt_qty=(Sum('po_quantity')), tt_value=(Sum(F('po_quantity')*F('avg_price'), output_field=FloatField()))).values('po_job_no__company_name__company_name','po_job_no__buyer_name__buyer_name', 'avg_smv', 'tt_qty', 'tt_value').filter(order_status="Confirmed")
    # pro_order = PO_Details.objects.values_list( 'po_job_no__buyer_name__buyer_name').annotate(avg_smv=Avg('po_job_no__smv'), tt_qty=(Sum('po_quantity')), tt_value=(Sum(F('po_quantity')*F('avg_price'), output_field=FloatField()))).values('po_job_no__company_name__company_name','po_job_no__buyer_name__buyer_name', 'avg_smv', 'tt_qty', 'tt_value').filter(order_status="Projected")
    
    myFilter = OrderFilter(request.GET , queryset = orders)
    orders = myFilter.qs
    context = {
        'orders': orders,
        'myFilter': myFilter,
        # 'con_and_pro':con_and_pro,
        # 'con_order': con_order,
        # 'pro_order': pro_order,
    }
    return render(request, 'Merchandising/Order/capacity_booked.html', context)

def order_selection(request):
    return render(request, 'Merchandising/Order/order_selection.html')

def work_progress(request, id):
    work_progress = PO_Details.objects.get(id=id)
    
    context={
        'work_progress': work_progress,
    }
    return render(request, 'Merchandising/Order/work_progress.html', context)

def work_progress_report(request):
    orders = OrderEntryInfo.objects.all().prefetch_related('order_entry')
    myFilter = OrderFilter(request.GET , queryset = orders)
    orders = myFilter.qs
    context = {
        'orders': orders,
        'myFilter': myFilter,
    }
    return render(request, 'Merchandising/Order/work_progress_report.html', context)

def tna_progress_report(request, id):
    tna_progress = PO_Details.objects.get(id=id)
    
    context={
        'tna_progress': tna_progress,
    }
    return render(request, 'Merchandising/Order/tna_progress_report.html', context)

def color_size_summary(request):
    
    return render(request, 'Merchandising/Order/color_size_summary.html')

def sample_approval_details(request):
    return render(request, 'Merchandising/Order/sample_approval_details.html')

def lapdip_approval_details(request):
    return render(request, 'Merchandising/Order/lapdip_approval_details.html')

def accessories_approval_details(request):
    return render(request, 'Merchandising/Order/accessories_approval_details.html')

def fabric_booking_details(request):
    return render(request, 'Merchandising/Order/fabric_booking_details.html')

def finish_fabric_details(request):
    return render(request, 'Merchandising/Order/finish_fabric_details.html')

def trims_details(request):
    return render(request, 'Merchandising/Order/trims_details.html')