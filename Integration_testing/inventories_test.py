import requests

BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}
# THE JSON FILES START OUT AS EMPTY


new_inventory = {
    "id": 420, 
    "item_id": "P000420", 
    "description": "Monitored non-volatile orchestration", 
    "item_reference": "MCs34615a", 
    "locations": [30146, 30295, 22284, 22228, 1857, 1613, 7407, 7496, 22421, 22593, 24138, 15318, 15345], 
    "total_on_hand": 197, 
    "total_expected": 0, 
    "total_ordered": 97, 
    "total_allocated": 0, 
    "total_available": 100, 
    "created_at": "2013-12-18 05:07:59", 
    "updated_at": "2016-08-19 17:55:22"}


def test_get_inventories():    
    get_response = requests.get(f"{BASE_URL}/inventories", headers=HEADER)
    inventorys_data = get_response.json()

    get_inventory = requests.get(f"{BASE_URL}/inventories/1", headers=HEADER)
    assert get_inventory.json() == None

    assert get_response.status_code == 200
    assert inventorys_data != None
    assert len(inventorys_data) == 0

def test_post_inventory():
    post_respose = requests.post(f"{BASE_URL}/inventories", headers=HEADER, json=new_inventory)

    assert post_respose.status_code == 201
    
    get_response = requests.get(f"{BASE_URL}/inventories/{new_inventory['id']}", headers=HEADER)
    assert get_response.status_code == 200

    inventory_data = get_response.json()
    assert inventory_data != None

def test_put_inventory():
    get_response = requests.get(f"{BASE_URL}/inventories/{new_inventory['id']}", headers=HEADER)
    inventory = get_response.json()

    old_updated_at = inventory['updated_at']
    old_locations = inventory['locations']
    inventory['locations'] = [1234, 30295, 22284, 22228, 1245, 1613, 7407, 8001, 22421, 22593, 24138, 15318, 15345]

    put_response = requests.put(f"{BASE_URL}/inventories/{new_inventory['id']}", headers=HEADER, json=inventory)
    assert put_response.status_code == 200

    get_inventory = requests.get(f"{BASE_URL}/inventories/{new_inventory['id']}", headers=HEADER)
    assert get_response.status_code == 200

    updated_locations = get_inventory.json()
    assert updated_locations['updated_at'] != old_updated_at
    assert updated_locations['locations'] != old_locations

def test_delete_inventory():
    get_inventory = requests.get(f"{BASE_URL}/inventories/{new_inventory['id']}", headers=HEADER)
    inventory = get_inventory.json()
    assert inventory['locations'] == [1234, 30295, 22284, 22228, 1245, 1613, 7407, 8001, 22421, 22593, 24138, 15318, 15345]

    delete_response = requests.delete(f"{BASE_URL}/inventories/{new_inventory['id']}", headers=HEADER)
    assert delete_response.status_code == 200

def test_get_deleted_inventory():
    get_request = requests.get(f"{BASE_URL}/inventories/420", headers=HEADER)
    assert get_request.json() == None

# SUCCES
