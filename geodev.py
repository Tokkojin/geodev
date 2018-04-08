import csv

with open('projects.tsv') as tsv:
    reader = csv.DictReader(tsv, dialect='excel-tab')
    for row in reader:
        print(row['project_id'])