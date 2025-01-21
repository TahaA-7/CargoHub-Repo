from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [

    #GET and POST methods:
    path('clients/', views.client_list, name='client_list'), 
    path('orders/', views.order_list, name='order_list'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('items/', views.item_list, name='item_list'),
    path('item_groups/', views.item_group_list, name='item_group_list'),
    path('item_lines/', views.item_lines_list, name='item_lines_list'),
    path('item_types/', views.item_types_list, name='item_types_list'),
    path('transfers/', views.transfer_list, name='transfer_list'),
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('inventories/', views.inventory_list, name='inventory_list'),
    path('locations/', views.location_list, name='location_list'),
    path('shipments/', views.shipment_list, name='shipment_list'),

    path('pseudo_models/', views.pseudo_models_list, name='pseudo_models_list'),

    #PUT, DELETE and GET methods for individual resources (by primary key (pk)):
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('suppliers/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    path('item_groups/<int:pk>/', views.item_group_detail, name='item_group_detail'),
    path('item_lines/<int:pk>/', views.item_lines_detail, name='item_lines_detail'),
    path('item_types/<int:pk>/', views.item_types_detail, name='item_types_detail'),
    path('transfers/<int:pk>/', views.transfer_detail, name='transfer_detail'),
    path("transfers/<int:transfer_id>/commit/", views.transfer_commit, name="transfer_commit"),
    path('warehouses/<int:pk>/', views.warehouse_detail, name='warehouse_detail'),
    path('inventories/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('locations/<int:pk>/', views.location_detail, name='location_detail'),
    path('shipments/<int:pk>/', views.shipment_detail, name='shipment_detail'),

    # path('helloworld', views.hello_world, name='hello_world'),

    path('pseudo_models/<int:pk>/', views.pseudo_models_detail, name='pseudo_models_detail'),
]