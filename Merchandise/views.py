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
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def log_tracking(request):

    logs = LogEntry.objects.all()
    
    return render(request, 'Home/log_info.html', {'logs':logs} )

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
    com_address = LibraryCompAddress.objects.all() 
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
    return render(request, 'Merchandising/Library/lib_company_address.html', {'form':form, 'com_address':com_address})

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

############# Budget costing library ####################
def lib_costing_per(request):
    costing_per = LibraryCostingPer.objects.all()

    if request.method == 'POST':
        form = LibCostingPerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library costing per info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibCostingPerForm()
    context ={
        'form':form, 
        'costing_per':costing_per,
    }
    return render(request, 'Merchandising/Library/Budget/lib_costing_per.html', context)

def lib_body_part(request):
    body_part = LibraryBodyPart.objects.all()

    if request.method == 'POST':
        form = LibBodyPartForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library body part info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibBodyPartForm()
    context ={
        'form':form, 
        'body_part':body_part,
    }
    return render(request, 'Merchandising/Library/Budget/lib_body_part.html', context)

def lib_body_part_type(request):
    body_part_type = LibraryBodyPartType.objects.all()

    if request.method == 'POST':
        form = LibBodyPartTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library body part info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibBodyPartTypeForm()
    context ={
        'form':form, 
        'body_part_type':body_part_type,
    }
    return render(request, 'Merchandising/Library/Budget/lib_body_part_type.html', context)

def lib_fab_nature(request):
    fab_nature = LibraryFabNature.objects.all()

    if request.method == 'POST':
        form = LibFabNatureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library fabric nature info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibFabNatureForm()
    context ={
        'form':form, 
        'fab_nature':fab_nature,
    }
    return render(request, 'Merchandising/Library/Budget/lib_fab_nature.html', context)

def lib_color_type(request):
    color_types = LibraryColorType.objects.all()

    if request.method == 'POST':
        form = LibColorTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library color type info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibColorTypeForm()
    context ={
        'form':form, 
        'color_types':color_types,
    }
    return render(request, 'Merchandising/Library/Budget/lib_color_type.html', context)

def lib_fabric_source(request):
    fabric_sources = LibraryFabricSource.objects.all()

    if request.method == 'POST':
        form = LibFabricSourceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library fabric source info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibFabricSourceForm()
    context ={
        'form':form, 
        'fabric_sources':fabric_sources,
    }
    return render(request, 'Merchandising/Library/Budget/lib_fabric_source.html', context)

def lib_fabric_description(request):
    fabric_desc = LibraryFabricDescription.objects.all()

    if request.method == 'POST':
        form = LibFabricDescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library fabric description info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibFabricDescriptionForm()
    context ={
        'form':form, 
        'fabric_desc':fabric_desc,
    }
    return render(request, 'Merchandising/Library/Budget/lib_fabric_description.html', context)

def lib_nominated_supp(request):
    nominated_sup = LibraryNominatedSupp.objects.all()

    if request.method == 'POST':
        form = LibNominatedSuppForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library nominated supplier info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibNominatedSuppForm()
    context ={
        'form':form, 
        'nominated_sup':nominated_sup,
    }
    return render(request, 'Merchandising/Library/Budget/lib_nominated_supp.html', context)

def lib_dia_types(request):
    dia_types = LibraryDiaTypes.objects.all()

    if request.method == 'POST':
        form = LibDiaTypesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library width/dia types info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibDiaTypesForm()
    context ={
        'form':form, 
        'dia_types':dia_types,
    }
    return render(request, 'Merchandising/Library/Budget/lib_dia_types.html', context)

def lib_consumption_basis(request):
    cons_basis = LibraryConsumptionBasis.objects.all()

    if request.method == 'POST':
        form = LibConsumptionBasisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library consumption basis info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibConsumptionBasisForm()
    context ={
        'form':form, 
        'cons_basis':cons_basis,
    }
    return render(request, 'Merchandising/Library/Budget/lib_consumption_basis.html', context)

def lib_color_size_sensitive(request):
    cs_sensitive = LibraryColorSizeSensitive.objects.all()

    if request.method == 'POST':
        form = LibColorSizeSensitiveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library color size sensitive info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibColorSizeSensitiveForm()
    context ={
        'form':form, 
        'cs_sensitive':cs_sensitive,
    }
    return render(request, 'Merchandising/Library/Budget/lib_color_size_sensitive.html', context)

############ Yarn Library Views ############
def lib_yarn_type(request):
    yarn_type = LibraryYarnType.objects.all()

    if request.method == 'POST':
        form = LibYarnTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library yarn type info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibYarnTypeForm()
    context ={
        'form':form, 
        'yarn_type':yarn_type,
    }
    return render(request, 'Merchandising/Library/Budget/lib_yarn_type.html', context)

def lib_yarn_supplier(request):
    yarn_supplier = LibraryYarnSupplier.objects.all()

    if request.method == 'POST':
        form = LibYarnSupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library yarn supplier info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibYarnSupplierForm()
    context ={
        'form':form, 
        'yarn_supplier':yarn_supplier,
    }
    return render(request, 'Merchandising/Library/Budget/lib_yarn_supplier.html', context)

############ Convertion Library Views ############
def lib_process(request):
    process = LibraryProcess.objects.all()

    if request.method == 'POST':
        form = LibProcessForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library process info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibProcessForm()
    context ={
        'form':form, 
        'process':process,
    }
    return render(request, 'Merchandising/Library/Budget/lib_process.html', context)

def lib_knitting(request):
    # FOR Dollaer Rate
    field_name = 'usd_rate'
    obj = LibraryDoller.objects.first()
    field_object = LibraryDoller._meta.get_field(field_name)
    usd_price = field_object.value_from_object(obj)
    knitting_item = LibraryKnitting.objects.all()

    if request.method == 'POST':
        form = LibKnittingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library knitting info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibKnittingForm()
    context ={
        'form':form, 
        'knitting_item':knitting_item,
        'usd_price':usd_price,
    }
    return render(request, 'Merchandising/Library/Budget/lib_knitting.html', context)

def lib_dyeing(request):
    # FOR Dollaer Rate
    field_name = 'usd_rate'
    obj = LibraryDoller.objects.first()
    field_object = LibraryDoller._meta.get_field(field_name)
    usd_price = field_object.value_from_object(obj)
    dyeing_item = LibraryDyeing.objects.all()

    if request.method == 'POST':
        form = LibDyeingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library dyeing info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibDyeingForm()
    context ={
        'form':form, 
        'dyeing_item':dyeing_item,
        'usd_price': usd_price,
    }
    return render(request, 'Merchandising/Library/Budget/lib_dyeing.html', context)

