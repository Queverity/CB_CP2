# CB 1st Write To Notes

import csv
# Writing to a flie
"""try:
    with open("notes\siblings.txt","w") as file:
        file.write("Anthony")
except:
    print("Writing failed")

# Appending to a file
try:
    with open("notes\siblings.txt","a") as file:
        file.write("\nWren\n")
except:
    print("Appending failed")
else:
    print("Code ended")

# Creating a file
# When you write or append to a file that does not exist, the file is just made. Super easy.

# Reading & Writing
try:
    with open("notes\\siblings.txt","r+") as file:
        content = file.read()
        content += "\nI wrote on my file"
        file.write(content)     
except:
    print("Reading & Writing failed")
else:
    print("Reading and Writing finished")"""

# add a + to r for reading and writing

# Writing to a CSV
new_username = ['Queverity','Burgundy']

with open("notes/sample.csv","r+",newline='') as csvfile:
    # delimiter is the thing that seperates your items
    fieldnames = ['username','favorite_color']
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'username':'FakeFaceFoxy','favorite_color':'red'})
    writer.writerow({'username':'FakeFoxy','favorite_color':'blue'})
    writer.writerow({'username':'FaceFoxy','favorite_color':'orange'})
    writer.writerow({'username':'FakeFaceFake','favorite_color':'yellow'})

print("Code finished")

