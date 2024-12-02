import csv, sqlite3, json, os, pandas as pd


all_files = [
    "clients.json",
    "inventories.json",
    "item_groups.json",
    "item_lines.json",
    "item_types.json",
    "items.json",
    "locations.json",
    "orders.json",
    "shipments.json",
    "suppliers.json",
    "transfers.json",
    "warehouses.json",
]

for filename in all_files:
    file_path = f"./data/{filename}"


    with open(file_path) as file:
        data = json.load(file)

    filename = filename[:-5]
    new_csv = open(f"./data/{filename}.csv", "w", encoding="utf-8")
    csv_writer = csv.writer(new_csv)

    count = 0
    for obj in data:
        if count == 0:
            header = obj.keys()
            csv_writer.writerow(header)
            count += 1
    

        csv_writer.writerow(obj.values())
    print(f"{filename} done")
    new_csv.close()


csv_directory = "./data"

sqlite_file = "test.db"

conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()


for file_name in os.listdir(csv_directory):
    if file_name.endswith('.csv'):
        file_path = os.path.join(csv_directory, file_name)
        table_name = os.path.splitext(f"api_{file_name}")[0]
        

        df = pd.read_csv(file_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        print(f"Inserted data from {file_name} into table {table_name}")

conn.commit()
conn.close()

print("worked")

