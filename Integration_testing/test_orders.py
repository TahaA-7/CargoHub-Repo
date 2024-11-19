import requests

BASE_URL = 'http://localhost:3000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

def test_data_post_order():
    new_order= {
        "id": 1,
        "source_id": 33,
        "order_date": "2019-04-03T11:33:15Z",
        "request_date": "2019-04-07T11:33:15Z",
        "reference": "ORD00001",
        "reference_extra": "Bedreven arm straffen bureau.",
        "order_status": "Delivered",
        "notes": "Voedsel vijf vork heel.",
        "shipping_notes": "Buurman betalen plaats bewolkt.",
        "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
        "warehouse_id": 18,
        "ship_to": None,
        "bill_to": None,
        "shipment_id": 1,
        "total_amount": 9905.13,
        "total_discount": 150.77,
        "total_tax": 372.72,
        "total_surcharge": 77.6,
        "created_at": "2019-04-03T11:33:15Z",
        "updated_at": "2019-04-05T07:33:15Z",
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

    response = requests.post(f"{BASE_URL}/orders", headers=HEADER, json=new_order)
    assert response.status_code == 201


def test_get_posted_order():
    local_new_order= {
        "id": 1,
        "source_id": 33,
        "order_date": "2019-04-03T11:33:15Z",
        "request_date": "2019-04-07T11:33:15Z",
        "reference": "ORD00001",
        "reference_extra": "Bedreven arm straffen bureau.",
        "order_status": "Delivered",
        "notes": "Voedsel vijf vork heel.",
        "shipping_notes": "Buurman betalen plaats bewolkt.",
        "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
        "warehouse_id": 18,
        "ship_to": None,
        "bill_to": None,
        "shipment_id": 1,
        "total_amount": 9905.13,
        "total_discount": 150.77,
        "total_tax": 372.72,
        "total_surcharge": 77.6,
        "created_at": "2019-04-03T11:33:15Z",
        "updated_at": "2019-04-05T07:33:15Z",
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


    response = requests.get(f"{BASE_URL}/orders/{local_new_order['id']}", headers=HEADER)
    # check if the received data is the same as the data we posted



    assert response.status_code == 200
    assert response.json()['id'] == local_new_order["id"]

def test_get_posted_order_items():
    local_order_items= {
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


    response = requests.get(f"{BASE_URL}/orders/1/items", headers=HEADER)
    # check if the received data is the same as the data we posted



    assert response.status_code == 200
    assert response.json() == local_order_items["items"]


    
def test_put_order_items():
    local_order={
        "id": 1,
        "source_id": 33,
        "order_date": "2019-04-03T11:33:15Z",
        "request_date": "2019-04-07T11:33:15Z",
        "reference": "ORD00001",
        "reference_extra": "Bedreven arm straffen bureau.",
        "order_status": "Delivered",
        "notes": "Voedsel vijf vork heel.",
        "shipping_notes": "Buurman betalen plaats bewolkt.",
        "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
        "warehouse_id": 18,
        "ship_to": None,
        "bill_to": None,
        "shipment_id": 1,
        "total_amount": 9905.13,
        "total_discount": 150.77,
        "total_tax": 372.72,
        "total_surcharge": 77.6,
        "created_at": "2019-04-03T11:33:15Z",
        "updated_at": "2019-04-05T07:33:15Z",
        "items": [
            {
                "item_id": "P007435",
                "amount": 23
            }
        ]}

    response = requests.put(f"{BASE_URL}/orders/1/items", headers=HEADER, json=local_order)
    # check if the received data is the same as the data we posted

    assert response.status_code == 201
    assert requests.get(f"{BASE_URL}/orders/1/items", headers=HEADER) == local_order["items"]

def test_put_order():
    get_order = requests.get(f"{BASE_URL}/orders/1", headers=HEADER)
    order = get_order.json()
    old = order["notes"]
    order["notes"] = "yappa"


    response = requests.put(f"{BASE_URL}/orders/1", headers=HEADER, json=order)
    
    assert response.status_code == 200  # SUCCESS

    get_order2 = requests.get(f"{BASE_URL}/orders/1", headers=HEADER)
    order2 = get_order2.json()


    assert  order2["notes"] != old  # SUCCESS


def test_get_updated_order():

    response = requests.get(f"{BASE_URL}/orders/1", headers=HEADER)
    # check if the received data is the same as the data we posted

    assert response.status_code == 200
    assert response.json()['notes'] == "yappa"


def test_delete_order():

    response = requests.delete(f"{BASE_URL}/orders/1", headers=HEADER)
    assert response.status_code == 200  # SUCCESS

def test_get_deleted_order():

    response = requests.get(f"{BASE_URL}/orders/1", headers=HEADER)
    assert response.json() == None



