
import requests

BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}


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
