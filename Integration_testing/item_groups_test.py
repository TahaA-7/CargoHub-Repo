import requests
from django.test import TestCase, Client
from django.urls import reverse

BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}
# THE JSON FILES START OUT AS EMPTY


new_item_group = {
    "id": 999, 
    "name": "Books", 
    "description": "", 
    "created_at": "2021-09-24 18:52:52", 
    "updated_at": "2023-11-06 09:41:37"}

def test_get_item_groups():
    get_response = requests.get(f"{BASE_URL}/item_groups", headers=HEADER)
    item_groups_data = get_response.json()

    get_item_group = requests.get(f"{BASE_URL}/item_groups/999", headers=HEADER)
    assert get_item_group.json() == None

    assert get_response.status_code == 200
    assert item_groups_data != None
    assert len(item_groups_data) == 0

def test_post_item_group():
    post_respose = requests.post(f"{BASE_URL}/item_groups", headers=HEADER, json=new_item_group)

    assert post_respose.status_code == 201
    
    get_response = requests.get(f"{BASE_URL}/item_groups/{new_item_group['id']}", headers=HEADER)
    assert get_response.status_code == 200

    item_group_data = get_response.json()
    assert item_group_data != None

def test_put_item_group():
    get_response = requests.get(f"{BASE_URL}/item_groups/{new_item_group['id']}", headers=HEADER)
    item_group = get_response.json()

    old_updated_at = item_group['updated_at']
    old_description = item_group['description']
    assert item_group['description'] == ""
    item_group['description'] = "The Nine Books"

    put_response = requests.put(f"{BASE_URL}/item_groups/{new_item_group['id']}", headers=HEADER, json=item_group)
    assert put_response.status_code == 200

    get_item_group = requests.get(f"{BASE_URL}/item_groups/{new_item_group['id']}", headers=HEADER)
    assert get_response.status_code == 200

    updated_item_group = get_item_group.json()
    assert updated_item_group['updated_at'] != old_updated_at
    assert updated_item_group['description'] != old_description

def test_delete_item_group():
    get_item_group = requests.get(f"{BASE_URL}/item_groups/{new_item_group['id']}", headers=HEADER)
    item_group = get_item_group.json()
    assert item_group['description'] == "The Nine Books"

    delete_response = requests.delete(f"{BASE_URL}/item_groups/{new_item_group['id']}", headers=HEADER)
    assert delete_response.status_code == 200

def test_get_deleted_item_group():
    get_request = requests.get(f"{BASE_URL}/item_groups/999", headers=HEADER)
    assert get_request.json() == None
