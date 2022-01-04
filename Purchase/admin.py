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

class PurchaseBankAdmin(admin.ModelAdmin):
    list_display = ['l_ref_no', 'p_date', 'buyer_name', 'inv_no', 'bill_no', 'bill_date']
    actions = [export_to_csv]

admin.site.register(PurchaseBank,PurchaseBankAdmin)
admin.site.register(Bank)
admin.site.register(BankBranch)
admin.site.register(BankAddress)
admin.site.register(ShipmentChalan)
admin.site.register(ShipmentChalanItems)
admin.site.register(Chechboxes)
