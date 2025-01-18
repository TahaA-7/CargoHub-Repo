# from rest_framework.test import APITestCase, APIClient
# from api.models import Clients
# from django.contrib.auth.tokens import default_token_generator
# from django.urls import reverse
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from rest_framework import status
# import pdb

# class DeleteAccountViewTestCase(APITestCase):
#     def setUp(self):
#         self.user = Clients.objects.create(
#             id= 2966,
#             name= "Raynaud SA",
#             address= "49, boulevard Arnaude Morel",
#             city= "Lopez",
#             zip_code= "97349",
#             province= "",
#             country= "France",
#             contact_name= "Theophile Bailly",
#             contact_phone= "+33 (0)4 67 14 22 66",
#             contact_email= "marcelverdier@example.org",
#             created_at= "2012-12-04 10:44:27",
#             updated_at= "2013-06-05 20:52:22"
#         )
#         self.client.force_authenticate(user=self.user)

#     def test_delete_account_success(self):
#         delete_response = self.client.delete(f'/api/clients/{self.user.id}', follow=True)
#         self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(delete_response.data['detail'], 'Account deleted successfully.')
#         # Add additional assertions as needed


from django.test import TransactionTestCase
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import *
from datetime import datetime

class clientsCRUDTest(TestCase):
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
            created_at=datetime(2012, 12, 4, 10, 44, 27),
            updated_at=datetime(2013, 6, 5, 20, 52, 22),
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
            "address": "This is an updated test address."
        }

    # def test_crud_post_verify(self):
    #     # CREATE
    #     print("Response Data:", self.test_data)
    #     print(self.test_data[0])
    #     create_response = self.client.post('/api/clients/', self.test_data[0], format='json')
    #     print("Response Data:", create_response.data)  # Debug output
    #     self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
    #     created_id = create_response.data['id']

    def test_crud_get(self):
        # READ
        read_response = self.client.get(f'/api/clients/9998/', format='json')
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(read_response.data['name'], self.test_data[0]['name'])
        self.assertEqual(read_response.data['address'], self.test_data[0]['address'])

    def test_crud_put_with_verification(self):
        # UPDATE
        with self.subTest("Update the client data"):
            update_response = self.client.put(f'/api/clients/9998/', self.updated_data, format='json')
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            self.assertEqual(update_response.data['name'], self.updated_data['name'])
            self.assertEqual(update_response.data['address'], self.updated_data['address'])

        # VERIFY
        with self.subTest("Verify the updated client data"):
            verify_get_response = self.client.get(f'/api/clients/9998/', format='json')
            self.assertEqual(verify_get_response.data["address"], self.updated_data['address'])


    def test_crud_delete_with_verification(self):
        # DELETE
        with self.subTest("Delete the client data"):
            delete_response = self.client.delete(f'/api/clients/9998/', format='json')
            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # VERIFY
        with self.subTest("Delete the data deletion"):
            verify_delete_response = self.client.get(f'/api/clients/9998/', format='json')
            self.assertEqual(verify_delete_response.status_code, status.HTTP_404_NOT_FOUND)


# on 11-01-2025 this one worked but now instead test_example1 ?
