from django.urls import path
from . import views
from .views import ChartData

urlpatterns=[
    path('', views.home, name= 'home'),
    
    # START = API FOR GRAPH - USING SERIALIZERS - DJANGO REST FRAMEWORKS
    path('api/data', views.get_data, name= 'get_data'),
    path('api/chart/data',ChartData.as_view(), name= 'ChartData'),
    #FINISH = API FOR GRAPH - USING SERIALIZERS - DJANGO REST FRAMEWORKS
    
    
    path('purchase/', views.purchase, name= 'purchase'),
    path('view_purchase/<int:id>/', views.view_purchase, name= 'view_purchase'),
    
    path('update_purchase/<int:id>/',  views.update_purchase, name='update_purchase' ),
    path('print_purchase/<int:id>/',  views.print_purchase, name='print_purchase' ),
    path('delete_purchase/<int:id>/',  views.delete_purchase, name='delete_purchase' ),
    path('purchase_report/', views.purchase_report, name= 'purchase_report'),
    path('api/erp/bank/', views.bank),

    

    path('deliveryChalan/', views.deliveryChalan, name= 'deliveryChalan'),
    path('viewChalan/<int:id>/', views.viewChalan, name= 'viewChalan'),
    path('editChalan/<int:id>/', views.editChalan, name= 'editChalan'),
    path('delivery_chalan_report/', views.delivery_chalan_report, name= 'delivery_chalan_report'),
    path('print_Challan/<int:id>/', views.print_Challan, name= 'print_Challan'),
    path('delete_Challan/<int:id>/', views.delete_Challan, name= 'delete_Challan'),
    
    
    path('lib_bank/', views.lib_bank, name= 'lib_bank'),
    path('edit_bank/<int:id>/', views.edit_bank, name= 'edit_bank'),
    path('delete_bank/<int:id>/', views.delete_bank, name= 'delete_bank'),
    path('lib_branch/', views.lib_branch, name= 'lib_branch'),
    path('edit_branch/<int:id>/', views.edit_branch, name= 'edit_branch'),
    path('delete_branch/<int:id>/', views.delete_branch, name= 'delete_branch'),
    path('lib_bank_address/', views.lib_bank_address, name= 'lib_bank_address'),
    path('edit_address/<int:id>/', views.edit_address, name= 'edit_address'),
    path('delete_address/<int:id>/', views.delete_address, name= 'delete_address'),
    
    path('login/', views.login, name= 'login'),
    ]