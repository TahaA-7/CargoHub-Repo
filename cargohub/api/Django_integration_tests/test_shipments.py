from django.test import TestCase
from cargohub.api.models import Shipments
from datetime import datetime



class ShipmentsIntegrationTests(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Populate test database with data
        cls.shipment1 = Shipments.objects.create(id = 1,name="Shipment1", description="Description1", created_at = datetime.now(), updated_at = datetime.now())
        cls.shipment2 = Shipments.objects.create(id = 2, name="Shipment2", description="Description2", created_at = datetime.now(), updated_at = datetime.now())

    
    def test_get_shipment(self):
        response = self.client.get('/shipments/1')
        self.assertEqual(response.status_code, 200)