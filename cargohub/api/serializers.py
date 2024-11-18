from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.AutoField(primary_key=True)
    name = serializers.CharField(max_length=255)
    address = serializers.TextField()
    city = serializers.CharField(max_length=100)
    zip_code = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=255)
    contact_phone = serializers.CharField(max_length=50)
    contact_email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class Warehouses(serializers.Model):
    id = serializers.AutoField(primary_key=True)
    code = serializers.CharField(max_length=8)
    name = serializers.CharField(max_length=255)
    address = serializers.TextField()
    zip = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=100)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=255)
    contact_phone = serializers.CharField(max_length=50)
    contact_email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class Suppliers(serializers.Model):
    id = serializers.AutoField(primary_key=True)
    code = serializers.CharField(max_length=7)
    name = serializers.CharField(max_length=255)
    address = serializers.TextField()
    address_extra = serializers.TextField()
    city = serializers.CharField(max_length=100)
    zip = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=255)
    phonenumber = serializers.CharField(max_length=50)
    reference = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


    

class Shipments(serializers.Model): 
    id = serializers.AutoField(primary_key=True)
    code = serializers.CharField(max_length=7)
    name = serializers.CharField(max_length=255)
    address = serializers.TextField()
    address_extra = serializers.TextField()
    city = serializers.CharField(max_length=100)
    zip = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=255)
    phonenumber = serializers.CharField(max_length=50)
    reference = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()



class Transfers(serializers.Model):
    id = serializers.AutoField(primary_key=True)
    reference = serializers.CharField(max_length=7)
    transfer_from = serializers.CharField(max_length=255, null=True)
    transfer_to = serializers.CharField(max_length=4, null=True)
    transfer_status = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


    

class Order(serializers.Model):
    source_id = serializers.IntegerField()
    order_date = serializers.DateTimeField()
    request_date = serializers.DateTimeField()
    reference = serializers.CharField(max_length=255)
    reference_extra = serializers.TextField(blank=True, null=True)
    order_status = serializers.CharField(max_length=50)
    notes = serializers.TextField(blank=True, null=True)
    shipping_notes = serializers.TextField(blank=True, null=True)
    picking_notes = serializers.TextField(blank=True, null=True)
    warehouse_id = serializers.IntegerField()
    ship_to = serializers.TextField(blank=True, null=True)
    bill_to = serializers.TextField(blank=True, null=True)
    shipment_id = serializers.IntegerField(blank=True, null=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_discount = serializers.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_tax = serializers.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_surcharge = serializers.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now=True)




class OrderItem(serializers.Model):
    order = serializers.ForeignKey(Order, related_name="items", on_delete=serializers.CASCADE)
    item_id = serializers.CharField(max_length=50)
    amount = serializers.IntegerField()


    


class Locations(serializers.Model):
    id = serializers.AutoField(primary_key=True)
    warehouse_id = serializers.IntegerField()
    code = serializers.CharField(max_length=5)
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now=True)

    