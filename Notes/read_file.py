# CB 1st Reading Files

import random
import csv

# Opening a File
try:
    with open("notes/reading.txt","r") as file:
        for line in file:
            print(f"Hello {line.strip()}")
except:
    print("That file can't be found.")

else:
    print("End")

try:
    with open("notes/sample.csv",mode = "r") as demo:
        content = csv.reader(demo)
        headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0]: line[0], headers[1]:line[1]})
except:
    print("Can't find the CSV")
else:
    for line in rows:
        print(f"Username: {line['username']} | Favorite Color: {line['favorite color'].capitalize()}")
  