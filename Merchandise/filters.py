from django.forms.widgets import Widget
import django_filters
from django_filters import FilterSet,DateFilter,CharFilter,DateFromToRangeFilter
from django_filters.widgets import RangeWidget,CSVWidget,DateRangeWidget
from django import forms
from django_filters import DateFilter
from .models import *

# def date(request):
#     if request is None:
#         return PO_Details.objects.none()

#     date = request.user.company
#     return company.department_set.all()

class OrderFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="order_entry__pub_shipment_date",lookup_expr='gte',label='From Date')
    # end_date = DateFilter(field_name="order_entry__pub_shipment_date",lookup_expr='lte',label='To Date')
    start_date = django_filters.DateFilter(field_name='order_entry__pub_shipment_date', lookup_expr='gte', label='From Date')
    end_date =  django_filters.DateFilter(field_name='order_entry__pub_shipment_date', lookup_expr='lte', label='To Date')
    style_description = django_filters.CharFilter(lookup_expr='icontains')
    job_no = django_filters.CharFilter(lookup_expr='icontains')
    po_no = django_filters.CharFilter(field_name='order_entry__po_no', lookup_expr='exact')
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
    start_date = DateFilter(field_name="pub_shipment_date",lookup_expr='gte',label='From Date')
    end_date = DateFilter(field_name="pub_shipment_date",lookup_expr='lte',label='To Date')
    company_name = django_filters.CharFilter(field_name='po_job_no__company_name__company_name', lookup_expr='icontains')
    job_no = django_filters.CharFilter(field_name='po_job_no__job_no', lookup_expr='icontains')
    buyer_name = django_filters.CharFilter(field_name='po_job_no__buyer_name__buyer_name', lookup_expr='icontains')
    company_location = django_filters.CharFilter(field_name='po_job_no__company_location__location_name', lookup_expr='icontains')
    agent = django_filters.CharFilter(field_name='po_job_no__agent__agent_name', lookup_expr='icontains')
    style_description = django_filters.CharFilter(field_name='po_job_no__style_description', lookup_expr='icontains')
    team_leader = django_filters.CharFilter(field_name='po_job_no__team_leader__leader_name', lookup_expr='icontains')
    dealing_merchant = django_filters.CharFilter(field_name='po_job_no__dealing_merchant__d_merchant_name', lookup_expr='icontains')
    factory_merchant = django_filters.CharFilter(field_name='po_job_no__factory_merchant__f_merchant_name', lookup_expr='icontains')
    product_cate = django_filters.CharFilter(field_name='po_job_no__product_cate__category_name', lookup_expr='icontains')
    po_no = django_filters.CharFilter(lookup_expr='icontains')
    insert_date = DateFilter(field_name="insert_date")
    class Meta:
        model = PO_Details
        fields = [
        'job_no',
        'po_no',
        'company_name',
        'buyer_name', 
        'company_location', 
        'agent', 
        'style_description',
        'team_leader', 
        'dealing_merchant', 
        'factory_merchant', 
        'product_cate',
        'inserted_by', 
        'insert_date',
        ]

        
class PO_OrderFilter(django_filters.FilterSet):
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
        'inserted_by',
        'product_cate', 
        ]

class OrderSelectFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="pub_shipment_date",lookup_expr='gte',label='From Date')
    end_date = DateFilter(field_name="pub_shipment_date",lookup_expr='lte',label='To Date')
    style_ref = django_filters.CharFilter(field_name='po_job_no__internal_ref', lookup_expr='icontains')
    company_name = django_filters.CharFilter(field_name='po_job_no__company_name__company_name', lookup_expr='icontains')
    job_no = django_filters.CharFilter(field_name='po_job_no__job_no', lookup_expr='icontains')
    buyer_name = django_filters.CharFilter(field_name='po_job_no__buyer_name__buyer_name', lookup_expr='icontains')
    class Meta:
        model = PO_Details
        fields = [
        'job_no', 
        'buyer_name', 
        'company_name',
        'style_ref',
        'internal_ref', 
        'file_no', 
        'po_no', 
        'inserted_by',
        
        ]