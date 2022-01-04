from django.urls import path
from . import views

urlpatterns=[
    path('lib_buyer/', views.lib_buyer, name= 'lib_buyer'),
    path('lib_company/', views.lib_company, name= 'lib_company'),
    path('lib_company_address/', views.lib_company_address, name= 'lib_company_address'),
    path('lib_prod_dept/', views.lib_prod_dept, name= 'lib_prod_dept'),
    path('lib_prod_subdept/', views.lib_prod_subdept, name= 'lib_prod_subdept'),
    path('lib_product_cate/', views.lib_product_cate, name= 'lib_product_cate'),
    path('lib_team_leader/', views.lib_team_leader, name= 'lib_team_leader'),
    path('lib_dealing_merchant/', views.lib_dealing_merchant, name= 'lib_dealing_merchant'),
    path('lib_factory_merchant/', views.lib_factory_merchant, name= 'lib_factory_merchant'),
    path('lib_season/', views.lib_season, name= 'lib_season'),
    path('lib_region/', views.lib_region, name= 'lib_region'),
    path('lib_agent/', views.lib_agent, name= 'lib_agent'),
    path('lib_client/', views.lib_client, name= 'lib_client'),
    path('lib_currency/', views.lib_currency, name= 'lib_currency'),
    path('lib_packing/', views.lib_packing, name= 'lib_packing'),
    path('lib_shipmode/', views.lib_shipmode, name= 'lib_shipmode'),
    path('lib_qualitylabel/', views.lib_qualitylabel, name= 'lib_qualitylabel'),
    path('lib_unit/', views.lib_unit, name= 'lib_unit'),
    path('lib_shipment_term/', views.lib_shipment_term, name= 'lib_shipment_term'),
    path('lib_design_source/', views.lib_design_source, name= 'lib_design_source'),
    path('lib_country/', views.lib_country, name= 'lib_country'),
    path('lib_country_type/', views.lib_country_type, name= 'lib_country_type'),
    path('lib_cut_off/', views.lib_cut_off, name= 'lib_cut_off'),
    path('lib_gmt_prod/', views.lib_gmt_prod, name= 'lib_gmt_prod'),
    path('lib_payment_term/', views.lib_payment_term, name= 'lib_payment_term'),
    path('lib_fabrication/', views.lib_fabrication, name= 'lib_fabrication'),

    # EDIT / DELETE
    path('edit_agent/<int:id>/', views.edit_agent, name= 'edit_agent'),
    path('delete_agent/<int:id>/', views.delete_agent, name= 'delete_agent'),

    path('edit_buyer/<int:id>/', views.edit_buyer, name= 'edit_buyer'),
    path('delete_buyer/<int:id>/', views.delete_buyer, name= 'delete_buyer'),
    
    path('edit_client/<int:id>/', views.edit_client, name= 'edit_client'),
    path('delete_client/<int:id>/', views.delete_client, name= 'delete_client'),
    
    path('edit_company/<int:id>/', views.edit_company, name= 'edit_company'),
    path('delete_company/<int:id>/', views.delete_company, name= 'delete_company'),
    
    # path('edit_companyAddress/<int:id>/', views.edit_companyAddress, name= 'edit_companyAddress'),
    # path('delete_compAddress/<int:id>/', views.delete_compAddress, name= 'delete_compAddress'),
    
    path('edit_prodDept/<int:id>/', views.edit_prodDept, name= 'edit_prodDept'),
    path('delete_prodDept/<int:id>/', views.delete_prodDept, name= 'delete_prodDept'),
    
    path('edit_prodSubDept/<int:id>/', views.edit_prodSubDept, name= 'edit_prodSubDept'),
    path('delete_prodSubDept/<int:id>/', views.delete_prodSubDept, name= 'delete_prodSubDept'),
    
    path('edit_prodcate/<int:id>/', views.edit_prodcate, name= 'edit_prodcate'),
    path('delete_prodcate/<int:id>/', views.delete_prodcate, name= 'delete_prodcate'),
    
    path('edit_teamleader/<int:id>/', views.edit_teamleader, name= 'edit_teamleader'),
    path('delete_teamleader/<int:id>/', views.delete_teamleader, name= 'delete_teamleader'),
    
    path('edit_dealMerchant/<int:id>/', views.edit_dealMerchant, name= 'edit_dealMerchant'),
    path('delete_dealMerchant/<int:id>/', views.delete_dealMerchant, name= 'delete_dealMerchant'),
    
    path('edit_factMerchant/<int:id>/', views.edit_factMerchant, name= 'edit_factMerchant'),
    path('delete_factMerchant/<int:id>/', views.delete_factMerchant, name= 'delete_factMerchant'),
    
    path('edit_season/<int:id>/', views.edit_season, name= 'edit_season'),
    path('delete_season/<int:id>/', views.delete_season, name= 'delete_season'),
    
    path('edit_region/<int:id>/', views.edit_region, name= 'edit_region'),
    path('delete_region/<int:id>/', views.delete_region, name= 'delete_region'),
    
    path('edit_currency/<int:id>/', views.edit_currency, name= 'edit_currency'),
    path('delete_currency/<int:id>/', views.delete_currency, name= 'delete_currency'),
    
    path('edit_packing/<int:id>/', views.edit_packing, name= 'edit_packing'),
    path('delete_packing/<int:id>/', views.delete_packing, name= 'delete_packing'),
    
    path('edit_shipmode/<int:id>/', views.edit_shipmode, name= 'edit_shipmode'),
    path('delete_shipmode/<int:id>/', views.delete_shipmode, name= 'delete_shipmode'),
    
    path('edit_qualitylabel/<int:id>/', views.edit_qualitylabel, name= 'edit_qualitylabel'),
    path('delete_qualitylabel/<int:id>/', views.delete_qualitylabel, name= 'delete_qualitylabel'),

    path('edit_unit/<int:id>/', views.edit_unit, name= 'edit_unit'),
    path('delete_unit/<int:id>/', views.delete_unit, name= 'delete_unit'),

    path('edit_shipment_term/<int:id>/', views.edit_shipment_term, name= 'edit_shipment_term'),
    path('delete_shipment_term/<int:id>/', views.delete_shipment_term, name= 'delete_shipment_term'),

    path('edit_design_source/<int:id>/', views.edit_design_source, name= 'edit_design_source'),
    path('delete_design_source/<int:id>/', views.delete_design_source, name= 'delete_design_source'),
    
    path('edit_country/<int:id>/', views.edit_country, name= 'edit_country'),
    path('delete_country/<int:id>/', views.delete_country, name= 'delete_country'),

    path('edit_country_type/<int:id>/', views.edit_country_type, name= 'edit_country_type'),
    path('delete_country_type/<int:id>/', views.delete_country_type, name= 'delete_country_type'),

    path('edit_cut_off/<int:id>/', views.edit_cut_off, name= 'edit_cut_off'),
    path('delete_cut_off/<int:id>/', views.delete_cut_off, name= 'delete_cut_off'),

    path('edit_product/<int:id>/', views.edit_product, name= 'edit_product'),
    path('delete_product/<int:id>/', views.delete_product, name= 'delete_product'),
    
    path('edit_payment_term/<int:id>/', views.edit_payment_term, name= 'edit_payment_term'),
    path('delete_payment_term/<int:id>/', views.delete_payment_term, name= 'delete_payment_term'),

    path('edit_fabrication/<int:id>/', views.edit_fabrication, name= 'edit_fabrication'),
    path('delete_fabrication/<int:id>/', views.delete_fabrication, name= 'delete_fabrication'),
    
    #Main Form Urls
    path('order_entry/', views.order_entry, name= 'order_entry'),
    path('view_order/<int:id>/', views.view_order, name= 'view_order'),
    path('edit_order/<int:id>/', views.edit_order, name= 'edit_order'),
    path('delete_order/<int:id>/', views.delete_order, name= 'delete_order'),
    path('order_report/', views.order_report, name= 'order_report'),
    # path('po_details/', views.po_details, name= 'po_details'),
    # path('color_size_entry/', views.color_size_entry, name= 'color_size_entry'),
    path('pre_costing/', views.pre_costing, name= 'pre_costing'),
    path('capacity_booked/', views.capacity_booked, name= 'capacity_booked'),
    path('shipment_schedule/', views.shipment_schedule, name= 'shipment_schedule'),
    path('order_selection/', views.order_selection, name= 'order_selection'),
    path('work_progress/<int:id>/', views.work_progress, name= 'work_progress'),
    path('work_progress_report/', views.work_progress_report, name= 'work_progress_report'),
    path('tna_progress_report/<int:id>/', views.tna_progress_report, name= 'tna_progress_report'),
    path('color_size_summary/', views.color_size_summary, name= 'color_size_summary'),
    path('sample_approval_details/', views.sample_approval_details, name= 'sample_approval_details'),
    path('lapdip_approval_details/', views.lapdip_approval_details, name= 'lapdip_approval_details'),
    path('accessories_approval_details/', views.accessories_approval_details, name= 'accessories_approval_details'),
    path('fabric_booking_details/', views.fabric_booking_details, name= 'fabric_booking_details'),
    path('finish_fabric_details/', views.finish_fabric_details, name= 'finish_fabric_details'),
    path('trims_details/', views.trims_details, name= 'trims_details'),

]