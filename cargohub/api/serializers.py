from rest_framework import serializers
from api.models import *

from .models import Clients, Warehouses, Suppliers, Shipments, Orders, Locations, Items, Item_types, Item_groups, Item_lines, Transfers, Inventories

class ClientSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=255)
    # address = serializers.CharField()
    # city = serializers.CharField(max_length=100)
    # zip_code = serializers.CharField(max_length=20)
    # province = serializers.CharField(max_length=100)
    # country = serializers.CharField(max_length=100)
    # contact_name = serializers.CharField(max_length=255)
    # contact_phone = serializers.CharField(max_length=50)
    # contact_email = serializers.EmailField()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta:
        model = Clients  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include


class WarehousesSerializer(serializers.ModelSerializer):
    # id = models.AutoField(primary_key=True)
    # code = models.CharField(max_length=20)
    # name = models.CharField(max_length=255)
    # address = models.TextField()
    # zip = models.CharField(max_length=20)
    # city = models.CharField(max_length=100)
    # province = models.CharField(max_length=100)
    # country = models.CharField(max_length=100)
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta:
        model = Warehouses  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include



class SuppliersSerializer(serializers.ModelSerializer):
    # id = models.AutoField(primary_key=True)
    # code = serializers.CharField(max_length=7)
    # name = serializers.CharField(max_length=255)
    # address = serializers.CharField()
    # address_extra = serializers.CharField()
    # city = serializers.CharField(max_length=100)
    # zip_code = serializers.CharField(max_length=20)
    # province = serializers.CharField(max_length=100)
    # country = serializers.CharField(max_length=100)
    # contact_name = serializers.CharField(max_length=255)
    # phonenumber = serializers.CharField(max_length=50)
    # reference = serializers.CharField(max_length=20)
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta:
        model = Suppliers  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include

    

class ShipmentsSerializer(serializers.ModelSerializer): 
    # id = models.AutoField(primary_key=True)
    # order_id = models.IntegerField(default=0)
    # source_id = models.IntegerField(default=0)  # ?
    # order_date = models.DateField()
    # request_date = models.DateField()
    # shipment_date = models.DateField()
    # shipment_type = models.CharField(max_length=20)
    # notes = models.TextField()
    # carrier_code = models.CharField(max_length=20)
    # carrier_description = models.TextField()
    # service_code = models.CharField(max_length=20, default=None)
    # payment_type = models.CharField(max_length=20)
    # transfer_mode = models.CharField(max_length=20)
    # total_package_count = models.IntegerField(default=0)
    # total_package_weight = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        model = Shipments  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include


class TransfersSerializer(serializers.ModelSerializer):
    # id = models.AutoField(primary_key=True)
    # reference = serializers.CharField(max_length=7, required=True)
    # transfer_from = serializers.CharField(max_length=255, required=True)
    # transfer_to = serializers.CharField(max_length=4, required=True)
    # transfer_status = serializers.CharField(max_length=255, required=True)
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta:
        model = Transfers  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include

    

class OrdersSerializer(serializers.ModelSerializer):
    # source_id = serializers.IntegerField()
    # order_date = serializers.DateTimeField()
    # request_date = serializers.DateTimeField()
    # reference = serializers.CharField(max_length=255)
    # reference_extra = serializers.CharField(max_length=255, required=True)  
    # order_status = serializers.CharField(max_length=50)
    # notes = serializers.CharField(max_length=255, required=True) 
    # shipping_notes = serializers.CharField(max_length=255, required=True) 
    # picking_notes = serializers.CharField(max_length=255, required=True) 
    # warehouse_id = serializers.IntegerField()
    # ship_to = serializers.CharField(max_length=255, required=True)  
    # bill_to = serializers.CharField(max_length=255, required=True)  
    # shipment_id = serializers.IntegerField(required=False) 
    # total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    # total_discount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    # total_tax = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    # total_surcharge = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta:
        model = Orders  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include



class OrderItemSerializer(serializers.ModelSerializer):
    from .models import Orders
    # order = serializers.PrimaryKeyRelatedField(queryset=Orders.objects.all())
    # item_id = serializers.CharField(max_length=50)
    # amount = serializers.IntegerField()
    class Meta:
        model = Orders  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include


class LocationsSerializer(serializers.ModelSerializer):
    # id = models.AutoField(primary_key=True)
    # warehouse_id = serializers.IntegerField()
    # code = serializers.CharField(max_length=5)
    # name = serializers.CharField(max_length=255)
    # created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    class Meta:
        model = Locations  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include

class ItemsSerializer(serializers.ModelSerializer):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # code = models.CharField(max_length=255)
    # description = models.TextField()
    # short_description = models.CharField(max_length=255)
    # upc_code = models.CharField(max_length=255)
    # model_number = models.CharField(max_length=255)
    # commodity_code = models.CharField(max_length=255)
    # item_line = models.IntegerField(default=0)
    # item_group = models.IntegerField(default=0)
    # item_type = models.IntegerField(default=0)
    # unit_purchase_quantity = models.IntegerField(default=0)
    # unit_order_quantity = models.IntegerField(default=0)
    # pack_order_quantity = models.IntegerField(default=0)
    # supplier_id = models.IntegerField(default=0)
    # supplier_code = models.CharField(max_length=255)
    # supplier_part_number = models.CharField(max_length=255)
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        model = Items  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include


class ItemLinesSerializer(serializers.ModelSerializer):
    # id = models.AutoField(primary_key=True)
    # name = serializers.CharField(max_length=255)
    # description = serializers.CharField()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta:
        model = Item_lines  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include


class ItemTypesSerializer(serializers.ModelSerializer):
    # id = models.AutoField(primary_key=True)
    # name = serializers.CharField(max_length=255)
    # description = serializers.CharField()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta:
        model = Item_types
        #fields = ('name', 'description', 'created_at', 'updated_at')
        fields = '__all__'



class ItemGroupsSerializer(serializers.ModelSerializer):
    # id = models.AutoField(primary_key=True)
    # name = serializers.CharField(max_length=255)
    # description = serializers.CharField()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta:
        model = Item_groups  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include

class InventoriesSerializer(serializers.ModelSerializer):
    # id = models.AutoField(primary_key=True)
    # item_id = models.CharField(max_length=255)
    # description = models.TextField()
    # item_reference = models.CharField(max_length=100)
    # locations = models.JSONField()  # MIGHT cause problems...
    # total_on_hand = models.IntegerField(default=0)
    # total_expected = models.IntegerField(default=0)
    # total_ordered = models.IntegerField(default=0)
    # total_allocated = models.IntegerField(default=0)
    # total_available = models.IntegerField(default=0)
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        model = Inventories  # Replace `Client` with the actual model name
        fields = '__all__'  # Or specify the list of fields you want to include

class PseudoModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pseudo_models
        fields = '__al__'
