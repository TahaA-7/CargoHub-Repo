import sqlite3, json

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