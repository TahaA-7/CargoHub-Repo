#from django.shortcuts import render
from rest_framework.decorators import api_view#, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import Clients, Warehouses, Suppliers, Shipments, Orders, Locations, Items, Item_types, Item_groups, Item_lines, Transfers, Inventories, Pseudo_models
from .serializers import ClientSerializer, WarehousesSerializer, SuppliersSerializer, ShipmentsSerializer, OrdersSerializer, OrderItemSerializer, LocationsSerializer, ItemsSerializer, ItemLinesSerializer, ItemGroupsSerializer, ItemTypesSerializer, TransfersSerializer, InventoriesSerializer, PseudoModelsSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import authentication_classes, permission_classes


# Firstly you will see a few generic methods to handle HTTP requests. Later you will see the actual implementation per endpoint
def update_object(model, pk, serializer_class, data):
    try:
        obj = model.objects.get(pk=pk)
    except model.DoesNotExist:
        return Response({"detail": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = serializer_class(obj, data=data, partial=True)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": f"Update failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def post_object(model, serializer_class, data):    
    serializer = serializer_class(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_objects(model, serializer_class):
    objects = model.objects.all()
    serializer = serializer_class(objects, many=True)
    return Response(serializer.data)

def get_object(model, pk, serializer_class):
    try:
        obj = model.objects.get(pk=pk)
    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = serializer_class(obj)
    return Response(serializer.data)

def delete_object(model, pk):
    try:
        obj = model.objects.get(pk=pk)
        obj.delete()
        return Response({'detail': 'Object deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except model.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

# def destroy(self, request, *args, **kwargs):
#     instance = self.get_object()
#     self.perform_destroy(instance)
#     return Response(status=status.HTTP_204_NO_CONTENT)

#end of generic methods
############################################################################################


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated])
def client_list(request):
    if request.method == 'GET':
        return get_objects(Clients, ClientSerializer)

    elif request.method == 'POST':
        return post_object(Clients, ClientSerializer, request.data)

@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated])
def client_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Clients, pk)
    elif request.method == 'PUT':
        return update_object(Clients, pk, ClientSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Clients, pk, ClientSerializer)
#
@api_view(['GET', 'POST'])
def warehouse_list(request):
    if request.method == 'GET':
        return get_objects(Warehouses, WarehousesSerializer)
    elif request.method == 'POST':
        return post_object(Warehouses, WarehousesSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def warehouse_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Warehouses, pk)
    elif request.method == 'PUT':
        return update_object(Warehouses, pk, WarehousesSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Warehouses, pk, WarehousesSerializer)




@api_view(['GET', 'POST'])
def inventory_list(request):
    if request.method == 'GET':
        return get_objects(Inventories, InventoriesSerializer)
    elif request.method == 'POST':
        return post_object(Inventories, InventoriesSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def inventory_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Inventories, pk)
    elif request.method == 'PUT':
        return update_object(Inventories, pk, InventoriesSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Inventories, pk, InventoriesSerializer)




@api_view(['GET', 'POST'])
def item_group_list(request):
    if request.method == 'GET':
        return get_objects(Item_groups, ItemGroupsSerializer)
    elif request.method == 'POST':
        return post_object(Item_groups, ItemGroupsSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def item_group_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Item_groups, pk)
    elif request.method == 'PUT':
        return update_object(Item_groups, pk, ItemGroupsSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Item_groups, pk, ItemGroupsSerializer)
    

@api_view(['GET', 'POST'])
def item_lines_list(request):
    if request.method == 'GET':
        return get_objects(Item_lines, ItemLinesSerializer)
    elif request.method == 'POST':
        return post_object(Item_lines, ItemLinesSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def item_lines_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Item_lines, pk)
    elif request.method == 'PUT':
        return update_object(Item_lines, pk, ItemLinesSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Item_lines, pk, ItemLinesSerializer)





@api_view(['GET', 'POST'])
def item_types_list(request):
    if request.method == 'GET':
        return get_objects(Item_types, ItemTypesSerializer)
    elif request.method == 'POST':
        return post_object(Item_types, ItemTypesSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def item_types_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Item_types, pk) 
    elif request.method == 'PUT':
        return update_object(Item_types, pk, ItemTypesSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Item_types, pk, ItemTypesSerializer)





