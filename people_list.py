people_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
import csv

with open ('export.csv', 'w', encoding='utf-8') as w:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(w, fields, delimiter=';')
    writer.writeheader()
    for row in people_list:
        writer.writerow(row)

