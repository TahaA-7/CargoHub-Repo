import requests

BASE_URL = 'http://localhost:80/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}
# THE JSON FILES START OUT AS EMPTY


new_client =     {
        "id": 2966,
        "name": "Raynaud SA",
        "address": "49, boulevard Arnaude Morel",
        "city": "Lopez",
        "zip_code": "97349",
        "province": None,
        "country": "France",
        "contact_name": "Th\u00e9ophile Bailly",
        "contact_phone": "+33 (0)4 67 14 22 66",
        "contact_email": "marcelverdier@example.org",
        "created_at": "2012-12-04 10:44:27",
        "updated_at": "2013-06-05 20:52:22"
    }

def test_auth():
    get_clients = requests.get(f"{BASE_URL}/clients")
    get_client = requests.get(f"{BASE_URL}/clients/{new_client['id']}")
    assert get_clients.status_code == 401
    assert get_client.status_code == 401
    
    nonexistent_endpoint_get_response = requests.get(f"{BASE_URL}/nonexistent", headers=HEADER)
    assert nonexistent_endpoint_get_response.status_code == 404


def test_get_clients():    
    get_response = requests.get(f"{BASE_URL}/clients", headers=HEADER)
    clients_data = get_response.json()

    get_client = requests.get(f"{BASE_URL}/clients/1", headers=HEADER)
    assert get_client.json() == None

    assert get_response.status_code == 200
    assert clients_data != None
    assert len(clients_data) == 0

def test_post_client():
    post_respose = requests.post(f"{BASE_URL}/clients", headers=HEADER, json=new_client)

    assert post_respose.status_code == 201
    
    get_response = requests.get(f"{BASE_URL}/clients/{new_client['id']}", headers=HEADER)
    assert get_response.status_code == 200

    client_data = get_response.json()
    assert client_data != None

def test_put_client():
    get_response = requests.get(f"{BASE_URL}/clients/{new_client['id']}", headers=HEADER)
    client = get_response.json()

    old_updated_at = client['updated_at']
    old_country = client['country']
    assert client['country'] == "France"
    client['country'] = "French Guiana"

    put_response = requests.put(f"{BASE_URL}/clients/{new_client['id']}", headers=HEADER, json=client)
    assert put_response.status_code == 200

    get_client = requests.get(f"{BASE_URL}/clients/{new_client['id']}", headers=HEADER)
    assert get_response.status_code == 200

    updated_client = get_client.json()
    assert updated_client['updated_at'] != old_updated_at
    assert updated_client['country'] != old_country

def test_delete_client():
    get_client = requests.get(f"{BASE_URL}/clients/{new_client['id']}", headers=HEADER)
    client = get_client.json()
    assert client['country'] == "French Guiana"

    delete_response = requests.delete(f"{BASE_URL}/clients/{new_client['id']}", headers=HEADER)
    assert delete_response.status_code == 200

def test_get_deleted_client():
    get_request = requests.get(f"{BASE_URL}/clients/2966", headers=HEADER)
    assert get_request.json() == None

# SUCCESS
