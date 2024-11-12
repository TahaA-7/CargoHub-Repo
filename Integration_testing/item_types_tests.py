import requests

BASE_URL = 'http://localhost:3000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}


def test_get_item_types():
    response = requests.get(f"{BASE_URL}/item_types", headers=HEADER)
    assert response.status_code == 200  # SUCCESS


def test_put_item_types():
    get_item_type = requests.get(f"{BASE_URL}/item_types/98", headers=HEADER)
    item_type = get_item_type.json()
    old_updated_at = item_type['updated_at']
    
    item_type['name'] = "Test item type updated"

    response = requests.put(f"{BASE_URL}/item_types/98", headers=HEADER, json=item_type)
    
    assert response.status_code == 200  # SUCCESS

    get_item_type2 = requests.get(f"{BASE_URL}/item_types/98", headers=HEADER)
    item_type2 = get_item_type2.json()
    new_updated_at = item_type2['updated_at']

    assert old_updated_at != new_updated_at  # SUCCESS

def test_get_put_item_types():
    get_item_type = requests.get(f"{BASE_URL}/item_types/98", headers=HEADER)
    assert get_item_type.status_code == 200  # SUCCESS

def test_delete_item_types():
    response = requests.delete(f"{BASE_URL}/item_types/99", headers=HEADER)
    assert response.status_code == 200  # SUCCESS


def test_get_deleted_item_types():
    response = requests.get(f"{BASE_URL}/item_types/99", headers=HEADER)
    assert response.status_code == 404  # SUCCESS