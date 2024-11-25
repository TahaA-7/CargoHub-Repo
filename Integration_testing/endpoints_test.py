import requests

BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

new_shipment = {
    "id": 999999898,
    "order_id": 999999999,
    "source_id": 33333333,
    "order_date": "2024-05-09",
    "shipment_date": "2024-05-11",
    "shipment_type": "I",
    "shipment_status": "Pending",
    "notes": "aapje wil banaantje",
    "carrier_code": "DPD",
    "carrier_description": "Dynamic Parcel Distribution",
    "service_code": "Fastest",
    "payment_type": "Manual",
    "transfer_mode": "Ground",
    "total_package_count": 31,
    "total_package_weight": 594.42,
    "created_at": "2024-05-10 19:11:00",
    "updated_at": "2024-05-11 20:11:00",
    "items": [
        {
            "item_id": "P007435",
            "amount": 23
        },
        {
            "item_id": "P009557",
            "amount": 1
        },
        {
            "item_id": "P009553",
            "amount": 50
        },
        {
            "item_id": "P010015",
            "amount": 16
        },
        {
            "item_id": "P002084",
            "amount": 33
        },
        {
            "item_id": "P009663",
            "amount": 18
        },
        {
            "item_id": "P010125",
            "amount": 18
        },
        {
            "item_id": "P005768",
            "amount": 26
        },
        {
            "item_id": "P004051",
            "amount": 1
        },
        {
            "item_id": "P005026",
            "amount": 29
        },
        {
            "item_id": "P000726",
            "amount": 22
        },
        {
            "item_id": "P008107",
            "amount": 47
        },
        {
            "item_id": "P001598",
            "amount": 32
        },
        {
            "item_id": "P002855",
            "amount": 20
        },
        {
            "item_id": "P010404",
            "amount": 30
        },
        {
            "item_id": "P010446",
            "amount": 6
        },
        {
            "item_id": "P001517",
            "amount": 9
        },
        {
            "item_id": "P009265",
            "amount": 2
        },
        {
            "item_id": "P001108",
            "amount": 20
        },
        {
            "item_id": "P009110",
            "amount": 18
        },
        {
            "item_id": "P009686",
            "amount": 13
        }
    ]
}

new_supplier = {
    "id": 797,
    "code": "SUP0797",
    "name": "Yip, Yap and Yup",
    "address": "3984 Johan-Pieterstraat",
    "address_extra": "",
    "city": "Uik",
    "zip_code": "3984",
    "province": "Zuid-Holland",
    "country": "Netherlands",
    "contact_name": "Klaas Verhoeven",
    "phonenumber": "061-546-593-09",
    "reference": "KELLABBERTAND",
    "created_at": "1999-10-20 19:07:18",
    "updated_at": "2000-11-21 23:01:12"
}

new_transfer = {
    "id": 212212,
    "reference": "TR212212",
    "transfer_from": None,
    "transfer_to": 33851,
    "transfer_status": "Completed",
    "created_at": "2003-11-11",
    "updated at": "2003-11-20",
    "items": [
        {
            "item_id": "P001354",
            "amount": 49
        }
    ]
}


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


def test_get_and_post_shipment():
    get_response = requests.get(f"{BASE_URL}/shipments/999999898")
    assert get_response.status_code == 401

    get_response2 = requests.get(f"{BASE_URL}/shipments/999999898", headers=HEADER)
    assert get_response2.json() == None

    post_response = requests.post(f"{BASE_URL}/shipments", headers=HEADER, json=new_shipment)
    assert post_response.status_code == 201

    get_response3 = requests.get(f"{BASE_URL}/shipments/999999898", headers=HEADER)
    assert get_response3.status_code == 200


def test_put_shipment():
    get_shipment = requests.get(f"{BASE_URL}/shipments/999999898", headers=HEADER)
    shipment = get_shipment.json()
    old_updated_at = shipment['updated_at']
    shipment['transfer_mode'] = "Air"

    response = requests.put(f"{BASE_URL}/shipments/999999898", headers=HEADER, json=shipment)
    assert response.status_code == 200

    get_response = requests.get(f"{BASE_URL}/shipments/999999898", headers=HEADER)
    assert get_response.status_code == 200
    assert get_shipment != get_response
    assert get_shipment.json() != new_shipment