############ Trim Library Views ############
def lib_groups_item(request):
    groups = LibraryGroupsItem.objects.all()

    if request.method == 'POST':
        form = LibGroupsItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library groups info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibGroupsItemForm()
    context ={
        'form':form, 
        'groups':groups,
    }
    return render(request, 'Merchandising/Library/Budget/lib_groups_item.html', context)

def lib_trim_source(request):
    sources = LibraryTrimSource.objects.all()

    if request.method == 'POST':
        form = LibTrimSourceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library source info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibTrimSourceForm()
    context ={
        'form':form, 
        'sources':sources,
    }
    return render(request, 'Merchandising/Library/Budget/lib_trim_source.html', context)

############ Embellishment Cost Library Views ############
def lib_emblcost_name(request):
    names = LibraryEmbCostName.objects.all()

    if request.method == 'POST':
        form = LibEmbCostNameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library embellishment cost name info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibEmbCostNameForm()
    context ={
        'form':form, 
        'names':names,
    }
    return render(request, 'Merchandising/Library/Budget/lib_emblcost_name.html', context)

def lib_emblcost_type(request):
    types = LibraryEmbCostType.objects.all()

    if request.method == 'POST':
        form = LibyEmbCostTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library embellishment cost type info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibyEmbCostTypeForm()
    context ={
        'form':form, 
        'types':types,
    }
    return render(request, 'Merchandising/Library/Budget/lib_emblcost_type.html', context)

############ Wash Cost Library Views ############
def lib_washcost_name(request):
    w_names = LibraryWash_CostName.objects.all()

    if request.method == 'POST':
        form = LibWashCost_NameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library wash cost name info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibWashCost_NameForm()
    context ={
        'form':form, 
        'w_names':w_names,
    }
    return render(request, 'Merchandising/Library/Budget/lib_washcost_name.html', context)

def lib_washcost_type(request):
    w_types = LibraryWash_CostType.objects.all()

    if request.method == 'POST':
        form = LibywashCost_TypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your library wash cost type info has been recorded!")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request , "Something went wrong!")
            print(form.errors)
    form = LibywashCost_TypeForm()
    context ={
        'form':form, 
        'w_types':w_types,
    }
    return render(request, 'Merchandising/Library/Budget/lib_washcost_type.html', context)
########### EDIT ALL LIBRARY FORMS ##########
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

def edit_companyAddress(request,id):
    cmpadd = LibraryCompAddress.objects.get(id = id)
    form = LibCompAddressForm(instance=cmpadd)
    if request.method == 'POST':
        form = LibCompAddressForm(request.POST,  instance = cmpadd)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Company Address info has been updated!")
            return redirect('lib_company_address')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Edit_Library/edit_compAddress.html',context)

def delete_compAddress(request,id):
    cmpadd = LibraryCompAddress.objects.get(id = id)
    cmpadd.delete()
    return redirect('lib_company_address')

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

############# Budget Edit libarary views ###############
def edit_costing_per(request, id):
    costing_per = LibraryCostingPer.objects.get(id = id)
    form = LibCostingPerForm(instance=costing_per)
    if request.method == 'POST':
        form = LibCostingPerForm(request.POST,  instance = costing_per)
        if form.is_valid():
            form.save()
            messages.success(request, "Costing Per info has been updated!")
            return redirect('lib_costing_per')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_costing_per.html',context)

def delete_costing_per(request,id):
    costing_per = LibraryCostingPer.objects.get(id = id)
    costing_per.delete()
    return redirect('lib_costing_per')

def edit_body_part(request, id):
    body_part = LibraryBodyPart.objects.get(id = id)
    form = LibBodyPartForm(instance=body_part)
    if request.method == 'POST':
        form = LibBodyPartForm(request.POST,  instance = body_part)
        if form.is_valid():
            form.save()
            messages.success(request, "body part info has been updated!")
            return redirect('lib_body_part')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_body_part.html',context)

def delete_body_part(request,id):
    body_part = LibraryBodyPart.objects.get(id = id)
    body_part.delete()
    return redirect('lib_body_part')

def edit_body_part_type(request, id):
    body_part_type = LibraryBodyPartType.objects.get(id = id)
    form = LibBodyPartTypeForm(instance=body_part_type)
    if request.method == 'POST':
        form = LibBodyPartTypeForm(request.POST,  instance = body_part_type)
        if form.is_valid():
            form.save()
            messages.success(request, "body part Type info has been updated!")
            return redirect('lib_body_part_type')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_body_part_type.html',context)

def delete_body_part_type(request,id):
    body_part_type = LibraryBodyPartType.objects.get(id = id)
    body_part_type.delete()
    return redirect('lib_body_part_type')

def edit_fab_nature(request, id):
    fab_nature = LibraryFabNature.objects.get(id = id)
    form = LibFabNatureForm(instance=fab_nature)
    if request.method == 'POST':
        form = LibFabNatureForm(request.POST,  instance = fab_nature)
        if form.is_valid():
            form.save()
            messages.success(request, "Fabric nature info has been updated!")
            return redirect('lib_fab_nature')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_fab_nature.html',context)

def delete_fab_nature(request,id):
    fab_nature = LibraryFabNature.objects.get(id = id)
    fab_nature.delete()
    return redirect('lib_fab_nature')

def edit_color_type(request, id):
    color_types = LibraryColorType.objects.get(id = id)
    form = LibColorTypeForm(instance=color_types)
    if request.method == 'POST':
        form = LibColorTypeForm(request.POST,  instance = color_types)
        if form.is_valid():
            form.save()
            messages.success(request, "Color Types info has been updated!")
            return redirect('lib_color_type')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_color_type.html',context)

def delete_color_type(request,id):
    color_types = LibraryColorType.objects.get(id = id)
    color_types.delete()
    return redirect('lib_color_type')

def edit_fabric_source(request, id):
    fabric_sources = LibraryFabricSource.objects.get(id = id)
    form = LibFabricSourceForm(instance=fabric_sources)
    if request.method == 'POST':
        form = LibFabricSourceForm(request.POST,  instance = fabric_sources)
        if form.is_valid():
            form.save()
            messages.success(request, "Fabric source info has been updated!")
            return redirect('lib_fabric_source')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_fabric_source.html',context)

def delete_fabric_source(request,id):
    fabric_sources = LibraryFabricSource.objects.get(id = id)
    fabric_sources.delete()
    return redirect('lib_fabric_source')

