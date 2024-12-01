import requests

BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}



def test_post_shipment():
    new_shipment = {
        "id": 999,
        "name": "test_shipment",
        "address": "test_address",
        "city": "test_city",
        "zip_code": "test_zip_code",
        "province": "test_province",
        "country": "test_country",
        "contact_name": "test_contact_name",
        "contact_phone": "test_contact_phone",
        "contact_email": "test_contact_email",
        "created_at": "test_created_at",
        "updated_at": "test_updated_at"

    }
    response = requests.post(f"{BASE_URL}/shipments", headers=HEADER, json=new_shipment)
    assert response.status_code == 201

    response = requests.delete(f"{BASE_URL}/shipments/999", headers=HEADER)
    assert response.status_code == 204



def test_get_shipments():
    response = requests.get(f"{BASE_URL}/shipments", headers=HEADER)
    assert response.status_code == 200


def test_put_shipment():
    get_shipment = requests.get(f"{BASE_URL}/shipments/999", headers=HEADER)
    if get_shipment.headers.get('Content-Type') == 'application/json':
        shipment = get_shipment.json()
    else:
        print(f"Unexpected response: {get_shipment.text}")
        assert False, "GET request did not return valid JSON"
    old_updated_at = shipment['updated_at']

    response = requests.put(f"{BASE_URL}/shipments/999", headers=HEADER, json=shipment)
    assert response.status_code == 200

    get_response = requests.get(f"{BASE_URL}/shipments/999", headers=HEADER)
    new_shipment = get_response.json()
    new_updated_at = new_shipment['updated_at']

    assert old_updated_at != new_updated_at


