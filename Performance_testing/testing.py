import requests, sqlite3, time
BASE_URL = 'http://localhost:8000/api/v1'

HEADER = {"API_KEY" : "a1b2c3d4e5"}

verified_warehouses = []
def test_get_all_warehouses():
    timer = time.time()
    response = requests.get(f"{BASE_URL}/warehouses", headers=HEADER)

    assert response.status_code == 200
    timer2 = time.time()
    print("Time taken for get all warehouses: ", timer2 - timer)


def test_get_all_warehousesdb():
    timer = time.time()
    response = requests.get(f"{BASE_URL}/warehousesdb", headers=HEADER)

    assert response.status_code == 200
    timer2 = time.time()
    print("Time taken for get all warehouses from db: ", timer2 - timer)


def test_get_all_locations():
    timer = time.time()
    response = requests.get(f"{BASE_URL}/locations", headers=HEADER)

    assert response.status_code == 200
    timer2 = time.time()
    print("Time taken for get all locations: ", timer2 - timer)

def test_get_all_locationsdb():
    timer = time.time()
    response = requests.get(f"{BASE_URL}/locationsdb", headers=HEADER)

    assert response.status_code == 200
    timer2 = time.time()
    print("Time taken for get all locations from db: ", timer2 - timer)

def test_get_all_orders():
    timer = time.time()
    response = requests.get(f"{BASE_URL}/orders", headers=HEADER)

    assert response.status_code == 200
    timer2 = time.time()
    print("Time taken for get all orders: ", timer2 - timer)

def test_get_all_ordersdb():
    timer = time.time()
    response = requests.get(f"{BASE_URL}/ordersdb", headers=HEADER)

    assert response.status_code == 200
    timer2 = time.time()
    print("Time taken for get all orders from db: ", timer2 - timer)

def test_get_all_clients():
    timer = time.time()
    response = requests.get(f"{BASE_URL}/clients", headers=HEADER)

    assert response.status_code == 200
    timer2 = time.time()
    print("Time taken for get all clients: ", timer2 - timer)

def test_get_all_clientsdb():
    timer = time.time()
    response = requests.get(f"{BASE_URL}/clientsdb", headers=HEADER)

    assert response.status_code == 200
    timer2 = time.time()
    print("Time taken for get all clients from db: ", timer2 - timer)

test_get_all_warehouses()
test_get_all_warehousesdb()
test_get_all_locations()
test_get_all_locationsdb()
test_get_all_orders()
test_get_all_ordersdb()
test_get_all_clients()
test_get_all_clientsdb()



