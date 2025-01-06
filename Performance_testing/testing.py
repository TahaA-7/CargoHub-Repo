import requests, sqlite3
BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

# def test_get_all_warehouses():
    

#     response = requests.get(f"{BASE_URL}/warehouses", headers=HEADER)
#     # check if the received data is the same as the data we posted

#     assert response.status_code == 200  # SUCCESS
#     print(type(response.json()[0]))



def test_get_all_warehousesdb():
    response = requests.get(f"{BASE_URL}/warehousesdb", headers=HEADER)

    assert response.status_code == 200
    print(response.json()[-1])

test_get_all_warehousesdb()