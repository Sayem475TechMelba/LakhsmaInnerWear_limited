from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;'\
          'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many\
        and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'

class BuyerAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class CompanyAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class CompAddressAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class ProdDeptAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class ProdSubDeptAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class ProductCateAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class TeamLeaderAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class DealingMerchantAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class FactoryMerchantAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class SeasonAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class RegionAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class AgentAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class ClientAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class CurrencyAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class PackingAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class ShipModeAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class QualityLabelAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class UnitAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class ShipmentTermAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class OrderEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'job_no','insert_date', 'buyer_name', 'company_name']
    actions = [export_to_csv]

class PoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pub_shipment_date', 'po_job_no']
    list_filter = ['pub_shipment_date']
    actions = [export_to_csv]

admin.site.register(LibraryBuyer, BuyerAdmin)
admin.site.register(LibraryCompany, CompanyAdmin)
admin.site.register(LibraryCompAddress, CompAddressAdmin)
admin.site.register(LibraryProdDept, ProdDeptAdmin)
admin.site.register(LibraryProdSubDept, ProdSubDeptAdmin)
admin.site.register(LibraryProductCate, ProductCateAdmin)
admin.site.register(LibraryTeamLeader, TeamLeaderAdmin)
admin.site.register(LibraryDealingMerchant, DealingMerchantAdmin)
admin.site.register(LibraryFactoryMerchant, FactoryMerchantAdmin)
admin.site.register(LibrarySeason, SeasonAdmin)
admin.site.register(LibraryRegion, RegionAdmin)
admin.site.register(LibraryAgent, AgentAdmin)
admin.site.register(LibraryClient, ClientAdmin)
admin.site.register(LibraryCurrency, CurrencyAdmin)
admin.site.register(LibraryPacking, PackingAdmin)
admin.site.register(LibraryShipMode, ShipModeAdmin)
admin.site.register(LibraryQualityLabel, QualityLabelAdmin)
admin.site.register(LibraryUnit, UnitAdmin)
admin.site.register(LibraryShipmentTerm, ShipmentTermAdmin)
admin.site.register(OrderEntryInfo, OrderEntryAdmin)
admin.site.register(PO_Details,PoAdmin)
admin.site.register(LibraryCountry)
admin.site.register(LibraryProduct)
admin.site.register(ColorSizeItems)
admin.site.register(SmvItems)
admin.site.register(BudgetPreCost)
admin.site.register(Grey_Cons_Items)
admin.site.register(Grey_Cons)