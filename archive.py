import csv

with open("Data_1.csv") as input, open("Data_3.csv", "w", newline="") as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
