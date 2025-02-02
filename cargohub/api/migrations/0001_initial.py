# Generated by Django 5.1.4 on 2025-01-21 15:29

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_clients',
            },
        ),
        migrations.CreateModel(
            name='Inventories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('item_reference', models.CharField(max_length=100)),
                ('locations', models.JSONField()),
                ('total_on_hand', models.IntegerField(default=0)),
                ('total_expected', models.IntegerField(default=0)),
                ('total_ordered', models.IntegerField(default=0)),
                ('total_allocated', models.IntegerField(default=0)),
                ('total_available', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_inventories',
            },
        ),
        migrations.CreateModel(
            name='Item_groups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_item_groups',
            },
        ),
        migrations.CreateModel(
            name='Item_lines',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_item_lines',
            },
        ),
        migrations.CreateModel(
            name='Item_types',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=255)),
                ('upc_code', models.CharField(max_length=255)),
                ('model_number', models.CharField(max_length=255)),
                ('commodity_code', models.CharField(max_length=255)),
                ('item_line', models.IntegerField(default=0)),
                ('item_group', models.IntegerField(default=0)),
                ('item_type', models.IntegerField(default=0)),
                ('unit_purchase_quantity', models.IntegerField(default=0)),
                ('unit_order_quantity', models.IntegerField(default=0)),
                ('pack_order_quantity', models.IntegerField(default=0)),
                ('supplier_id', models.IntegerField(default=0)),
                ('supplier_code', models.CharField(max_length=255)),
                ('supplier_part_number', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_items',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('warehouse_id', models.IntegerField()),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_locations',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source_id', models.IntegerField()),
                ('order_date', models.DateTimeField()),
                ('request_date', models.DateTimeField()),
                ('reference', models.CharField(max_length=255)),
                ('reference_extra', models.TextField(blank=True, null=True)),
                ('order_status', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('shipping_notes', models.TextField(blank=True, null=True)),
                ('picking_notes', models.TextField(blank=True, null=True)),
                ('warehouse_id', models.IntegerField()),
                ('ship_to', models.IntegerField(blank=True, null=True)),
                ('bill_to', models.IntegerField(blank=True, null=True)),
                ('shipment_id', models.IntegerField(blank=True, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_surcharge', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_orders',
            },
        ),
        migrations.CreateModel(
            name='Pseudo_models',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pseudonym', models.CharField(max_length=255)),
                ('pseudology', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default=0)),
                ('source_id', models.IntegerField(default=0)),
                ('order_date', models.DateField()),
                ('request_date', models.DateField()),
                ('shipment_date', models.DateField()),
                ('shipment_type', models.CharField(max_length=20)),
                ('notes', models.TextField()),
                ('carrier_code', models.CharField(max_length=20)),
                ('carrier_description', models.TextField()),
                ('service_code', models.CharField(default=None, max_length=20)),
                ('payment_type', models.CharField(max_length=20)),
                ('transfer_mode', models.CharField(max_length=20)),
                ('total_package_count', models.IntegerField(default=0)),
                ('total_package_weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_shipments',
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('address_extra', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_suppliers',
            },
        ),
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reference', models.CharField(max_length=255)),
                ('transfer_from', models.CharField(max_length=255, null=True)),
                ('transfer_to', models.CharField(max_length=6, null=True)),
                ('transfer_status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_transfers',
            },
        ),
        migrations.CreateModel(
            name='Warehouses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('zip', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'api_warehouses',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.orders')),
            ],
            options={
                'db_table': 'api_order_items',
            },
        ),
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.CharField(max_length=255)),
                ('amount', models.IntegerField(default=0)),
                ('shipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.shipments')),
            ],
            options={
                'db_table': 'api_shipment_items',
            },
        ),
        migrations.CreateModel(
            name='TransferItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.CharField(max_length=255)),
                ('amount', models.IntegerField(default=0)),
                ('transfer_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.transfers')),
            ],
            options={
                'db_table': 'api_transfer_items',
            },
        ),
        migrations.CreateModel(
            name='WarehouseContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('warehouse_contact', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.warehouses')),
            ],
        ),
    ]
