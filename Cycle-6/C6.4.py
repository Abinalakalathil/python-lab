import csv
with open('D:\csv.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)