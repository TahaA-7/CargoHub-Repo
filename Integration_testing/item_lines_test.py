import requests
import time

BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

def test_get_item_lines():
    response = requests.get(f"{BASE_URL}/item_lines", headers=HEADER)
    assert response.status_code == 200  # SUCCESS


def test_put_item_lines():
    get_item_line = requests.get(f"{BASE_URL}/item_lines/93", headers=HEADER)
    item_line = get_item_line.json()
    old_updated_at = item_line['updated_at']
    
    item_line['name'] = "Test item line updated"

    response = requests.put(f"{BASE_URL}/item_lines/93", headers=HEADER, json=item_line)
    
    assert response.status_code == 200  # SUCCESS

    get_item_line2 = requests.get(f"{BASE_URL}/item_lines/93", headers=HEADER)
    item_line2 = get_item_line2.json()
    new_updated_at = item_line2['updated_at']

    assert old_updated_at != new_updated_at  # SUCCESS

def test_get_put_item_lines():
    get_item_line = requests.get(f"{BASE_URL}/item_lines/93", headers=HEADER)
    assert get_item_line.status_code == 200  # SUCCESS

    item_line = get_item_line.json()
    item_line['name'] = "Test item line updated"

    response = requests.put(f"{BASE_URL}/item_lines/93", headers=HEADER, json=item_line)
    assert response.status_code == 200  # SUCCESS

def test_delete_item_lines():
    response = requests.delete(f"{BASE_URL}/item_lines/92", headers=HEADER)
    assert response.status_code == 200  # SUCCESS

def test_get_deleted_item_lines():
    requests.delete(f"{BASE_URL}/item_lines/92", headers=HEADER)

    response = requests.get(f"{BASE_URL}/item_lines/92", headers=HEADER)
    assert response.status_code == 200  # SUCCESS

