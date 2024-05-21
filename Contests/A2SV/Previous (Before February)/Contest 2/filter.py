import csv
from collections import defaultdict

teams = defaultdict(list)

with open('input.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        filtered_row = {
            'firstName': row['First Name'], 
            'middleName': row['Middle Name'], 
            'lastName': row['Last Name'],
            'email':  row['Email'],
            'university': row['Eligible Universities/Colleges'],
            'image': row['University/College ID Photo'],
        }
        teams[row['Team Name'].lower()].append(filtered_row)

import json

with open('teams.json', 'w') as jsonfile:
    json.dump(teams, jsonfile)
