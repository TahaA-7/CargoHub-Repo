import requests

BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

def test_get_item_groups():
    response = requests.get(f"{BASE_URL}/item_groups", headers=HEADER)
    assert response.status_code == 200  # SUCCESS


def test_put_item_groups():
    get_item_group = requests.get(f"{BASE_URL}/item_groups/97", headers=HEADER)

    item_group = get_item_group.json()
    old_updated_at = item_group['updated_at']
    
    item_group['name'] = "Test item group updated"

    response = requests.put(f"{BASE_URL}/item_groups/97", headers=HEADER, json=item_group)
    
    assert response.status_code == 200  # SUCCESS

    get_item_group2 = requests.get(f"{BASE_URL}/item_groups/97", headers=HEADER)
    item_group2 = get_item_group2.json()
    new_updated_at = item_group2['updated_at']

    assert old_updated_at != new_updated_at  # SUCCESS



def test_delete_item_groups():
    response = requests.delete(f"{BASE_URL}/item_groups/99", headers=HEADER)
    assert response.status_code == 200  # SUCCESS
    


#def test_get_deleted_item_groups():
#    
#    response = requests.get(f"{BASE_URL}/item_groups/99", headers=HEADER)
#    assert response.status_code == 404  # SUCCESS
