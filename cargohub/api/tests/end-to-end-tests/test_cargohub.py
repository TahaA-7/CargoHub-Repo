from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from datetime import datetime
from django.utils.timezone import make_aware
import sys
import os
import uuid
from django.core.management import call_command

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from api.models import Clients, Inventories, Warehouses, Item_groups, Item_lines, Item_types, Items, Locations, Orders, Shipments, Suppliers, Transfers

# NOTES: cd to `cargohub` and run with `python manage.py test api.tests.end-to-end-tests.test_unit_test_views`

class AuthIntegrationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user and token
        cls.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="testuser@example.com"
        )

        cls.token = Token.objects.create(user=cls.user)

    def setUp(self):

        self.client = APIClient()
        assert isinstance(self.client, APIClient)   # NOTE: due to import issues
        # Authenticate the client for each test
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_auth_required(self):
        # Test without authentication
        self.client.credentials()  # Remove authentication
        response = self.client.get('/api/pseudo_models/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_with_valid_token(self):
        # Test with valid token
        response = self.client.get('/api/pseudo_models/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_nonexistent_endpoint(self):
        # Test nonexistent endpoint with authentication
        response = self.client.get('/api/nonexistent-endpoint/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ClientsCRUDTest(TestCase):
    def setUp(self):

        # Initialize the test client
        self.client = APIClient()

        # Set up initial test data
        self.test_client = Clients.objects.create(
            id=9998,
            name="Raynaud SA",
            address="49, boulevard Arnaude Morel",
            city="Lopez",
            zip_code="97349",
            province="Gelderland",
            country="France",
            contact_name="Theophile Bailly",
            contact_phone="+33 (0)4 67 14 22 66",
            contact_email="marcelverdier@example.org",
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2013-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.test_data = {
            "name": "Raynaud SA",
            "address": "49, boulevard Arnaude Morel",
            "city": "Lopez",
            "zip_code": "97349",
            "province": "Gelderland",
            "country": "France",
            "contact_name": "Theophile Bailly",
            "contact_phone": "+33 (0)4 67 14 22 66",
            "contact_email": "marcelverdier@example.org",
        },
        self.updated_data = {
            "name": "Updated Test Item",
            "address": "This is an updated test description."
        }
        self.api_key = "a1b2c3d4e5"
        self.headers = {"HTTP_AUTHORIZATION" : self.api_key}

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/clients', follow=True, format='json', **self.headers)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.client.get(f'/api/clients/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['name'], self.test_data[0]['name'])
        self.assertEqual(read_response.data['address'], self.test_data[0]['address'])

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the client data"):
            update_response = self.client.put(f'/api/clients/9998/', self.updated_data, format='json', **self.headers)
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['name'], self.updated_data['name'])
            self.assertEqual(update_response.data['address'], self.updated_data['address'])

        # VERIFY
        with self.subTest("Verify the updated client data"):
            verify_get_response = self.client.get(f'/api/clients/9998/', format='json', **self.headers)
            self.assertEqual(verify_get_response.data["address"], self.updated_data['address'])


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the client data"):
            delete_response = self.client.delete(f'/api/clients/9998/', format='json', **self.headers)
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.client.get(f'/api/clients/9998/', format='json', **self.headers)
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class InventoriesCRUDTest(TestCase):
    def setUp(self):
        # Initialize the test inventory
        self.inventory = APIClient()

        # Set up initial test data
        self.test_inventory_data = Inventories.objects.create(
            id=9998,
            item_id="P009998",
            description="test",
            item_reference="LopezDeDerde",
            locations=[102, 203123, 2310],
            total_on_hand=12,
            total_expected=12,
            total_ordered=12,
            total_allocated=123,
            total_available=123,
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2013-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "description": "This is an updated test description."
        }

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/inventories', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.inventory.get(f'/api/inventories/{self.test_inventory_data.id}/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['description'], self.test_inventory_data.description)


    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the inventory data"):
            get_response = self.inventory.get(f'/api/inventories/{self.test_inventory_data.id}/', self.updated_data, format='json')
            old_updated_at = get_response.data['updated_at']
            update_response = self.inventory.put(f'/api/inventories/{self.test_inventory_data.id}/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertNotEqual(update_response.data['updated_at'], old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated inventory data"):
            verify_get_response = self.inventory.get(f'/api/inventories/{self.test_inventory_data.id}/', format='json')
            self.assertEqual(verify_get_response.data['description'], self.updated_data['description'])


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the inventory data"):
            delete_response = self.inventory.delete(f'/api/inventories/{self.test_inventory_data.id}/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.inventory.get(f'/api/inventories/{self.test_inventory_data.id}/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class Item_GroupsCRUDTest(TestCase):
    def setUp(self):
        # Initialize the test item_group
        self.item_group = APIClient()

        # Set up initial test data
        self.test_item_group_data = Item_groups.objects.create(
            id=9998,
            description="Test Item Group",
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2013-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "description": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_group_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/item_groups', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        # print(get_response.data)
        read_response = self.item_group.get(f'/api/item_groups/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['description'], self.test_item_group_data.description)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_group_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item_group data"):
            update_response = self.item_group.put(f'/api/item_groups/9998/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['description'], self.updated_data['description'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item_group data"):
            verify_get_response = self.item_group.get(f'/api/item_groups/9998/', format='json')
            self.assertEqual(verify_get_response.data["description"], self.updated_data['description'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item_group data"):
            delete_response = self.item_group.delete(f'/api/item_groups/9998/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.item_group.get(f'/api/item_groups/9998/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class Item_linesCRUDTest(TestCase):
    def setUp(self):
        # Initialize the test item_line
        self.item_line = APIClient()

        # Set up initial test data
        self.test_item_line_data = Item_lines.objects.create(
            id=9998,
            description="Test Item Line",
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2013-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "description": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_line_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/item_lines', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.item_line.get(f'/api/item_lines/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['description'], self.test_item_line_data.description)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_line_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item_line data"):
            update_response = self.item_line.put(f'/api/item_lines/9998/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['description'], self.updated_data['description'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item_line data"):
            verify_get_response = self.item_line.get(f'/api/item_lines/9998/', format='json')
            self.assertEqual(verify_get_response.data["description"], self.updated_data['description'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item_line data"):
            delete_response = self.item_line.delete(f'/api/item_lines/9998/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.item_line.get(f'/api/item_lines/9998/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class Item_typesCRUDTest(TestCase):
    def setUp(self):
        # Initialize the test item_type
        self.item_type = APIClient()

        # Set up initial test data
        self.test_item_type_data = Item_types.objects.create(
            id=9998,
            description="Test Item Type",
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2013-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "description": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_type_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/item_types', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.item_type.get(f'/api/item_types/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['description'], self.test_item_type_data.description)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_type_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item_type data"):
            update_response = self.item_type.put(f'/api/item_types/9998/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['description'], self.updated_data['description'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item_type data"):
            verify_get_response = self.item_type.get(f'/api/item_types/9998/', format='json')
            self.assertEqual(verify_get_response.data["description"], self.updated_data['description'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item_type data"):
            delete_response = self.item_type.delete(f'/api/item_types/9998/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.item_type.get(f'/api/item_types/9998/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class ItemsCRUDTest(TestCase):
    def setUp(self):
        # Initialize the test item
        self.item = APIClient()
        # self.uuid = uuid.uuid4()

        # Set up initial test data
        self.test_item_data = Items.objects.create(
            # id=str(self.uuid),
            # id = "c303282d-f2e6-46ca-a04a-35d3d873712d",
            uid = 9998,      # NOTE: THE REASON AN INT IS USED HERE IS BECAUSE THE REQUEST AUTOMATICALLY TRANSLATES IT TO (U)UID
            code="testCode",
            description="Test Item",
            short_description = "test",
            upc_code = "65354947122",
            model_number = "test-4th-TEST",
            commodity_code = "TEST-4th",
            item_line = 9,
            item_group = 13,
            item_type = 124,
            unit_purchase_quantity = 2,
            unit_order_quantity = 10,
            pack_order_quantity = 5,
            supplier_id = 5,
            supplier_code = "SUP555",
            supplier_part_number = "E-86805-TEST",
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2013-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )
        # self.item_id = self.test_item_data.id

        self.updated_data = {
            "description": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/items', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.item.get(f'/api/items/{self.test_item_data.uid}/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['description'], self.test_item_data.description)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item data"):
            update_response = self.item.put(f'/api/items/{self.test_item_data.uid}/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['description'], self.updated_data['description'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item data"):
            verify_get_response = self.item.get(f'/api/items/{self.test_item_data.uid}/', format='json')
            self.assertEqual(verify_get_response.data["description"], self.updated_data['description'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item data"):
            delete_response = self.item.delete(f'/api/items/{self.test_item_data.uid}/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.item.get(f'/api/items/{self.test_item_data.uid}/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class LocationsCRUDTest(TestCase):
    def setUp(self):
        # Initialize the test item
        self.location = APIClient()

        # Set up initial test data
        self.test_item_data = Locations.objects.create(
            id=9998,
            warehouse_id=998,
            code="Test code",
            name = "test",
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2013-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "name": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/locations', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.location.get(f'/api/locations/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['name'], self.test_item_data.name)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item data"):
            update_response = self.location.put(f'/api/locations/9998/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['name'], self.updated_data['name'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item data"):
            verify_get_response = self.location.get(f'/api/locations/9998/', format='json')
            self.assertEqual(verify_get_response.data["name"], self.updated_data['name'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item data"):
            delete_response = self.location.delete(f'/api/locations/9998/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.location.get(f'/api/locations/9998/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class OrdersCRUDTest(TestCase):
    def setUp(self):
        # Initialize the test item
        self.order = APIClient()

        # Set up initial test data
        self.test_item_data = Orders.objects.create(
            id=9998,
            source_id = 12,
            order_date = make_aware(datetime.strptime("2013-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            request_date = make_aware(datetime.strptime("2013-12-05 10:44:27", "%Y-%m-%d %H:%M:%S")),
            reference = "ORD09998",
            reference_extra = "as a test",
            order_status = "testing...",
            notes = "This is a test",
            shipping_notes = "For testing purposes",
            picking_notes = "With tests",
            warehouse_id = 14,
            ship_to = 10,
            bill_to = 99,
            shipment_id = 31,
            total_amount = 111.12,
            total_discount = 13.14,
            total_tax = 14.15,
            total_surcharge = 28.3,
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2014-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "notes": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/orders', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.order.get(f'/api/orders/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['notes'], self.test_item_data.notes)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item data"):
            update_response = self.order.put(f'/api/orders/9998/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['notes'], self.updated_data['notes'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item data"):
            verify_get_response = self.order.get(f'/api/orders/9998/', format='json')
            self.assertEqual(verify_get_response.data["notes"], self.updated_data['notes'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item data"):
            delete_response = self.order.delete(f'/api/orders/9998/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.order.get(f'/api/orders/9998/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class ShipmentsCRUDTest(TestCase):        # NOTE: Somehow selects `api_shipments` instead of shipments
    def setUp(self):
        # Initialize the test item
        self.shipment = APIClient()

        # Set up initial test data
        self.test_item_data = Shipments.objects.create(
            id=98765,
            order_id = 31,
            source_id = 14,
            order_date = make_aware(datetime.strptime("2013-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            request_date = make_aware(datetime.strptime("2013-12-05 10:44:27", "%Y-%m-%d %H:%M:%S")),
            shipment_date = make_aware(datetime.strptime("2013-12-06 10:44:27", "%Y-%m-%d %H:%M:%S")),
            shipment_type = "test type",
            notes = "This is a test.",
            carrier_code = "TST",
            carrier_description = "We only do testing.",
            service_code = "Testest",
            payment_type = "ByTests",
            transfer_mode = "ThroughTests",
            total_package_count = 123,
            total_package_weight = 194.2,
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2014-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "notes": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/shipments', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.shipment.get(f'/api/shipments/{self.test_item_data.id}/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['notes'], self.test_item_data.notes)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item data"):
            update_response = self.shipment.put(f'/api/shipments/{self.test_item_data.id}/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['notes'], self.updated_data['notes'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item data"):
            verify_get_response = self.shipment.get(f'/api/shipments/{self.test_item_data.id}/', format='json')
            self.assertEqual(verify_get_response.data["notes"], self.updated_data['notes'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item data"):
            delete_response = self.shipment.delete(f'/api/shipments/{self.test_item_data.id}/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.shipment.get(f'/api/shipments/{self.test_item_data.id}/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class SuppliersCRUDTest(TestCase):        # NOTE: Same issue as with `Shipments`
    def setUp(self):
        # Initialize the test item
        self.supplier = APIClient()

        # Set up initial test data
        self.test_item_data = Suppliers.objects.create(
            id=9998,
            code = "TEST9998",
            name = "Test",
            address = "333 Teststraat 3",
            address_extra = "T. 9998",
            city = "Test City",
            zip_code = "12451",
            province = "Testyland",
            country = "New Testia",
            contact_name = "Dexter T. Test",
            phonenumber = "06123456789",
            reference = "TEST-SUP9998",
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2014-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "name": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/suppliers', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.supplier.get(f'/api/suppliers/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['name'], self.test_item_data.name)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item data"):
            update_response = self.supplier.put(f'/api/suppliers/9998/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['name'], self.updated_data['name'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item data"):
            verify_get_response = self.supplier.get(f'/api/suppliers/9998/', format='json')
            self.assertEqual(verify_get_response.data["name"], self.updated_data['name'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item data"):
            delete_response = self.supplier.delete(f'/api/suppliers/9998/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.supplier.get(f'/api/suppliers/9998/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class TransfersCRUDTest(TestCase):
    def setUp(self):
        # Initialize the test item
        self.transfer = APIClient()

        # Set up initial test data
        self.test_item_data = Transfers.objects.create(
            id=9998,
            reference = "TR09998",
            transfer_from = None,
            transfer_to = 1234,
            transfer_status = "Testing",
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2014-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "transfer_status": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/transfers', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.transfer.get(f'/api/transfers/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['transfer_status'], self.test_item_data.transfer_status)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item data"):
            update_response = self.transfer.put(f'/api/transfers/9998/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['transfer_status'], self.updated_data['transfer_status'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item data"):
            verify_get_response = self.transfer.get(f'/api/transfers/9998/', format='json')
            self.assertEqual(verify_get_response.data["transfer_status"], self.updated_data['transfer_status'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item data"):
            delete_response = self.transfer.delete(f'/api/transfers/9998/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.transfer.get(f'/api/transfers/9998/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


class WarehousesCRUDTest(TestCase):
    def setUp(self):
        # Initialize the test item
        self.warehouse = APIClient()

        # Set up initial test data
        self.test_item_data = Warehouses.objects.create(
            id=9998,
            code = "TEST9998",
            name = "Test",
            address = "Testlaan 2",
            zip = "3485 TS",
            city = "Testendam",
            province = "Testland",
            country = "New Testia",
            created_at=make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at=make_aware(datetime.strptime("2014-06-05 20:52:22", "%Y-%m-%d %H:%M:%S"))
        )

        self.updated_data = {
            "address": "Updated Test Item"
        }
        self.old_updated_at = self.test_item_data.updated_at

    def test_crud_get(self):
        # READ
        get_response = self.client.get('/api/warehouses', follow=True, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        read_response = self.warehouse.get(f'/api/warehouses/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['address'], self.test_item_data.address)
        self.assertNotEqual(read_response.data['updated_at'], self.test_item_data.updated_at)

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the item data"):
            update_response = self.warehouse.put(f'/api/warehouses/9998/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['address'], self.updated_data['address'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)

        # VERIFY
        with self.subTest("Verify the updated item data"):
            verify_get_response = self.warehouse.get(f'/api/warehouses/9998/', format='json')
            self.assertEqual(verify_get_response.data["address"], self.updated_data['address'])
            self.assertNotEqual(update_response.data['updated_at'], self.old_updated_at)


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the item data"):
            delete_response = self.warehouse.delete(f'/api/warehouses/9998/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.warehouse.get(f'/api/warehouses/9998/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)
