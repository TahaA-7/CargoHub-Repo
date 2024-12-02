import requests
import time
BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

def test_post_item():
    new_item= {"uid": "P000001",
        "code": "sjQ23408K",
        "description": "Face-to-face clear-thinking complexity",
        "short_description": "must",
        "upc_code": "6523540947122",
        "model_number": "63-OFFTq0T",
        "commodity_code": "oTo304",
        "item_line": 11,
        "item_group": 73,
        "item_type": 14,
        "unit_purchase_quantity": 47,
        "unit_order_quantity": 13,
        "pack_order_quantity": 11,
        "supplier_id": 34,
        "supplier_code": "SUP423",
        "supplier_part_number": "E-86805-uTM",
                }

    response = requests.post(f"{BASE_URL}/items", headers=HEADER, json=new_item)
    assert response.status_code == 201  #DOESN'T WORK


def test_get_posted_item():
    local_new_item= {"uid": "P000001",
        "code": "sjQ23408K",
        "description": "Face-to-face clear-thinking complexity",
        "short_description": "must",
        "upc_code": "6523540947122",
        "model_number": "63-OFFTq0T",
        "commodity_code": "oTo304",
        "item_line": 11,
        "item_group": 73,
        "item_type": 14,
        "unit_purchase_quantity": 47,
        "unit_order_quantity": 13,
        "pack_order_quantity": 11,
        "supplier_id": 34,
        "supplier_code": "SUP423",
        "supplier_part_number": "E-86805-uTM",
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
                }


    response = requests.get(f"{BASE_URL}/items/{local_new_item['uid']}", headers=HEADER)
    # check if the received data is the same as the data we posted

    assert response.json()["uid"] == local_new_item["uid"]


def test_put_item():
    get_item = requests.get(f"{BASE_URL}/items/P000001", headers=HEADER)
    item = get_item.json()
    old_updated_at = item['updated_at']
    # old_warehouse_code = 'YQZZNL56'
    item['code'] = "YQZZNL56909090"

    response = requests.put(f"{BASE_URL}/items/{item['uid']}", headers=HEADER, json=item)
    
    assert response.status_code == 200  # SUCCESS

    get_item2 = requests.get(f"{BASE_URL}/items/P000001", headers=HEADER)
    item2 = get_item2.json()
    new_updated_at = item2['updated_at']

    assert old_updated_at != new_updated_at  # SUCCESS




def test_delete_warehouse():
    local_new_item= {"uid": "P000001",
        "code": "sjQ23408K",
        "description": "Face-to-face clear-thinking complexity",
        "short_description": "must",
        "upc_code": "6523540947122",
        "model_number": "63-OFFTq0T",
        "commodity_code": "oTo304",
        "item_line": 11,
        "item_group": 73,
        "item_type": 14,
        "unit_purchase_quantity": 47,
        "unit_order_quantity": 13,
        "pack_order_quantity": 11,
        "supplier_id": 34,
        "supplier_code": "SUP423",
        "supplier_part_number": "E-86805-uTM",
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
                }
    response = requests.delete(f"{BASE_URL}/items/{local_new_item['uid']}", headers=HEADER)
    assert response.status_code == 200  # SUCCESS
    

def test_get_deleted_warehouse():
    local_new_item= {"uid": "P000001",
        "code": "sjQ23408K",
        "description": "Face-to-face clear-thinking complexity",
        "short_description": "must",
        "upc_code": "6523540947122",
        "model_number": "63-OFFTq0T",
        "commodity_code": "oTo304",
        "item_line": 11,
        "item_group": 73,
        "item_type": 14,
        "unit_purchase_quantity": 47,
        "unit_order_quantity": 13,
        "pack_order_quantity": 11,
        "supplier_id": 34,
        "supplier_code": "SUP423",
        "supplier_part_number": "E-86805-uTM",
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2015-09-26 06:37:56"
                }
    response = requests.get(f"{BASE_URL}/items/P000001", headers=HEADER)

    # print(response.json())
    assert response.json() == None  # SUCCESS


# def test_auth_get_warehouse():
#     response = requests.get(f"{BASE_URL}/warehouses")
#     assert response.status_code == 401  # Unauthorized = SUCCESS

