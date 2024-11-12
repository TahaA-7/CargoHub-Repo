import requests

BASE_URL = 'http://localhost:3000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

def test_data_post_warehouse():
    new_warehouse= {"id": 1239,
                "code": "YQZZNL56",
                "name": "Heemskerk cargo hub",
                "address": "Karlijndreef 281",
                "zip": "4002 AS",
                "city": "Heemskerk",
                "province": "Friesland",
                "country": "NL",
                "contact": {"name": "Fem Keijzer", "phone": "(078) 0013363", "email": "blamore@example.net"}, "created_at": "1983-04-13 04:59:55", "updated_at": "2007-02-08 20:11:00"
                }

    response = requests.post(f"{BASE_URL}/warehouses", headers=HEADER, json=new_warehouse)
    assert response.status_code == 201  # SUCCESS


def test_get_posted_warehouse():
    local_new_warehouse= {"id": 1239,
                "code": "YQZZNL56",
                "name": "Heemskerk cargo hub",
                "address": "Karlijndreef 281",
                "zip": "4002 AS",
                "city": "Heemskerk",
                "province": "Friesland",
                "country": "NL",
                "contact": {"name": "Fem Keijzer", "phone": "(078) 0013363", "email": "blamore@example.net"}, "created_at": "1983-04-13 04:59:55", "updated_at": "2007-02-08 20:11:00"
                }


    response = requests.get(f"{BASE_URL}/warehouses/{local_new_warehouse['id']}", headers=HEADER)
    # check if the received data is the same as the data we posted

    print(response.json())
    print(local_new_warehouse)

    assert response.status_code == 200  # SUCCESS

def test_put_warehouse():
    get_warehouse = requests.get(f"{BASE_URL}/warehouses/1239", headers=HEADER)
    warehouse = get_warehouse.json()
    old_updated_at = warehouse['updated_at']
    # old_warehouse_code = 'YQZZNL56'
    warehouse['code'] = "YQZZNL56909090"

    response = requests.put(f"{BASE_URL}/warehouses/1239", headers=HEADER, json=warehouse)
    
    assert response.status_code == 200  # SUCCESS

    get_warehouse2 = requests.get(f"{BASE_URL}/warehouses/1239", headers=HEADER)
    warehouse2 = get_warehouse2.json()
    new_updated_at = warehouse2['updated_at']

    assert old_updated_at != new_updated_at  # SUCCESS


# def test_get_updated_warehouse():
#     local_updated_warehouse= {"id": 1239,
#                 "code": "YQZZNL56909090",
#                 "name": "Heemskerk cargo hub",
#                 "address": "Karlijndreef 281",
#                 "zip": "4002 AS",
#                 "city": "Heemskerk",
#                 "province": "Friesland",
#                 "country": "NL",
#                 "contact": {"name": "Fem Keijzer", "phone": "(078) 0013363", "email": "blamore@example.net"}, "created_at": "1983-04-13 04:59:55", "updated_at": "2007-02-08 20:11:00"
#                 }
#     response = requests.get(f"{BASE_URL}/warehouses/{local_updated_warehouse['id']}", headers=HEADER)
#     # check if the received data is the same as the data we posted
#     assert response.json() == local_updated_warehouse


def test_delete_warehouse():
    local_warehouse= {"id": 1239,
                "code": "YQZZNL56909090",
                "name": "Heemskerk cargo hub",
                "address": "Karlijndreef 281",
                "zip": "4002 AS",
                "city": "Heemskerk",
                "province": "Friesland",
                "country": "NL",
                "contact": {"name": "Fem Keijzer", "phone": "(078) 0013363", "email": "blamore@example.net"}, "created_at": "1983-04-13 04:59:55", "updated_at": "2007-02-08 20:11:00"
                }
    response = requests.delete(f"{BASE_URL}/warehouses/{local_warehouse['id']}", headers=HEADER)
    assert response.status_code == 200  # SUCCESS

def test_get_deleted_warehouse():
    local_warehouse= {"id": 999999999,
                "code": "YQZZNL56909090",
                "name": "Heemskerk cargo hub",
                "address": "Karlijndreef 281",
                "zip": "4002 AS",
                "city": "Heemskerk",
                "province": "Friesland",
                "country": "NL",
                "contact": {"name": "Fem Keijzer", "phone": "(078) 0013363", "email": "blamore@example.net"}, "created_at": "1983-04-13 04:59:55", "updated_at": "2007-02-08 20:11:00"
                }
    response = requests.get(f"{BASE_URL}/warehouses/{local_warehouse['id']}", headers=HEADER)

    # print(response.json())
    assert response.json() == None  # SUCCESS


