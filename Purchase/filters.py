from django.forms.widgets import Widget
import django_filters
from django_filters import FilterSet,DateFilter,CharFilter,DateFromToRangeFilter
from django_filters.widgets import RangeWidget,CSVWidget,DateRangeWidget
from django import forms
from django_filters import DateFilter
from .models import *

class PurchaseFilter(django_filters.FilterSet):
    
    start_date = DateFilter(field_name="p_date",lookup_expr='gte',label='From Date')
    end_date = DateFilter(field_name="p_date",lookup_expr='lte',label='To Date')
    buyer_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PurchaseBank
        fields = [
        'factory_name', 
        'job_no', 
        'order_no',
        'buyer_name', 
        'bill_no',
        'payment_status', 
        'bill_date', 
        ]
        
class ChalanFilter(django_filters.FilterSet):

    start_date = DateFilter(field_name="chalan_date",lookup_expr='gte',label='From Date')
    end_date = DateFilter(field_name="chalan_date",lookup_expr='lte',label='To Date')
    driver_name = django_filters.CharFilter(lookup_expr='icontains')
    buyer_name = django_filters.CharFilter(lookup_expr='icontains')
    port_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = ShipmentChalan
        fields = [
        'chalan_no', 
        'invoice_no',
        'job_no',
        
        'factory_name', 
        'buyer_name', 
        'driver_name', 
        'shipmode', 
        'port_name', 
         
        ]
        
