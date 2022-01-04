from django.forms.widgets import Widget
import django_filters
from django_filters import FilterSet,DateFilter,CharFilter,DateFromToRangeFilter
from django_filters.widgets import RangeWidget,CSVWidget,DateRangeWidget
from django import forms
from django_filters import DateFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    
    start_date = DateFilter(field_name="insert_date",lookup_expr='gte',label='From Date')
    end_date = DateFilter(field_name="insert_date",lookup_expr='lte',label='To Date')
    style_description = django_filters.CharFilter(lookup_expr='icontains')
    job_no = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = OrderEntryInfo
        fields = [
        # 'job_no', 
        'buyer_name', 
        'company_name',
        'company_location', 
        'agent', 
        'style_description',
        'team_leader', 
        'dealing_merchant', 
        'factory_merchant', 
        'product_cate', 
        ]
        
class POFilter(django_filters.FilterSet):
    
    start_date = DateFilter(field_name="insert_date",lookup_expr='gte',label='From Date')
    end_date = DateFilter(field_name="insert_date",lookup_expr='lte',label='To Date')
    company_name = CharFilter(field_name='po_job_no__company_name', lookup_expr='icontains')
    class Meta:
        model = PO_Details
        fields = [
        
        'company_name', 
        ]
        

        
