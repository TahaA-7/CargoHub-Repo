# Generated by Django 5.1.3 on 2024-11-19 13:27

import django.db.models.deletion
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
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventories',
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
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Item_groups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Item_lines',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('warehouse_id', models.IntegerField()),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('ship_to', models.TextField(blank=True, null=True)),
                ('bill_to', models.TextField(blank=True, null=True)),
                ('shipment_id', models.IntegerField(blank=True, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_surcharge', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('address_extra', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('address_extra', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reference', models.CharField(max_length=7)),
                ('transfer_from', models.CharField(max_length=255, null=True)),
                ('transfer_to', models.CharField(max_length=4, null=True)),
                ('transfer_status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Warehouses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('zip', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.orders')),
            ],
        ),
    ]
