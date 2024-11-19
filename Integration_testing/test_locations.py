import requests

BASE_URL = 'http://localhost:3000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

def test_data_post_location():
    new_location= {
        "id": 3,
        "warehouse_id": 1,
        "code": "A.2.0",
        "name": "Row: A, Rack: 2, Shelf: 0",
        "created_at": "1992-05-15 03:21:32",
        "updated_at": "1992-05-15 03:21:32"
    }

    response = requests.post(f"{BASE_URL}/locations", headers=HEADER, json=new_location)
    assert response.status_code == 201  # SUCCESS


def test_get_posted_location():
    local_new_location= {
        "id": 3,
        "warehouse_id": 1,
        "code": "A.2.0",
        "name": "Row: A, Rack: 2, Shelf: 0",
        "created_at": "1992-05-15 03:21:32",
        "updated_at": "1992-05-15 03:21:32"
    }

    response = requests.get(f"{BASE_URL}/locations/{local_new_location['id']}", headers=HEADER)
    # check if the received data is the same as the data we posted




    assert response.status_code == 200  # SUCCESS
    assert response.json()['id'] == local_new_location['id']




def test_put_location():
    get_location = requests.get(f"{BASE_URL}/locations/3", headers=HEADER)
    location = get_location.json()
    old_updated_at = location['updated_at']
    location['code'] = "changed"

    response = requests.put(f"{BASE_URL}/locations/3", headers=HEADER, json=location)
    
    assert response.status_code == 200  # SUCCESS

    get_location2 = requests.get(f"{BASE_URL}/locations/3", headers=HEADER)
    location2 = get_location2.json()
    new_updated_at = location2['updated_at']

    assert old_updated_at != new_updated_at  # SUCCESS


def test_get_updated_location():
    response = requests.get(f"{BASE_URL}/locations/3", headers=HEADER)
    # check if the received data is the same as the data we posted
    assert response.json()['code'] == "changed"  # SUCCESS


def test_delete_location():

    response = requests.delete(f"{BASE_URL}/locations/3", headers=HEADER)
    assert response.status_code == 200  # SUCCESS

def test_get_deleted_location():

    response = requests.get(f"{BASE_URL}/locations/3", headers=HEADER)

    # print(response.json())
    assert response.json() == None  # SUCCESS


