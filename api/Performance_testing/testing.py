import requests, sqlite3, time
BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

verified_warehouses = []
def test_get_all_warehouses():
    timer = time.time()

    response = requests.get(f"{BASE_URL}/warehouses", headers=HEADER)

    timer2 = time.time()
    print("Time taken for get all warehouses: ", timer2 - timer)


def test_get_all_warehousesdb():
    timer = time.time()
    response = requests.get(f"{BASE_URL}/warehousesdb", headers=HEADER)

    assert response.status_code == 200
    timer2 = time.time()
    print("Time taken for get all warehouses from db: ", timer2 - timer)


     

test_get_all_warehouses()
test_get_all_warehousesdb()