def edit_fabric_description(request, id):
    fabric_desc = LibraryFabricDescription.objects.get(id = id)
    form = LibFabricDescriptionForm(instance=fabric_desc)
    if request.method == 'POST':
        form = LibFabricDescriptionForm(request.POST,  instance = fabric_desc)
        if form.is_valid():
            form.save()
            messages.success(request, "Fabric description info has been updated!")
            return redirect('lib_fabric_description')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_fabric_description.html',context)

def delete_fabric_description(request,id):
    fabric_desc = LibraryFabricDescription.objects.get(id = id)
    fabric_desc.delete()
    return redirect('lib_fabric_description')

def edit_nominated_supp(request, id):
    nominated_sup = LibraryNominatedSupp.objects.get(id = id)
    form = LibNominatedSuppForm(instance=nominated_sup)
    if request.method == 'POST':
        form = LibNominatedSuppForm(request.POST,  instance = nominated_sup)
        if form.is_valid():
            form.save()
            messages.success(request, "Nominated supplier info has been updated!")
            return redirect('lib_nominated_supp')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_nominated_supp.html',context)

def delete_nominated_supp(request,id):
    nominated_sup = LibraryNominatedSupp.objects.get(id = id)
    nominated_sup.delete()
    return redirect('lib_nominated_supp')

def edit_dia_types(request, id):
    dia_types = LibraryDiaTypes.objects.get(id = id)
    form = LibDiaTypesForm(instance=dia_types)
    if request.method == 'POST':
        form = LibDiaTypesForm(request.POST,  instance = dia_types)
        if form.is_valid():
            form.save()
            messages.success(request, "Width/Dia types info has been updated!")
            return redirect('lib_dia_types')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_dia_types.html',context)

def delete_dia_types(request,id):
    dia_types = LibraryDiaTypes.objects.get(id = id)
    dia_types.delete()
    return redirect('lib_dia_types')

def edit_consumption_basis(request, id):
    cons_basis = LibraryConsumptionBasis.objects.get(id = id)
    form = LibConsumptionBasisForm(instance=cons_basis)
    if request.method == 'POST':
        form = LibConsumptionBasisForm(request.POST,  instance = cons_basis)
        if form.is_valid():
            form.save()
            messages.success(request, "Consumption basis info has been updated!")
            return redirect('lib_consumption_basis')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_consumption_basis.html',context)

def delete_consumption_basis(request,id):
    cons_basis = LibraryConsumptionBasis.objects.get(id = id)
    cons_basis.delete()
    return redirect('lib_consumption_basis')

def edit_color_size_sensitive(request, id):
    cs_sensitive = LibraryColorSizeSensitive.objects.get(id = id)
    form = LibColorSizeSensitiveForm(instance=cs_sensitive)
    if request.method == 'POST':
        form = LibColorSizeSensitiveForm(request.POST,  instance = cs_sensitive)
        if form.is_valid():
            form.save()
            messages.success(request, " Color size sensitive info has been updated!")
            return redirect('lib_color_size_sensitive')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_color_size_sensitive.html',context)

def delete_color_size_sensitive(request,id):
    cs_sensitive = LibraryColorSizeSensitive.objects.get(id = id)
    cs_sensitive.delete()
    return redirect('lib_color_size_sensitive')

########## Yarn cost edit view ########
def edit_yarn_type(request, id):
    yarn_type = LibraryYarnType.objects.get(id = id)
    form = LibYarnTypeForm(instance=yarn_type)
    if request.method == 'POST':
        form = LibYarnTypeForm(request.POST,  instance = yarn_type)
        if form.is_valid():
            form.save()
            messages.success(request, " Yarn type info has been updated!")
            return redirect('lib_yarn_type')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_yarn_type.html',context)

def delete_yarn_type(request,id):
    yarn_type = LibraryYarnType.objects.get(id = id)
    yarn_type.delete()
    return redirect('lib_yarn_type')

def edit_yarn_supplier(request, id):
    yarn_supplier = LibraryYarnSupplier.objects.get(id = id)
    form = LibYarnSupplierForm(instance=yarn_supplier)
    if request.method == 'POST':
        form = LibYarnSupplierForm(request.POST,  instance = yarn_supplier)
        if form.is_valid():
            form.save()
            messages.success(request, " Yarn supplier info has been updated!")
            return redirect('lib_yarn_supplier')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_yarn_supplier.html',context)

def delete_yarn_supplier(request,id):
    yarn_supplier = LibraryYarnSupplier.objects.get(id = id)
    yarn_supplier.delete()
    return redirect('lib_yarn_supplier')

##### Conversion cost lib edit view #####
def edit_process(request, id):
    process = LibraryProcess.objects.get(id = id)
    form = LibProcessForm(instance=process)
    if request.method == 'POST':
        form = LibProcessForm(request.POST,  instance = process)
        if form.is_valid():
            form.save()
            messages.success(request, " Process info has been updated!")
            return redirect('lib_process')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_process.html',context)

def delete_process(request,id):
    process = LibraryProcess.objects.get(id = id)
    process.delete()
    return redirect('lib_process')

def edit_knitting(request, id):
    # FOR Dollaer Rate
    field_name = 'usd_rate'
    obj = LibraryDoller.objects.first()
    field_object = LibraryDoller._meta.get_field(field_name)
    usd_price = field_object.value_from_object(obj)

    knitting_item = LibraryKnitting.objects.get(id = id)
    form = LibKnittingForm(instance=knitting_item)
    if request.method == 'POST':
        form = LibKnittingForm(request.POST,  instance = knitting_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Knitting info has been updated!")
            return redirect('lib_knitting')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form, 'usd_price':usd_price}
    return render(request, 'Merchandising/Library/Budget/edit_knitting.html',context)

def delete_knitting(request,id):
    knitting_item = LibraryKnitting.objects.get(id = id)
    knitting_item.delete()
    return redirect('lib_knitting')

def edit_dyeing(request, id):
    # FOR Dollaer Rate
    field_name = 'usd_rate'
    obj = LibraryDoller.objects.first()
    field_object = LibraryDoller._meta.get_field(field_name)
    usd_price = field_object.value_from_object(obj)
    dyeing_item = LibraryDyeing.objects.get(id = id)
    form = LibDyeingForm(instance=dyeing_item)
    if request.method == 'POST':
        form = LibDyeingForm(request.POST,  instance = dyeing_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Dyeing info has been updated!")
            return redirect('lib_dyeing')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form, 'usd_price':usd_price}
    return render(request, 'Merchandising/Library/Budget/edit_dyeing.html',context)

def delete_dyeing(request,id):
    dyeing_item = LibraryDyeing.objects.get(id = id)
    dyeing_item.delete()
    return redirect('lib_dyeing')

