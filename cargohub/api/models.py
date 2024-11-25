from django.db import models

# Create your models here.
class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
    

class Inventories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
    

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Item_lines(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Item_types(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Item_groups(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Warehouses(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    address = models.TextField()
    zip = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
    


class Suppliers(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=7)
    name = models.CharField(max_length=255)
    address = models.TextField()
    address_extra = models.TextField()
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=50)
    reference = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
    

class Shipments(models.Model): 
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=7)
    name = models.CharField(max_length=255)
    address = models.TextField()
    address_extra = models.TextField()
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=50)
    reference = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
    

class Transfers(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=7)
    transfer_from = models.CharField(max_length=255, null=True)
    transfer_to = models.CharField(max_length=4, null=True)
    transfer_status = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.reference
    

class Orders(models.Model):
    source_id = models.IntegerField()
    order_date = models.DateTimeField()
    request_date = models.DateTimeField()
    reference = models.CharField(max_length=255)
    reference_extra = models.TextField(blank=True, null=True)
    order_status = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    shipping_notes = models.TextField(blank=True, null=True)
    picking_notes = models.TextField(blank=True, null=True)
    warehouse_id = models.IntegerField()
    ship_to = models.TextField(blank=True, null=True)
    bill_to = models.TextField(blank=True, null=True)
    shipment_id = models.IntegerField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_surcharge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.reference} - {self.order_status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, related_name="items", on_delete=models.CASCADE)
    item_id = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"Item {self.item_id} (Amount: {self.amount})"
    


class Locations(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse_id = models.IntegerField()
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
