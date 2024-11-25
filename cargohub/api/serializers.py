from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    city = serializers.CharField(max_length=100)
    zip_code = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=255)
    contact_phone = serializers.CharField(max_length=50)
    contact_email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class WarehousesSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=8)
    name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    zip = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=100)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=255)
    contact_phone = serializers.CharField(max_length=50)
    contact_email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class SuppliersSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=7)
    name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    address_extra = serializers.CharField()
    city = serializers.CharField(max_length=100)
    zip = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=255)
    phonenumber = serializers.CharField(max_length=50)
    reference = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


    

class ShipmentsSerializer(serializers.ModelSerializer): 
    code = serializers.CharField(max_length=7)
    name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    address_extra = serializers.CharField()
    city = serializers.CharField(max_length=100)
    zip = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=255)
    phonenumber = serializers.CharField(max_length=50)
    reference = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()



class TransfersSerializer(serializers.ModelSerializer):
    reference = serializers.CharField(max_length=7, required=True)
    transfer_from = serializers.CharField(max_length=255, required=True)
    transfer_to = serializers.CharField(max_length=4, required=True)
    transfer_status = serializers.CharField(max_length=255, required=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


    

class OrdersSerializer(serializers.ModelSerializer):
    source_id = serializers.IntegerField()
    order_date = serializers.DateTimeField()
    request_date = serializers.DateTimeField()
    reference = serializers.CharField(max_length=255)
    reference_extra = serializers.CharField(max_length=255, required=True)  
    order_status = serializers.CharField(max_length=50)
    notes = serializers.CharField(max_length=255, required=True) 
    shipping_notes = serializers.CharField(max_length=255, required=True) 
    picking_notes = serializers.CharField(max_length=255, required=True) 
    warehouse_id = serializers.IntegerField()
    ship_to = serializers.CharField(max_length=255, required=True)  
    bill_to = serializers.CharField(max_length=255, required=True)  
    shipment_id = serializers.IntegerField(required=False) 
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_discount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    total_tax = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    total_surcharge = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()




class OrderItemSerializer(serializers.ModelSerializer):
    from .models import Orders
    order = serializers.PrimaryKeyRelatedField(queryset=Orders.objects.all())
    item_id = serializers.CharField(max_length=50)
    amount = serializers.IntegerField()


    


class LocationsSerializer(serializers.ModelSerializer):
    warehouse_id = serializers.IntegerField()
    code = serializers.CharField(max_length=5)
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class ItemsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()



class ItemLinesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()



class ItemTypesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class ItemGroupsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class InventoriesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    city = serializers.CharField(max_length=100)
    zip_code = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=255)
    contact_phone = serializers.CharField(max_length=50)
    contact_email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()