######### Trim cost edit views ##############
def edit_groups_item(request, id):
    groups = LibraryGroupsItem.objects.get(id = id)
    form = LibGroupsItemForm(instance=groups)
    if request.method == 'POST':
        form = LibGroupsItemForm(request.POST,  instance = groups)
        if form.is_valid():
            form.save()
            messages.success(request, "Groups info has been updated!")
            return redirect('lib_groups_item')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_groups_item.html',context)

def delete_groups_item(request,id):
    groups = LibraryGroupsItem.objects.get(id = id)
    groups.delete()
    return redirect('lib_groups_item')

def edit_trim_source(request, id):
    sources = LibraryTrimSource.objects.get(id = id)
    form = LibTrimSourceForm(instance=sources)
    if request.method == 'POST':
        form = LibTrimSourceForm(request.POST,  instance = sources)
        if form.is_valid():
            form.save()
            messages.success(request, "Source info has been updated!")
            return redirect('lib_trim_source')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_trim_source.html',context)

def delete_trim_source(request,id):
    sources = LibraryTrimSource.objects.get(id = id)
    sources.delete()
    return redirect('lib_trim_source')

######### Embellishment cost edit views ##############
def edit_emblcost_name(request, id):
    names = LibraryEmbCostName.objects.get(id = id)
    form = LibEmbCostNameForm(instance=names)
    if request.method == 'POST':
        form = LibEmbCostNameForm(request.POST,  instance = names)
        if form.is_valid():
            form.save()
            messages.success(request, "Embellishment cost name info has been updated!")
            return redirect('lib_emblcost_name')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_emblcost_name.html',context)

def delete_emblcost_name(request,id):
    names = LibraryEmbCostName.objects.get(id = id)
    names.delete()
    return redirect('lib_emblcost_name')

def edit_emblcost_type(request, id):
    types = LibraryEmbCostType.objects.get(id = id)
    form = LibyEmbCostTypeForm(instance=types)
    if request.method == 'POST':
        form = LibyEmbCostTypeForm(request.POST,  instance = types)
        if form.is_valid():
            form.save()
            messages.success(request, "Embellishment cost type info has been updated!")
            return redirect('lib_emblcost_type')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_emblcost_type.html',context)

def delete_emblcost_type(request,id):
    types = LibraryEmbCostType.objects.get(id = id)
    types.delete()
    return redirect('lib_emblcost_type')    

######### Embellishment cost edit views ##############
def edit_washcost_name(request, id):
    w_names = LibraryWash_CostName.objects.get(id = id)
    form = LibWashCost_NameForm(instance=w_names)
    if request.method == 'POST':
        form = LibWashCost_NameForm(request.POST,  instance = w_names)
        if form.is_valid():
            form.save()
            messages.success(request, "Wash cost name info has been updated!")
            return redirect('lib_washcost_name')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_washcost_name.html',context)

def delete_washcost_name(request,id):
    w_names = LibraryWash_CostName.objects.get(id = id)
    w_names.delete()
    return redirect('lib_washcost_name')

def edit_washcost_type(request, id):
    w_types = LibraryWash_CostType.objects.get(id = id)
    form = LibywashCost_TypeForm(instance=w_types)
    if request.method == 'POST':
        form = LibywashCost_TypeForm(request.POST,  instance = w_types)
        if form.is_valid():
            form.save()
            messages.success(request, "Wash cost type info has been updated!")
            return redirect('lib_washcost_type')
        else:
            messages.error("Something went wrong!")
            print(form.errors)
    context = {'form':form}
    return render(request, 'Merchandising/Library/Budget/edit_washcost_type.html',context)

def delete_washcost_type(request,id):
    w_types = LibraryWash_CostType.objects.get(id = id)
    w_types.delete()
    return redirect('lib_washcost_type')
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
    try:
        po_details = PO_Details.objects.filter(pub_shipment_date__year=request.GET.get('year'), pub_shipment_date__month=request.GET.get('month')).order_by('-id')
        year = request.GET.get('year')
    except:
        po_details = PO_Details.objects.all().order_by('-id')
        year = 'year'
    orders = OrderEntryInfo.objects.all().order_by('-id')
    order_count = orders.count()
    myFilter = POFilter(request.GET , queryset = po_details)
    po_details = myFilter.qs
    context = {
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter,
        'po_details':po_details,
        'year': year,
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
        'count': len(ColorSizeItems.objects.filter(po_color_size=id)),
        'same_po': same_po,
    }
    return render(request, "Merchandising/Order/edit_order.html", context)



def add_po_report(request):
    orders = OrderEntryInfo.objects.all().order_by('-id')
    
    myFilter = PO_OrderFilter(request.GET , queryset = orders)
    orders = myFilter.qs
    context = {
        'orders': orders,
        'myFilter': myFilter,
    }
    return render(request, 'Merchandising/Order/add_po_report.html', context)

def add_po(request, id):
    obj = OrderEntryInfo.objects.get(id=id)
    form = OrderEntryForm(instance=obj)
    smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form, extra=0)
    form_smv_items = smv_factory(instance=obj)
    po_form = AddPoDeatilsForm()
    
    if request.method == "POST":
        if request.POST.get('_task') == "form":
            if request.method == "GET":
                obj = OrderEntryInfo.objects.get(id=id)
                if obj is None:
                    return redirect(reverse('order_entry'))

                form = OrderEntryForm(instance=obj)
                smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form, extra=0)
                form_smv_items = smv_factory(instance=obj)
            elif request.method == "POST":
                obj = OrderEntryInfo.objects.get(id=id)
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
                po_form = AddPoDeatilsForm()
                items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm, extra=1)
                form_items = items_factory()
            elif request.method == "POST":
                po_form = AddPoDeatilsForm(request.POST, request.FILES)
                items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm)
                form_items = items_factory(request.POST, request.FILES)
                if po_form.is_valid() and form_items.is_valid():
                    breakdown = po_form.save()
                    inserted_by = request.user
                    po_form.instance.inserted_by = inserted_by
                    po_form.save()
                    form_items.instance = breakdown
                    form_items.save()
                    messages.success(request, 'Your PO info has been Added Successfully...')
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(po_form.errors)
                    print(form_items.errors)
    #for smv
    form = OrderEntryForm(instance=obj)
    smv_factory = inlineformset_factory(OrderEntryInfo, SmvItems, form=SmvItems_Form, extra=0)
    form_smv_items = smv_factory(instance=obj)

    po_form = AddPoDeatilsForm()
    items_factory = inlineformset_factory(PO_Details, ColorSizeItems, form=colorsize_ItemsForm, extra=1)
    form_items = items_factory()
    same_po = PO_Details.objects.filter(po_job_no__job_no=obj.job_no)
    
    context = {
        'obj':obj,
        'form': form,
        'po_form': po_form,
        'form_items': form_items,
        'form_smv_items': form_smv_items,
        'same_po': same_po,
    }
    return render(request, "Merchandising/Order/add_po.html", context)

