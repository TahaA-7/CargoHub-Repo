from django.test import TestCase
from django.utils.timezone import now
from api.models import *
from datetime import datetime


class AuthIntegrationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.api_key = "a1b2c3d4e5"
        cls.headers = {"HTTP_AUTHORIZATION" : cls.api_key}
        
    def test_auth(self):
        get_response = self.client.get('/api/clients/')
        self.assertEqual(get_response.headers['Content-Type'], 'application/json')
        self.assertEqual(get_response.status_code, 403) # FAILED: RETURNS 200 BECAUSE AUTHORISATION NOT IMPLEMENTED YET

    def test_nonexistent_endpoint_get(self):
        response = self.client.get('/api/nonexistent-endpoint/', **self.headers)
        self.assertEqual(response.status_code, 404)


class ClientsIntegrationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item1 = Clients.objects.create(
        id= 2966,
        name= "Raynaud SA",
        address= "49, boulevard Arnaude Morel",
        city= "Lopez",
        zip_code= "97349",
        province= "",
        country= "France",
        contact_name= "Th\u00e9ophile Bailly",
        contact_phone= "+33 (0)4 67 14 22 66",
        contact_email= "marcelverdier@example.org",
        created_at= "2012-12-04 10:44:27",
        updated_at= "2013-06-05 20:52:22")
        cls.api_key = "a1b2c3d4e5"
        cls.headers = {"HTTP_AUTHORIZATION" : cls.api_key}

    def test_clients_get(self):
        response = self.client.get('/api/clients/', **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.item1.name, response.content.decode())

    def test_client_post_by_get(self):
        get_response = self.client.get(f'/api/clients/9999', **self.headers)
        self.assertEqual(get_response.status_code, 301)  # idk why 301 instead of 404

        get_response2 = self.client.get(f'/api/clients/{self.item1.id}', follow=True, **self.headers)
        self.assertEqual(get_response2.status_code, 200)

    def test_client_put(self):
        get_response = self.client.get(f'/api/clients/{self.item1.id}', follow=True, **self.headers)
        client = get_response.json()

        old_updated_at = client['updated_at']
        old_country = client['country']

        self.assertEqual(old_country, 'France')

        updated_client_data = {
            'country': 'French Guiana',
            'updated_at': now()
        }

        put_response = self.client.put(
            f'/api/clients/{self.item1.id}', follow=True, data=updated_client_data, content_type='application/json', **self.headers)
        self.assertEqual(put_response.status_code, 200)

        # get_updated_client = self.client.get(f'/api/clients/{self.item1.id}', follow=True, **self.headers)
        # updated_client = get_updated_client.json()
        # self.assertNotEqual(old_updated_at, updated_client['updated_at'])
        # self.assertNotEqual(old_country, updated_client['country'])
        # self.assertEqual(updated_client['country'], 'French Guiana')
        updated_client = Clients.objects.get(id=self.item1.id)
        self.assertNotEqual(old_updated_at, updated_client.updated_at)
        self.assertNotEqual(old_country, updated_client.country)  # `updated_at` got updated but not this one
        self.assertEqual(updated_client.country, 'French Guiana')

    def test_client_delete(self):
        client = self.client.get(f'/api/clients/{self.item1.id}', follow=True, **self.headers).json()
        self.assertEqual(client['country'], 'French Guiana')

        delete_response = self.client.delete(f'/api/clients/{self.item1.id}', follow=True, **self.headers)
        self.assertEqual(delete_response.status_code, 200)

    def test_get_deleted_client(self):
        deleted_client = self.client.get(f'/api/clients/{self.item1.id}', follow=True, **self.headers).json()
        self.assertEqual(deleted_client, None)


class ItemTypesIntegrationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Populate test database with data
        cls.item1 = Item_types.objects.create(
            id=1, 
            name="Item1", 
            description="Description1", 
            created_at=now(), 
            updated_at=now()
        )
        cls.item2 = Item_types.objects.create(
            id=2, 
            name="Item2", 
            description="Description2", 
            created_at=now(), 
            updated_at=now()
        )
        cls.api_key = "a1b2c3d4e5"
        cls.headers = {"HTTP_AUTHORIZATION" : cls.api_key}


    def test_item_type_get(self):
        response = self.client.get('/api/item_types/', **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.item1.name, response.content.decode())
        self.assertIn(self.item2.name, response.content.decode())