@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        return get_objects(Items, ItemsSerializer)
    elif request.method == 'POST':
        return post_object(Items, ItemsSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def item_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Items, pk)
    elif request.method == 'PUT':
        return update_object(Items, pk, ItemsSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Items, pk, ItemsSerializer)





@api_view(['GET', 'POST'])
def location_list(request):
    if request.method == 'GET':
        return get_objects(Locations, LocationsSerializer)
    elif request.method == 'POST':
        return post_object(Locations, LocationsSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def location_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Locations, pk)
    elif request.method == 'PUT':
        return update_object(Locations, pk, LocationsSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Locations, pk, LocationsSerializer)





@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        return get_objects(Orders, OrdersSerializer)
    elif request.method == 'POST':
        return post_object(Orders, OrdersSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def order_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Orders, pk)
    elif request.method == 'PUT':
        return update_object(Orders, pk, OrdersSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Orders, pk, OrdersSerializer)





@api_view(['GET', 'POST'])
def shipment_list(request):
    if request.method == 'GET':
        return get_objects(Shipments, ShipmentsSerializer)
    elif request.method == 'POST':
        return post_object(Shipments, ShipmentsSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def shipment_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Shipments, pk)
    elif request.method == 'PUT':
        return update_object(Shipments, pk, ShipmentsSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Shipments, pk, ShipmentsSerializer)





@api_view(['GET', 'POST'])
def supplier_list(request):
    if request.method == 'GET':
        return get_objects(Suppliers, SuppliersSerializer)
    elif request.method == 'POST':
        return post_object(Suppliers, SuppliersSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def supplier_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Suppliers, pk)
    elif request.method == 'PUT':
        return update_object(Suppliers, pk, SuppliersSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Suppliers, pk, SuppliersSerializer)





@api_view(['GET', 'POST'])
def transfer_list(request):
    if request.method == 'GET':
        return get_objects(Transfers, TransfersSerializer)
    elif request.method == 'POST':
        return post_object(Transfers, TransfersSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
def transfer_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Transfers, pk)
    elif request.method == 'PUT':
        return update_object(Transfers, pk, TransfersSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Transfers, pk, TransfersSerializer)
    


@api_view(['POST'])
def transfer_commit(request, transfer_id):
    try:
        transfer = get_object_or_404(Transfers, id=transfer_id)

        with transaction.atomic():
            for item in transfer.items.all():
                from_inventory = Inventories.objects.get(
                    item_id=item.item_id, location_id=transfer.transfer_from
                )
                to_inventory = Inventories.objects.get(
                    item_id=item.item_id, location_id=transfer.transfer_to
                )
                from_inventory.total_on_hand -= item.amount
                from_inventory.total_expected = (
                    from_inventory.total_on_hand + from_inventory.total_ordered
                )
                from_inventory.total_available = (
                    from_inventory.total_on_hand - from_inventory.total_allocated
                )
                from_inventory.save()

                to_inventory.total_on_hand += item.amount
                to_inventory.total_expected = (
                    to_inventory.total_on_hand + to_inventory.total_ordered
                )
                to_inventory.total_available = (
                    to_inventory.total_on_hand - to_inventory.total_allocated
                )
                to_inventory.save()
        
        return Response(
            {"message": "Transfer committed successfully."},
            status=status.HTTP_200_OK
        )

    except Inventories.DoesNotExist:
        return Response(
            {"error": "Inventory record not found for the given item/location."},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response(
            {"error": f"An error occurred: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST
        )



@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def pseudo_models_list(request):
    if request.method == 'GET':
        return get_objects(Pseudo_models, PseudoModelsSerializer)
    elif request.method == 'POST':
        return post_object(Pseudo_models, PseudoModelsSerializer, request.data)

@api_view(['DELETE', 'PUT', 'GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def pseudo_models_detail(request, pk):
    if request.method == 'DELETE':
        return delete_object(Pseudo_models, pk)
    elif request.method == 'PUT':
        return update_object(Pseudo_models, pk, PseudoModelsSerializer, request.data)
    elif request.method == 'GET':
        return get_object(Pseudo_models, pk, PseudoModelsSerializer)


@api_view(['GET'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)