def delete_order(request, id):
    po = PO_Details.objects.get(id=id)
    po.delete()
    return redirect('order_report')

####### Budget Pre Costing Form ##########
def pre_costing(request):
    fab_desc = LibraryFabricDescription.objects.all()
    knitting_item = LibraryKnitting.objects.all()
    dyeing_item = LibraryDyeing.objects.all()
    groups = LibraryGroupsItem.objects.all()
    country = LibraryCountry.objects.all()
    nom_supp = LibraryNominatedSupp.objects.all()
    types = LibraryEmbCostType.objects.all()
    w_types = LibraryWash_CostType.objects.all()

    # FOR BUDGET - PIECE QUANTITY 
    field_name = 'pcs_amount'
    obj = LibraryPcsQty.objects.first()
    field_object = LibraryPcsQty._meta.get_field(field_name)
    pcs = field_object.value_from_object(obj)
    
    body_parts = LibraryBodyPart.objects.all()
    form = BudgetPreCostForm(request.POST, request.FILES)
    fab_form = FabricCostForm()
    fc_factory = inlineformset_factory(FabricCost, Fabric_Inline_Item, form=FabricItemForm, extra=1)
    form_items_fc = fc_factory()

    yarn_form = YarnCostForm()
    yc_factory = inlineformset_factory(YarnCost, Yarn_Inline_Item, form=YarnItemForm, extra=1)
    form_items_yc = yc_factory()
    
    con_form = ConversionCostForm()
    cc_factory = inlineformset_factory(ConversionCost, Conversion_Inline, form=ConversionItemForm, extra=1)
    form_items_cc = cc_factory()

    trim_form = TrimCostForm()
    tc_factory = inlineformset_factory(TrimCost, TrimCostItems, form=TrimItemsForm, extra=1)
    trim_form_item = tc_factory()

    embl_form = EmbellishmentCostForm()
    ec_factory = inlineformset_factory(EmbellishmentCost, EmbellishmentCostItem, form=EmbellishmentItemsForm, extra=1)
    embl_form_item = ec_factory()
    
    wash_form = WashCostForm()
    wac_factory = inlineformset_factory(WashCost, WashCost_Items, form=WashCostItemsForm, extra=1)
    wash_form_item = wac_factory()

    if request.method == 'POST':
        if request.POST.get('_task') == "cost_form": #For budget cost form
            form = BudgetPreCostForm(request.POST)
            if form.is_valid():
                form.save()
                inserted_by = request.user
                form.instance.job_no = OrderEntryInfo.objects.get(id=int(request.POST.get('job_no')[5:]))
                form.instance.job_qty = request.POST.get('job_qty')
                form.instance.inserted_by = inserted_by
                form.save()
                # messages.success(request, "Your budget costing info has been recorded!")
                return HttpResponseRedirect(request.path_info)
            else:
                messages.error(request , "Something went wrong!")
                print(form.errors)
        
        elif request.POST.get('_task') == "f_form":
            if request.method == "GET":
                fab_form = FabricCostForm()
                fc_factory = inlineformset_factory(FabricCost, Fabric_Inline_Item, form=FabricItemForm, extra=1)
                form_items_fc = fc_factory()
           
            elif request.method == "POST":
                fab_form = FabricCostForm(request.POST, request.FILES)
                fc_factory = inlineformset_factory(FabricCost, Fabric_Inline_Item, form=FabricItemForm)
                form_items_fc = fc_factory(request.POST)
                if fab_form.is_valid() and form_items_fc.is_valid():
                    data = fab_form.save()
                    inserted_by = request.user
                    fab_form.instance.inserted_by = inserted_by
                    fab_form.instance.b_job_no = BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=inserted_by)))
                    fab_form.save()
                    form_items_fc.instance = data
                    form_items_fc.save()
                    helper.coustom_inline(
                        Grey_Cons.objects.filter(inserted_by=request.user).order_by('-id')[:int(request.POST.get("inline_count"))],
                        Fabric_Inline_Item.objects.filter(fabric_cost=helper.job_no(FabricCost.objects.filter(inserted_by=request.user))).order_by('-id')[:int(request.POST.get("inline_count"))],
                        int(request.POST.get("inline_count"))
                    )
                    # messages.success(request, 'Your fabric cost info has been Added Successfully...')
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(form_items_fc.errors)

        elif request.POST.get('_task') == "y_form": #for yarn cost form
            if request.method == "GET":
                yarn_form = YarnCostForm()
                yc_factory = inlineformset_factory(YarnCost, Yarn_Inline_Item, form=YarnItemForm, extra=1)
                form_items_yc = yc_factory()
           
            elif request.method == "POST":
                yarn_form = YarnCostForm(request.POST, request.FILES)
                yc_factory = inlineformset_factory(YarnCost, Yarn_Inline_Item, form=YarnItemForm)
                form_items_yc = yc_factory(request.POST)
                if yarn_form.is_valid() and form_items_yc.is_valid():
                    data = yarn_form.save()
                    inserted_by = request.user
                    yarn_form.instance.inserted_by = inserted_by
                    yarn_form.instance.b_job_no = BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=inserted_by)))
                    yarn_form.save()
                    form_items_yc.instance = data
                    form_items_yc.save()
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(form_items_yc.errors)
        
        elif request.POST.get("_task") == 'grey_data': # for avg. grey comsumption form
            grey_cons_model = Grey_Cons(b_job_no=BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=request.user))),
            inserted_by=request.user
            )
            grey_cons_model.save()
            for i in range(0, len(helper.color_size(OrderEntryInfo.objects.get(id=int(request.POST.get('__po_job')[5:]))))):
                data = Grey_Cons_Items(
                    color_size=ColorSizeItems.objects.get(id=request.POST.get(f'id_{i+1}')),
                    grey_cons = grey_cons_model,
                    dia = request.POST.get(f"dia_{i+1}"),
                    item_sizes = request.POST.get(f"item_{i+1}"),
                    fab_cons =  request.POST.get(f"fin_cons_{i+1}"),
                    process_loss_pct = request.POST.get(f"pro_{i+1}"),
                    grey_cons_unit =  request.POST.get(f"unit_{i+1}"),
                    rate = request.POST.get(f"rate_{i+1}"),
                    amount = request.POST.get(f"amt_{i+1}"),
                    pcs = request.POST.get(f"pcs_{i+1}"),
                    total_qty = request.POST.get(f"tt_qty_{i+1}"),
                    total_amount = request.POST.get(f"tt_amt_{i+1}"),
                    remarks =  request.POST.get(f"remarks_{i+1}")
                )
                data.save()
        
        elif request.POST.get("_task") == 'cont_color': #for color contrast form
            color_con_model = ColorContrast(b_job_no=BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=request.user))),
            inserted_by=request.user
            )
            color_con_model.save()
            for i in range(0, len(helper.gmts_item(OrderEntryInfo.objects.get(id=int(request.POST.get('__po_job')[5:])), 'color'))):
                data = ColorContrastItems(
                    color_contrast = color_con_model,
                    gmts_color = request.POST.get(f"gmts_color_{i+1}"),
                    contrast_color = request.POST.get(f"contrast_color_{i+1}")
                    
                )
                data.save()
         
        elif request.POST.get("_task") == 'dyeing_color':  # For dyeing pop up form
            dyeing_color_model = DyeingColor(b_job_no=BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=request.user))),
            inserted_by=request.user
            )
            dyeing_color_model.save()
            for i in range(0, len(helper.color_size(OrderEntryInfo.objects.get(id=int(request.POST.get('__po_job')[5:]))))):
                data = DyeingColorItems(
                    dyeing_color = dyeing_color_model,
                    gmts_color = request.POST.get(f"gmts_color_{i+1}"),
                    fabric_color = request.POST.get(f"fabric_color_{i+1}"),
                    cons_rate = request.POST.get(f"cons_rate_{i+1}"),
                    charge_unit = request.POST.get(f"charge_unit_{i+1}")
                    
                )
                data.save()
        elif request.POST.get('_task') == "con_form":          #For conversion cost
            if request.method == "GET":
                con_form = ConversionCostForm()
                cc_factory = inlineformset_factory(ConversionCost, Conversion_Inline, form=ConversionItemForm, extra=1)
                form_items_cc = cc_factory()
           
            elif request.method == "POST":
                con_form = ConversionCostForm(request.POST, request.FILES)
                cc_factory = inlineformset_factory(ConversionCost, Conversion_Inline, form=ConversionItemForm)
                form_items_cc = cc_factory(request.POST)
                if con_form.is_valid() and form_items_cc.is_valid():
                    data = con_form.save()
                    inserted_by = request.user
                    con_form.instance.b_job_no = BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=inserted_by)))
                    con_form.instance.inserted_by = inserted_by
                    con_form.save()
                    form_items_cc.instance = data
                    form_items_cc.save()
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(form_items_cc.errors)

        elif request.POST.get("_task") == 'cl_data':  # For Care Lebel form
            care_lebel_model = Care_Level(b_job_no=BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=request.user))),
            inserted_by=request.user,
            tt_cons = request.POST.get("tt_cons"),
            tt_ex_pct = request.POST.get("tt_ex_pct"),
            grand_tt_cons = request.POST.get("grand_tt_cons"),
            tt_rate = request.POST.get("tt_rate"),
            sub_tt_amount = request.POST.get("sub_tt_amount"),
            tt_qty_dzn = request.POST.get("tt_qty_dzn"),
            grand_tt_amount = request.POST.get("grand_tt_amount"),
            tt_pcs = request.POST.get("tt_pcs"),
            avg_tt_cons = request.POST.get("avg_tt_cons"),
            avg_ex_pct = request.POST.get("avg_ex_pct"),
            avg_grand_tt_cons = request.POST.get("avg_grand_tt_cons"),
            avg_tt_rate = request.POST.get("avg_tt_rate"),
            avg_sub_tt_amount = request.POST.get("avg_sub_tt_amount"),
            avg_tt_qty_dzn = request.POST.get("avg_tt_qty_dzn"),
            avg_grand_tt_amount = request.POST.get("avg_grand_tt_amount"),
            avg_tt_pcs = request.POST.get("avg_tt_pcs"),
            )
            care_lebel_model.save()
            for i in range(0, len(helper.color_size(OrderEntryInfo.objects.get(id=int(request.POST.get('__po_job')[5:]))))):
                data = Care_level_Items(
                    color_size=ColorSizeItems.objects.get(id=request.POST.get(f'id_{i+1}')),
                    care_level = care_lebel_model,
                    po_no = request.POST.get(f"po_no_{i+1}"),
                    gmts_item = request.POST.get(f"gmts_item_{i+1}"),
                    country = request.POST.get(f"country_{i+1}"),
                    color = request.POST.get(f"color_{i+1}"),
                    gmts_size = request.POST.get(f"gmts_size_{i+1}"),
                    item_color = request.POST.get(f"item_color_{i+1}"),
                    item_sizes = request.POST.get(f"item_sizes_{i+1}"),
                    cons = request.POST.get(f"cons_{i+1}"),
                    ex_pct = request.POST.get(f"ex_pct_{i+1}"),
                    tt_cons = request.POST.get(f"tt_cons_{i+1}"),
                    rate = request.POST.get(f"rate_{i+1}"),
                    amount = request.POST.get(f"amount_{i+1}"),
                    tt_qty = request.POST.get(f"tt_qty_{i+1}"),
                    tt_amount = request.POST.get(f"tt_amount_{i+1}"),
                    placement = request.POST.get(f"placement_{i+1}"),
                    pcs = request.POST.get(f"pcs_{i+1}"),
                    
                )
                data.save()

        elif request.POST.get('_task') == "trim_form":          #For Trim cost
            if request.method == "GET":
                trim_form = TrimCostForm()
                tc_factory = inlineformset_factory(TrimCost, TrimCostItems, form=TrimItemsForm, extra=1)
                trim_form_item = tc_factory()
           
            elif request.method == "POST":
                trim_form = TrimCostForm(request.POST, request.FILES)
                tc_factory = inlineformset_factory(TrimCost, TrimCostItems, form=TrimItemsForm)
                trim_form_item = tc_factory(request.POST, request.FILES)
                if trim_form.is_valid() and trim_form_item.is_valid():
                    data = trim_form.save()
                    inserted_by = request.user
                    trim_form.instance.b_job_no = BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=inserted_by)))
                    trim_form.instance.inserted_by = inserted_by
                    trim_form.save()
                    trim_form_item.instance = data
                    trim_form_item.save()
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(trim_form_item.errors)

        elif request.POST.get('_task') == "embl_form":          #For Embellishment cost
            if request.method == "GET":
                embl_form = EmbellishmentCostForm()
                ec_factory = inlineformset_factory(EmbellishmentCost, EmbellishmentCostItem, form=EmbellishmentItemsForm, extra=1)
                embl_form_item = ec_factory()
           
            elif request.method == "POST":
                embl_form = EmbellishmentCostForm(request.POST, request.FILES)
                ec_factory = inlineformset_factory(EmbellishmentCost, EmbellishmentCostItem, form=EmbellishmentItemsForm)
                embl_form_item = ec_factory(request.POST, request.FILES)
                if embl_form.is_valid() and embl_form_item.is_valid():
                    data = embl_form.save()
                    inserted_by = request.user
                    embl_form.instance.b_job_no = BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=inserted_by)))
                    embl_form.instance.inserted_by = inserted_by
                    embl_form.save()
                    embl_form_item.instance = data
                    embl_form_item.save()
                    # helper.embl_inline(
                    #     EmbConsCosting.objects.filter(inserted_by=request.user).order_by('-id')[:int(request.POST.get("embl_count"))],
                    #     EmbellishmentCostItem.objects.filter(embellishment_cost=helper.job_no(EmbellishmentCost.objects.filter(inserted_by=request.user))).order_by('-id')[:int(request.POST.get("embl_count"))],
                    #     int(request.POST.get("embl_count"))
                    # )
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(embl_form_item.errors)

        elif request.POST.get("_task") == 'embcost_data':  # For embl costing 1 dzn form
            embcons_costing_model = EmbConsCosting(b_job_no=BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=request.user))),
            inserted_by=request.user,
            tt_cons = request.POST.get("tt_cons"),
            tt_rate = request.POST.get("tt_rate"),
            tt_amount = request.POST.get("tt_amount"),
            avg_tt_cons = request.POST.get("avg_tt_cons"),
            avg_tt_rate = request.POST.get("avg_tt_rate"),
            avg_tt_amount = request.POST.get("avg_tt_amount"),
            )
            embcons_costing_model.save()
            for i in range(0, len(helper.color_size(OrderEntryInfo.objects.get(id=int(request.POST.get('__po_job')[5:]))))):
                data = EmbConsCosting_Items(
                    color_size=ColorSizeItems.objects.get(id=request.POST.get(f'id_{i+1}')),
                    emb_cons_costing = embcons_costing_model,
                    po_no = request.POST.get(f"po_no_{i+1}"),
                    country = request.POST.get(f"country_{i+1}"),
                    gmts_item = request.POST.get(f"gmts_item_{i+1}"),
                    color = request.POST.get(f"color_{i+1}"),
                    gmts_size = request.POST.get(f"gmts_size_{i+1}"),
                    cons = request.POST.get(f"cons_{i+1}"),
                    ex_pct = request.POST.get(f"ex_pct_{i+1}"),
                    tt_cons = request.POST.get(f"tt_cons_{i+1}"),
                    rate = request.POST.get(f"rate_{i+1}"),
                    amount = request.POST.get(f"amount_{i+1}"),
                    
                )
                data.save()
        elif request.POST.get('_task') == "wash_form":          #For Wash cost
            if request.method == "GET":
                wash_form = WashCostForm()
                wac_factory = inlineformset_factory(WashCost, WashCost_Items, form=WashCostItemsForm, extra=1)
                wash_form_item = wac_factory()
           
            elif request.method == "POST":
                wash_form = WashCostForm(request.POST, request.FILES)
                wac_factory = inlineformset_factory(WashCost, WashCost_Items, form=WashCostItemsForm)
                wash_form_item = wac_factory(request.POST, request.FILES)
                if wash_form.is_valid() and wash_form_item.is_valid():
                    data = wash_form.save()
                    inserted_by = request.user
                    wash_form.instance.b_job_no = BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=inserted_by)))
                    wash_form.instance.inserted_by = inserted_by
                    wash_form.save()
                    wash_form_item.instance = data
                    wash_form_item.save()
                    # helper.wash_inline(
                    #     WashConsCosting.objects.filter(inserted_by=request.user).order_by('-id')[:int(request.POST.get("wash_count"))],
                    #     WashCost_Items.objects.filter(embellishment_cost=helper.job_no(WashCost.objects.filter(inserted_by=request.user))).order_by('-id')[:int(request.POST.get("wash_count"))],
                    #     int(request.POST.get("wash_count"))
                    # )
                    return HttpResponseRedirect(request.path_info)
                else:
                    messages.error(request , "Something went wrong!")
                    print(wash_form_item.errors)

        elif request.POST.get("_task") == 'washcost_data':  # For wash costing 1 dzn form
            washcons_costing_model = WashConsCosting(b_job_no=BudgetPreCost.objects.get(id=helper.bc_job_no(BudgetPreCost.objects.filter(inserted_by=request.user))),
            inserted_by=request.user,
            w_tt_cons = request.POST.get("w_tt_cons"),
            w_tt_ex_pct = request.POST.get("w_tt_ex_pct"),
            w_grand_tt_cons = request.POST.get("w_grand_tt_cons"),
            w_tt_rate = request.POST.get("w_tt_rate"),
            w_sub_tt_amount = request.POST.get("w_sub_tt_amount"),
            w_grand_tt_qty = request.POST.get("w_grand_tt_qty"),
            w_grand_tt_amount = request.POST.get("w_grand_tt_amount"),
            w_avg_tt_cons = request.POST.get("w_avg_tt_cons"),
            w_avg_ex_pct = request.POST.get("w_avg_ex_pct"),
            w_avg_grand_tt_cons = request.POST.get("w_avg_grand_tt_cons"),
            w_avg_tt_rate = request.POST.get("w_avg_tt_rate"),
            w_avg_sub_tt_amount = request.POST.get("w_avg_sub_tt_amount"),
            w_avg_grand_tt_qty = request.POST.get("w_avg_grand_tt_qty"),
            w_avg_grand_tt_amount = request.POST.get("w_avg_grand_tt_amount"),
            )
            washcons_costing_model.save()
            for i in range(0, len(helper.color_size(OrderEntryInfo.objects.get(id=int(request.POST.get('__po_job')[5:]))))):
                data = WashConsCosting_Items(
                    color_size=ColorSizeItems.objects.get(id=request.POST.get(f'id_{i+1}')),
                    wash_cons_cost = washcons_costing_model,
                    w_po_no = request.POST.get(f"w_po_no_{i+1}"),
                    w_country = request.POST.get(f"w_country_{i+1}"),
                    w_gmts_item = request.POST.get(f"w_gmts_item_{i+1}"),
                    w_color = request.POST.get(f"w_color_{i+1}"),
                    w_gmts_size = request.POST.get(f"w_gmts_size_{i+1}"),
                    w_item_qty = request.POST.get(f"w_item_qty_{i+1}"),
                    w_cons = request.POST.get(f"w_cons_{i+1}"),
                    w_ex_pct = request.POST.get(f"w_ex_pct_{i+1}"),
                    w_tt_cons = request.POST.get(f"w_tt_cons_{i+1}"),
                    w_rate = request.POST.get(f"w_rate_{i+1}"),
                    w_amount = request.POST.get(f"w_amount_{i+1}"),
                    w_tt_qty = request.POST.get(f"w_tt_qty_{i+1}"),
                    w_tt_amount = request.POST.get(f"w_tt_amount_{i+1}"),
                    w_pcs = request.POST.get(f"w_pcs_{i+1}"),
                    
                )
                data.save()

        else:
            context ={
                'form':form,
                'fab_desc':fab_desc,
                'pcs': pcs,
                'body_parts': body_parts,
                'knitting_item': knitting_item,
                'dyeing_item': dyeing_item,
                'country': country,
                'groups': groups,
                'nom_supp': nom_supp,
                'types':types,
                'w_types':w_types,
                'fab_form': fab_form,
                'form_items_fc': form_items_fc,
                'yarn_form': yarn_form,
                'form_items_yc': form_items_yc,
                'con_form': con_form,
                'form_items_cc': form_items_cc,
                'trim_form': trim_form,
                'trim_form_item': trim_form_item,
                'embl_form': embl_form,
                'embl_form_item': embl_form_item,
                'wash_form':wash_form,
                'wash_form_item': wash_form_item,
                'fetch': OrderEntryInfo.objects.get(id=int(request.POST.get('_task')[5:])),
                'color': helper.color_size(OrderEntryInfo.objects.get(id=int(request.POST.get('_task')[5:]))),
                'color_count': len(helper.color_size(OrderEntryInfo.objects.get(id=int(request.POST.get('_task')[5:])))),
                'total_po': helper.total(OrderEntryInfo.objects.get(id=int(request.POST.get('_task')[5:])), 'po_quantity'),
                'total_avg_price': helper.total(OrderEntryInfo.objects.get(id=int(request.POST.get('_task')[5:])), 'avg_price'),
                'gmts_item': helper.gmts_item(OrderEntryInfo.objects.get(id=int(request.POST.get('_task')[5:])), 'gmt'),
                'gmts_color': helper.gmts_item(OrderEntryInfo.objects.get(id=int(request.POST.get('_task')[5:])), 'color'),
                'con_color': len(helper.gmts_item(OrderEntryInfo.objects.get(id=int(request.POST.get('_task')[5:])), 'color'))
            }
            
            return render(request, 'Merchandising/Order/pre_costing.html', context)

    form = BudgetPreCostForm()
    fab_form = FabricCostForm()
    fc_factory = inlineformset_factory(FabricCost, Fabric_Inline_Item, form=FabricItemForm, extra=1)
    form_items_fc = fc_factory()
    fab_desc = LibraryFabricDescription.objects.all()

    yarn_form = YarnCostForm()
    yc_factory = inlineformset_factory(YarnCost, Yarn_Inline_Item, form=YarnItemForm, extra=1)
    form_items_yc = yc_factory()
        
    context ={
        'form':form,
        'fab_desc':fab_desc, 
        'body_parts': body_parts,
        'knitting_item': knitting_item,
        'dyeing_item': dyeing_item,
        'country': country,
        'groups': groups,
        'nom_supp': nom_supp,
        'types':types,
        'w_types':w_types,
        'fab_form': fab_form,
        'form_items_fc': form_items_fc,
        'yarn_form': yarn_form,
        'form_items_yc': form_items_yc,
        'con_form': con_form,
        'form_items_cc': form_items_cc,
        'trim_form': trim_form,
        'trim_form_item': trim_form_item,
        'embl_form': embl_form,
        'embl_form_item': embl_form_item,
        'wash_form':wash_form,
        'wash_form_item': wash_form_item,
    }
    return render(request, 'Merchandising/Order/pre_costing.html', context)

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
    po_details = PO_Details.objects.all().order_by('-id')
    myFilter = OrderSelectFilter(request.GET , queryset = po_details)
    po_details = myFilter.qs
    context = {
        'myFilter': myFilter,
        'po_details':po_details,
    }
    return render(request, 'Merchandising/Order/order_selection.html', context)


