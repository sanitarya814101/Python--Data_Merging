import csv
from email import header
data_set_1 = []
data_set_2 = []

with open("Data_2.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data_set_1.append(row)

with open("Data_3.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        data_set_2.append(row)

header1 = data_set_1[0]
data1 = data_set_1[1:]

header2 = data_set_2[0]
data2 = data_set_2[1:]

headers = header1 + header2

data = []

for index, data_row in enumerate(data1):
    data.append(data1[index] + data2[index])

with open("Final_Dataset.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)
