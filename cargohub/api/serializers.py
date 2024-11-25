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


class InventorySerializer(serializers.ModelSerializer):
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


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.AutoField(primary_key=True)
    name = serializers.CharField(max_length=255)
    description = serializers.TextField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class Item_line(serializers.Model):
    id = serializers.AutoField(primary_key=True)
    name = serializers.CharField(max_length=255)
    description = serializers.TextField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def __str__(self):
        return self.name
    
class Item_typeSerializer(serializers.Model):
    id = serializers.AutoField(primary_key=True)
    name = serializers.CharField(max_length=255)
    description = serializers.TextField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class Item_groupsSerializer(serializers.Model):
    id = serializers.AutoField(primary_key=True)  
    name = serializers.CharField(max_length=255)
    description = serializers.TextField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()