import requests

BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}


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
