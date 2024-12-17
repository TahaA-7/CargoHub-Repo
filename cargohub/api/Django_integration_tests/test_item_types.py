from django.test import TestCase
from cargohub.api.models import Item_types
from datetime import datetime

class ItemTypesIntegrationTests(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Populate test database with data
        cls.item1 = Item_types.objects.create(id = 1,name="Item1", description="Description1", created_at = datetime.now(), updated_at = datetime.now())
        cls.item2 = Item_types.objects.create(id = 2, name="Item2", description="Description2", created_at = datetime.now(), updated_at = datetime.now())

    
    def test_item_type_endpoint(self):
        
        response = self.client.get('/item_types/')  # Replace with your endpoint URL
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.item1.name, response.content.decode())
        self.assertIn(self.item2.name, response.content.decode())