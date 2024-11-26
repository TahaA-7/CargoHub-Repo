import csv, sqlite3, json, pandas

file_path = "../TESTJSON/testing.json"

# Open and write to the file
with open(file_path) as file:
    data = json.load(file)

new_csv = open("testing.csv", "w")
csv_writer = csv.writer(new_csv)

count = 0


for obj in data:
    if count == 0:
 
        # Writing headers of CSV file
        header = obj.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(obj.values())

new_csv.close()


#df = pandas.read_csv(csvfile)
#df.to_sql(table_name, conn, if_exists='append', index=False)