def test_delete_shipment():
    get_shipment = requests.get(f"{BASE_URL}/shipments/999999898", headers=HEADER)
    shipment = get_shipment.json()
    assert shipment['transfer_mode'] == "Air"

    delete_response = requests.delete(f"{BASE_URL}/shipments/999999898", headers=HEADER)
    assert delete_response.status_code == 200


def test_get_after_deleting_shipment():
    get_shipment_after_delete = requests.get(f"{BASE_URL}/shipments/999999898", headers=HEADER)
    assert get_shipment_after_delete.json() == None

#

def test_get_post_get_supplier():
    get_response = requests.get(f"{BASE_URL}/suppliers/797", headers=HEADER)
    #assert get_response.status_code == 404
    assert get_response.json() == None

    post_response = requests.post(f"{BASE_URL}/suppliers", headers=HEADER, json=new_supplier)
    assert post_response.status_code == 201

    get_response2 = requests.get(f"{BASE_URL}/suppliers/{new_supplier['id']}", headers=HEADER)
    assert get_response2.status_code == 200
    assert get_response2.json() != None


def test_put_and_get_supplier():
    get_supplier = requests.get(f"{BASE_URL}/suppliers/797", headers=HEADER)
    supplier = get_supplier.json()
    old_updated_at = supplier['updated_at']
    old_supplier_name = supplier['contact_name']
    supplier['contact_name'] = 'Mohammed Talhaoui'

    put_response = requests.put(f"{BASE_URL}/suppliers/797", headers=HEADER, json=supplier)
    assert put_response.status_code == 200

    get_supplier2 = requests.get(f"{BASE_URL}/suppliers/797", headers=HEADER)
    assert get_supplier2.status_code == 200

    new_supplier = get_supplier2.json()
    assert new_supplier['updated_at'] != old_updated_at
    assert new_supplier['contact_name'] != old_supplier_name


def test_delete_and_get_supplier():
    get_supplier = requests.get(f"{BASE_URL}/suppliers/{new_supplier['id']}", headers=HEADER)
    supplier = get_supplier.json()
    assert supplier['contact_name'] == "Mohammed Talhaoui"

    delete_response = requests.delete(f"{BASE_URL}/suppliers/{new_supplier['id']}", headers=HEADER)
    assert delete_response.status_code == 200

    get_supplier2 = requests.get(f"{BASE_URL}/suppliers/{new_supplier['id']}", headers=HEADER)
    assert get_supplier2.json() == None

#

def test_post_transfer():
    get_transfer = requests.get(f"{BASE_URL}/transfers/{new_transfer['id']}", headers=HEADER)
    assert get_transfer.json() == None

    post_response = requests.post(f"{BASE_URL}/transfers", headers=HEADER, json=new_transfer)
    assert post_response.status_code == 201

    get_response = requests.get(f"{BASE_URL}/transfers/{new_transfer['id']}", headers=HEADER)
    assert get_response.status_code == 200
    assert get_response.json() != None

def test_put_tranfser():
    get_transfer = requests.get(f"{BASE_URL}/transfers/212212", headers=HEADER)
    transfer = get_transfer.json()
    old_updated_at = transfer['updated_at']
    old_transfer_from = transfer['transfer_from']
    transfer['transfer_from'] = "Netherlands"

    put_response = requests.put(f"{BASE_URL}/transfers/212212", headers=HEADER, json=transfer)
    assert put_response.status_code == 200

    new_get_transfer = requests.get(f"{BASE_URL}/transfers/212212", headers=HEADER)
    assert new_get_transfer.status_code == 200
    new_transfer = new_get_transfer.json()
    assert new_transfer['updated_at'] != old_updated_at
    assert new_transfer['transfer_from'] != old_transfer_from

def test_delete_transfer():
    get_transfer = requests.get(f"{BASE_URL}/transfers/212212", headers=HEADER)
    transfer = get_transfer.json()
    assert transfer['transfer_from'] == "Netherlands"

    delete_response = requests.delete(f"{BASE_URL}/transfers/212212", headers=HEADER)
    assert delete_response.status_code == 200

    get_transfer2 = requests.get(f"{BASE_URL}/transfers/212212", headers=HEADER)
    assert get_transfer2.json() == None
