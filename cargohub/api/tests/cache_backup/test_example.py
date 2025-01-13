from django.test import TestCase
from django.test import TransactionTestCase
# from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Clients
from django.utils.timezone import now
# from django.db import connection

class PersistentDataTests(TestCase):
    @classmethod
    def setUp(cls):
        cls.item1 = Clients.objects.create(
            id= 9999,
            name= "Raynaud SA",
            address= "49, boulevard Arnaude Morel",
            city= "Lopez",
            zip_code= "97349",
            province= "",
            country= "France",
            contact_name= "Theophile Bailly",
            contact_phone= "+33 (0)4 67 14 22 66",
            contact_email= "marcelverdier@example.org",
            created_at= "2012-12-04 10:44:27",
            updated_at= "2013-06-05 20:52:22"
        )
        cls.api_key = "a1b2c3d4e5"
        cls.headers = {"HTTP_AUTHORIZATION" : cls.api_key}

    # def test_persisted_data(self):
    #     self.assertEqual(Clients.objects.count(), 1)

    # def test_data_still_exists(self):
    #     self.assertEqual(Clients.objects.first().name, "Raynaud SA")

    def test_get(self):
        get_response = self.client.get(f'/api/clients/9999', follow=True, **self.headers)
        self.assertEqual(get_response.status_code, 200)
        self.assertIn(self.item1.name, get_response.content.decode())

    def test_client_post_by_get(self):
        get_response2 = self.client.get(f'/api/clients/{Clients.objects.first().id}', follow=True, **self.headers)
        self.assertEqual(get_response2.status_code, 200)

    def test_client_put(self):
        get_response = self.client.get(f'/api/clients/{self.item1.id}', follow=True, **self.headers)
        client = get_response.json()

        old_updated_at = client['updated_at']
        old_country = client['country']

        self.assertEqual(old_country, 'France')

        updated_client_data = {
            'country': 'French Guiana',
            'updated_at': now().isoformat()
        }

        client_obj = Clients.objects.get(id=self.item1.id)
        client_obj.country = 'French Guiana'
        client_obj.save()
        put_response = self.client.put(
            f'/api/clients/{self.item1.id}', follow=True, data=updated_client_data, content_type='application/json', **self.headers)
        self.assertEqual(put_response.status_code, 200)
        # client_obj.save()

        updated_client = Clients.objects.get(id=self.item1.id)
        self.assertNotEqual(old_updated_at, updated_client.updated_at)
        self.assertNotEqual(old_country, updated_client.country)  # `updated_at` got updated but not this one
        self.assertEqual(updated_client.country, 'French Guiana')

    def test_client_delete(self):
        client = self.client.get(f'/api/clients/{self.item1.id}', follow=True, **self.headers).json()
        self.assertEqual(client['country'], 'French Guiana')

        delete_response = self.client.delete(f'/api/clients/{self.item1.id}', follow=True, **self.headers)
        self.assertEqual(delete_response.status_code, 200)



        deleted_client = self.client.get(f'/api/clients/{self.item1.id}', follow=True, **self.headers)
        self.assertEqual(deleted_client.status_code, 200)