# def test_auth_get_warehouse():
#     response = requests.get(f"{BASE_URL}/warehouses")
#     assert response.status_code == 401  # Unauthorized = SUCCESS

    
    
    
def test_data_post_client():
    new_client = {
        "id": 90909090,
        "name": "Mccormick LLC",
        "address": "6409 Morris Terrace",
        "city": "North Glenda",
        "zip_code": "07992",
        "province": "Arizona",
        "country": "United States",
        "contact_name": "Mr. Joseph Morales",
        "contact_phone": "358-492-9708x998",
        "contact_email": "leonard32@example.net",
        "created_at": "1979-05-01 03:25:35",
        "updated_at": "2017-08-03 08:10:08"
    }

    response = requests.post(f"{BASE_URL}/clients", headers=HEADER, json=new_client)
    assert response.status_code == 201  # SUCCESS


def test_get_posted_client():
    test_client_id = 90909090

    response = requests.get(f"{BASE_URL}/clients/{test_client_id}", headers=HEADER)
    # check if the received data is the same as the data we posted

    assert response.status_code == 200  # SUCCESS



def test_put_client():
    get_client = requests.get(f"{BASE_URL}/clients/90909090", headers=HEADER)
    client = get_client.json()
    old_updated_at = client['updated_at']
    # old_client_code = 'YQZZNL56'
    client['city'] = "New city test"

    response = requests.put(f"{BASE_URL}/clients/90909090", headers=HEADER, json=client)
    
    assert response.status_code == 200  # SUCCESS

    get_client2 = requests.get(f"{BASE_URL}/clients/90909090", headers=HEADER)
    client2 = get_client2.json()
    new_updated_at = client2['updated_at']

    assert old_updated_at != new_updated_at  # SUCCESS


def test_get_updated_client():
    
    response = requests.get(f"{BASE_URL}/clients/90909090", headers=HEADER)
    # check if the received data is the same as the data we posted
    assert response.json()['city'] == 'New city test'  # SUCCESS



def test_delete_client():
   
    response = requests.delete(f"{BASE_URL}/clients/90909090", headers=HEADER)
    assert response.status_code == 200  # SUCCESS

def test_get_deleted_client():
 
    response = requests.get(f"{BASE_URL}/clients/90909090", headers=HEADER)

    # print(response.json())
    assert response.json() == None  # SUCCESS




def test_data_post_inventory():
    new_inventory = {
        "id": 12109321789,
        "item_id": "P00TEST0002",
        "description": "Focused transitional alliance",
        "item_reference": "nyg48736S",
        "locations": [
            19800,
            23653,
            3068,
            3334,
            20477,
            20524,
            17579,
            2271,
            2293,
            22717
        ],
        "total_on_hand": 194,
        "total_expected": 0,
        "total_ordered": 139,
        "total_allocated": 0,
        "total_available": 55,
        "created_at": "2020-05-31 16:00:08",
        "updated_at": "2020-11-08 12:49:21"
    }

    response = requests.post(f"{BASE_URL}/inventories", headers=HEADER, json=new_inventory)
    assert response.status_code == 201  # SUCCESS


def test_get_posted_inventory():
    test_inventory_id = 90909090

    response = requests.get(f"{BASE_URL}/inventories/{test_inventory_id}", headers=HEADER)
    # check if the received data is the same as the data we posted

    assert response.status_code == 200  # SUCCESS



def test_put_inventory():
    get_inventory = requests.get(f"{BASE_URL}/inventories/12109321789", headers=HEADER)
    inventory = get_inventory.json()
    old_updated_at = inventory['updated_at']
    # old_inventory_code = 'YQZZNL56'
    inventory['description'] = "Changed description"

    response = requests.put(f"{BASE_URL}/inventories/12109321789", headers=HEADER, json=inventory)
    
    assert response.status_code == 200  # SUCCESS

    get_inventory2 = requests.get(f"{BASE_URL}/inventories/12109321789", headers=HEADER)
    inventory2 = get_inventory2.json()
    new_updated_at = inventory2['updated_at']

    assert old_updated_at != new_updated_at  # SUCCESS


def test_get_updated_inventory():
    
    response = requests.get(f"{BASE_URL}/inventories/12109321789", headers=HEADER)
    # check if the received data is the same as the data we posted
    assert response.json()['description'] == 'Changed description'  # SUCCESS

def test_delete_inventory():
   
    response = requests.delete(f"{BASE_URL}/inventories/12109321789", headers=HEADER)
    assert response.status_code == 200  # SUCCESS

def test_get_deleted_inventory():
 
    response = requests.get(f"{BASE_URL}/inventories/12109321789", headers=HEADER)

    # print(response.json())
    assert response.json() == None  # SUCCESS