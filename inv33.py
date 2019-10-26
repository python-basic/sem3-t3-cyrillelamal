import csv
import json


with open('data.json', 'rt') as json_file:
    json_data = json.loads(json_file.read())
    fieldnames = list(json_data[0].keys())
    with open('log.csv', 'wt') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in json_data:
            writer.writerow(row)
