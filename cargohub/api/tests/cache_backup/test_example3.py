from django.test import TestCase
from django.test import TransactionTestCase
# from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Locations
from django.utils.timezone import now
# from django.db import connection
from django.db import transaction
from api.tests.persistent_testcase import PersistentTestCase

class PersistentDataTests(PersistentTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.item1 = Locations.objects.create(
            id= 99999,
            warehouse_id= 999,
            code= "H.4.3",
            name= "Row: H, Rack: 4, Shelf: 3",
            created_at= "2012-12-04 10:44:27",
            updated_at= "2013-06-05 20:52:22"
        )
        cls.api_key = "a1b2c3d4e5"
        cls.headers = {"HTTP_AUTHORIZATION" : cls.api_key}

    def test_get(self):
        get_response = self.client.get(f'/api/locations/99999', follow=True, **self.headers)
        self.assertEqual(get_response.status_code, 200)
        self.assertIn(self.item1.name, get_response.content.decode())

    def test_location_put(self):
        get_response = self.client.get(f'/api/locations/{self.item1.id}', follow=True, **self.headers)
        location = get_response.json()

        old_updated_at = location['updated_at']
        old_code = location['code']

        self.assertEqual(old_code, 'H.4.3')

        updated_location_data = {
            'code': 'I.4.3',
            'name': 'Row: I, Rack: 4, Shelf: 3',
            'updated_at': now().isoformat()
        }

        location_obj = Locations.objects.get(id=self.item1.id)
        location_obj.code = 'I.4.3'
        # location_obj.save()
        put_response = self.client.put(
            f'/api/locations/{self.item1.id}', follow=True, data=updated_location_data, content_type='application/json', **self.headers)
        self.assertEqual(put_response.status_code, 200)
        # location_obj.save()

        updated_client = Locations.objects.get(id=self.item1.id)
        self.assertNotEqual(old_updated_at, updated_client.updated_at)

        updated_client.save()

    def test_verify_put(self):
        old_code = 'H.4.3'
        get_response = self.client.get(f'/api/locations/{self.item1.id}', follow=True, **self.headers)
        self.assertNotEqual(old_code, get_response.data['code'])
        self.assertEqual(get_response.data['code'], 'I.4.3')

    def test_location_delete(self):
        delete_response = self.client.delete(f'/api/locations/{self.item1.id}', follow=True, **self.headers)
        self.assertEqual(delete_response.status_code, 200)
        self.item1.save()



        deleted_location = self.client.get(f'/api/locations/{self.item1.id}', follow=True, **self.headers)
        self.assertEqual(deleted_location.status_code, 404)

    @classmethod
    def tearDownClass(cls):
        Locations.objects.all().delete()
        super().tearDownClass()
