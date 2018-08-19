#! python3
import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Score']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Mike', 'Score': 90})
    writer.writerow({'Name': 'Bob', 'Score': 95})