def work_progress(request, id):
    work_progress = PO_Details.objects.get(id=id)
    
    context={
        'work_progress': work_progress,
    }
    return render(request, 'Merchandising/Order/WIP/work_progress.html', context)

def work_progress_report(request):
    orders = OrderEntryInfo.objects.all().prefetch_related('order_entry')
    myFilter = OrderFilter(request.GET , queryset = orders)
    orders = myFilter.qs
    context = {
        'orders': orders,
        'myFilter': myFilter,
    }
    return render(request, 'Merchandising/Order/WIP/work_progress_report.html', context)

def tna_progress_report(request, id):
    tna_progress = PO_Details.objects.get(id=id)
    
    context={
        'tna_progress': tna_progress,
    }
    return render(request, 'Merchandising/Order/WIP/tna_progress_report.html', context)

def color_size_summary(request):
    
    return render(request, 'Merchandising/Order/WIP/color_size_summary.html')

def sample_approval_details(request):
    return render(request, 'Merchandising/Order/WIP/sample_approval_details.html')

def lapdip_approval_details(request):
    return render(request, 'Merchandising/Order/WIP/lapdip_approval_details.html')

def accessories_approval_details(request):
    return render(request, 'Merchandising/Order/WIP/accessories_approval_details.html')

def fabric_booking_details(request):
    return render(request, 'Merchandising/Order/WIP/fabric_booking_details.html')

def finish_fabric_details(request):
    return render(request, 'Merchandising/Order/WIP/finish_fabric_details.html')

def trims_details(request):
    return render(request, 'Merchandising/Order/WIP/trims_details.html')

def cutting_finish_details(request):
    return render(request, 'Merchandising/Order/WIP/cutting_finish.html')

def iron_finish_details(request):
    return render(request, 'Merchandising/Order/WIP/iron_finish_details.html')

def finishing_details(request):
    return render(request, 'Merchandising/Order/WIP/finishing_details.html')

def buyer_inspection_details(request):
    return render(request, 'Merchandising/Order/WIP/buyer_inspection_details.html')

def actual_shipment_details(request):
    return render(request, 'Merchandising/Order/WIP/actual_shipment_details.html')