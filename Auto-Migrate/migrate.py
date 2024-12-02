import csv, sqlite3, json, pandas


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


#df = pandas.read_csv(csvfile)
#df.to_sql(table_name, conn, if_exists='append', index=False)