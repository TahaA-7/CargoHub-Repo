from django.test import TestCase
from api.serializers import *
# from rest_framework.test import APIClient
from datetime import datetime
from django.utils.timezone import make_aware
# from django.core.exceptions import BadRequest

# NOTES: cd to `cargohub` and run with `python manage.py test api.tests.unittests.test_unit_test_serializers`

class OrdersSerializerUnitTest(TestCase):
    def setUp(self):
        # self.order = APIClient()

        self.test_order_dict = {
            # "id": missing! expecting this to be automatically made.
            "source_id": 1, # Expected valid
            "order_date": "2012-12-04 10:44:27",    # Expected valid<s>, but warning<s> cannot test this with serializers, only models
            "request_date": "2012-12-05",   # Expected error
            "reference": "test1",   # Expected valid
            "reference_extra": "just some text since this is supposed to be a text field...",   # Expected valid
            "order_status": "A" * 51,  # Expected error (max_length=50 assumed)
            "notes": 1,     # Excpected error
            "shipping_notes": "The one above and below should raise an error...",   # Expected valid
            "picking_notes": 1.1,   # Expected error
            "warehouse_id": 2.1,    # Expected error
            "ship_to": None,    # Expected valid
            "bill_to": 4,   # Expected valid
            "shipment_id": None,  # Expected valid?
            "total_amount": 0,  # Expected valid?
            "total_discount": 0.0,  # Expected valid
            "total_tax": 1, # Expected error
            "total_surcharge": "12",    # Expected error
            "created_at": make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),    # Expected valid
            # "updated_at": missing!    # Expected ?
            }

    def test_serializer_validation(self):
        serializer = OrdersSerializer(data=self.test_order_dict)
        self.assertFalse(serializer.is_valid())  # Expecting some fields to fail validation
        errors = serializer.errors

        # Validating the fields
        self.assertNotIn("id", errors)
        self.assertNotIn("source_id", errors)
        self.assertNotIn("order_date", errors)
        # self.assertIn("request_date", errors)
            # FAILURE: Expected an error because of incomplete format, but it supports `%Y-%m-%d` format
        self.assertIn("order_status", errors)  # Exceeds max_length
        # self.assertIn("notes", errors)
            # FAILURE: Expected an error because the value was an int, but apparently Textfield accepts ints and converts them to a string
        # self.assertIn("picking_notes", errors)  # Invalid type
            # FAILURE: Same reason as with `notes`. Apparently floats/decimals get automatically converted...
        self.assertIn("warehouse_id", errors)  # Invalid type
        self.assertNotIn("ship_to", errors)
        self.assertNotIn("bill_to", errors)
        self.assertNotIn("shipment_id", errors)
        self.assertNotIn("total_amount", errors)
        self.assertNotIn("total_discount", errors)
        # self.assertIn("total_tax", errors)
            # FAILURE: ints get auto-converted to a float/decimal
        # self.assertIn("total_surcharge", errors)  # Invalid type
            # FAILURE: strings when `isdigit()` get auto-converted to a float/decimal
        self.assertNotIn("total_amount", errors)
        self.assertNotIn("created_at", errors)
        self.assertNotIn("updated_at", errors)  # NOTE: non-existent model fields cannot be tested with serializers, only with models

    def test_valid_order_data(self):
        valid_order_data = self.test_order_dict.copy()
        valid_order_data.update({
            "order_status": "Valid Status",
            "notes": "Valid notes",
            "picking_notes": "Valid picking notes",
            "warehouse_id": 3,
            "total_surcharge": 12.5,
        })

        serializer = OrdersSerializer(data=valid_order_data)
        self.assertTrue(serializer.is_valid())  # Expecting this data to pass validation
        self.assertEqual(serializer.errors, {})  # No validation errors expected

class ClientsSerializerUnitTest(TestCase):
    def setUp(self):
        self.test_client_dict1 = {
            "contact_email": "aapje@banaantje.nl",
            "created_at": "aapje banaantje"
        }
        self.test_client_dict2 = {
            "contact_email": "nonsensical onzin",
            "created_at": "-2012-12-04 10:44:27"
        }
        self.test_client_dict3 = {
            "contact_email": "aapje@banaantje.gorilla",
            "created_at": "100-1-1"
        }

    def test_serializer_validation1(self):
        serializer = ClientSerializer(data=self.test_client_dict1)
        self.assertFalse(serializer.is_valid())  # Expecting some fields to fail validation
        errors = serializer.errors

        self.assertNotIn("contact_email", errors)
        self.assertIn("created_at", errors)

    def test_serializer_validation2(self):
        serializer = ClientSerializer(data=self.test_client_dict2)
        self.assertFalse(serializer.is_valid())  # Expecting some fields to fail validation
        errors = serializer.errors

        self.assertIn("contact_email", errors)
        self.assertIn("created_at", errors)

    def test_serializer_validation3(self):
        serializer = ClientSerializer(data=self.test_client_dict3)
        self.assertFalse(serializer.is_valid())  # Expecting some fields to fail validation
        errors = serializer.errors

        self.assertNotIn("contact_email", errors)    # NOTE: the EmailField only checks regex
        self.assertIn("created_at", errors) # NOTE: yes it is a valid datetime object
