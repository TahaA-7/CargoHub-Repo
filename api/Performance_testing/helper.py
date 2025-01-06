import sqlite3

def get_warehousesdb():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM warehouses")


    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]


    all_warehouses = []
    for i, row in enumerate(rows):
        row_dict = dict(zip(columns, row))
        all_warehouses.append(row_dict)

    conn.close()
    return all_warehouses

def get_locationsdb():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM locations")


    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]


    all_locations = []
    for i, row in enumerate(rows):
        row_dict = dict(zip(columns, row))
        all_locations.append(row_dict)

    conn.close()
    return all_locations

def get_ordersdb():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")


    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]


    all_orders = []
    for i, row in enumerate(rows):
        row_dict = dict(zip(columns, row))
        all_orders.append(row_dict)

    conn.close()
    return all_orders

def get_clientsdb():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")


    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]


    all_clients = []
    for i, row in enumerate(rows):
        row_dict = dict(zip(columns, row))
        all_clients.append(row_dict)

    conn.close()
    return all_clients