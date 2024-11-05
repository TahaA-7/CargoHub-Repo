import requests

BASE_URL = 'http://localhost:3000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

def test_data_post_warehouse():
    new_warehouse= {"id": 999999999,
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
    local_new_warehouse= {"id": 999999999,
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
    get_warehouse = requests.get(f"{BASE_URL}/warehouses/999999999", headers=HEADER)
    warehouse = get_warehouse.json()
    old_updated_at = warehouse['updated_at']
    # old_warehouse_code = 'YQZZNL56'
    warehouse['code'] = "YQZZNL56909090"

    response = requests.put(f"{BASE_URL}/warehouses/999999999", headers=HEADER, json=warehouse)
    
    assert response.status_code == 200  # SUCCESS

    get_warehouse2 = requests.get(f"{BASE_URL}/warehouses/999999999", headers=HEADER)
    warehouse2 = get_warehouse2.json()
    new_updated_at = warehouse2['updated_at']

    assert old_updated_at != new_updated_at  # SUCCESS


def test_get_updated_warehouse():
    local_updated_warehouse= {"id": 999999999,
                "code": "YQZZNL56909090",
                "name": "Heemskerk cargo hub",
                "address": "Karlijndreef 281",
                "zip": "4002 AS",
                "city": "Heemskerk",
                "province": "Friesland",
                "country": "NL",
                "contact": {"name": "Fem Keijzer", "phone": "(078) 0013363", "email": "blamore@example.net"}, "created_at": "1983-04-13 04:59:55", "updated_at": "2007-02-08 20:11:00"
                }
    response = requests.get(f"{BASE_URL}/warehouses/{local_updated_warehouse['id']}", headers=HEADER)
    # check if the received data is the same as the data we posted
    assert response.json()['code'] == local_updated_warehouse['code']  # SUCCESS


def test_delete_warehouse():
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


    