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
