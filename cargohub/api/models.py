from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
# class Base(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField(auto_now=True)

# class Cliens(Base):
#     id = Base.id


class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    # contact = models.OneToOneField(Contact, on_delete=models.CASCADE, related_name="client")
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class ClientContact(models.Model):
#     client_contact = models.ForeignKey(Clients, related_name="items", on_delete=models.CASCADE)
#     contact_name = models.CharField(max_length=255)
#     contact_phone = models.CharField(max_length=50)
#     contact_email = models.EmailField()

#     def __str__(self):
#         return self.contact_name + " |\n" + self.contact_phone + " |\n" + self.contact_email + " |\n"
    

class Inventories(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.CharField(max_length=255)
    description = models.TextField()
    item_reference = models.CharField(max_length=100)
    locations = models.JSONField()  # MIGHT cause problems...
    total_on_hand = models.IntegerField(default=0)
    total_expected = models.IntegerField(default=0)
    total_ordered = models.IntegerField(default=0)
    total_allocated = models.IntegerField(default=0)
    total_available = models.IntegerField(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Item {self.item_id}: {self.description}"

    class Meta:
        db_table = 'api_inventories'


# class Item(models.Model):
#     item_id = models.AutoField(primary_key=True)
#     amount = models.IntegerField(default=0)
    

class Items(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.CharField(max_length=255)
    upc_code = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    commodity_code = models.CharField(max_length=255)
    item_line = models.IntegerField(default=0)
    item_group = models.IntegerField(default=0)
    item_type = models.IntegerField(default=0)
    unit_purchase_quantity = models.IntegerField(default=0)
    unit_order_quantity = models.IntegerField(default=0)
    pack_order_quantity = models.IntegerField(default=0)
    supplier_id = models.IntegerField(default=0)
    supplier_code = models.CharField(max_length=255)
    supplier_part_number = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id + "   " + self.code


class Item_lines(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Item_types(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk:  # Object is being created
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Item_groups(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Warehouses(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    address = models.TextField()
    zip = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    # contact = models.OneToOneField(Contact, on_delete=models.CASCADE, related_name="warehouse")
    # contact_name = models.CharField(max_length=255)
    # contact_phone = models.CharField(max_length=50)
    # contact_email = models.EmailField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WarehouseContact(models.Model):
    warehouse_contact = models.ForeignKey(Warehouses, related_name="items", on_delete=models.CASCADE, default=None)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField()

    def __str__(self):
        return self.contact_name + " |\n" + self.contact_phone + " |\n" + self.contact_email + " |\n"
    

class Suppliers(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.TextField()
    address_extra = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=50)
    reference = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Shipments(models.Model): 
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    source_id = models.IntegerField(default=0)  # ?
    order_date = models.DateField()
    request_date = models.DateField()
    shipment_date = models.DateField()
    shipment_type = models.CharField(max_length=20)
    notes = models.TextField()
    carrier_code = models.CharField(max_length=20)
    carrier_description = models.TextField()
    service_code = models.CharField(max_length=20, default=None)
    payment_type = models.CharField(max_length=20)
    transfer_mode = models.CharField(max_length=20)
    total_package_count = models.IntegerField(default=0)
    total_package_weight = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    # items = models.JSONField()

    def __str__(self):
        return self.id + " " + self.notes

    class Meta:
        db_table = 'api_shipments'


class ShipmentItem(models.Model):
    id = models.AutoField(primary_key=True)
    shipment_id = models.ForeignKey(Shipments, related_name="items", on_delete=models.CASCADE)
    item_id = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    

class Transfers(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=255)
    transfer_from = models.CharField(max_length=255, null=True)
    transfer_to = models.CharField(max_length=6, null=True)
    transfer_status = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    # items = models.JSONField()

    def __str__(self):
        return self.reference


class TransferItem(models.Model):
    id = models.AutoField(primary_key=True)
    transfer_item = models.ForeignKey(Transfers, related_name="items", on_delete=models.CASCADE)
    item_id = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    source_id = models.IntegerField()  # ?
    order_date = models.DateTimeField()
    request_date = models.DateTimeField()
    reference = models.CharField(max_length=255)
    reference_extra = models.TextField(blank=True, null=True)
    order_status = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    shipping_notes = models.TextField(blank=True, null=True)
    picking_notes = models.TextField(blank=True, null=True)
    warehouse_id = models.IntegerField()
    ship_to = models.IntegerField(null=True, blank=True)
    bill_to = models.IntegerField(null=True, blank=True)
    shipment_id = models.IntegerField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_surcharge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # items = models.JSONField()

    def __str__(self):
        return f"Order {self.reference} - {self.order_status}"


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, related_name="items", on_delete=models.CASCADE)
    item_id = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"Item {self.item_id} (Amount: {self.amount})"


class Locations(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse_id = models.IntegerField()
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Pseudo_models(models.Model):
    id = models.AutoField(primary_key=True)
    pseudonym = models.CharField(max_length=255)
    pseudology = models.TextField()
