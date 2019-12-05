#1. Read the data from the spreadsheet
#2. Collect all of the sales from each month into a single list
#3. Output the total sales across all months

import csv
from collections import OrderedDict
from typing import Any

import random

def read_data():
    data = []

    with open('Student_file.csv', 'r') as student_csv:
        spreadsheet = csv.DictReader(student_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def run():
    data = read_data()

    students = []
    for row in data:
        student = row['name']
        students.append(student)

    return students

run()

def choose_house():
    random_house = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
    students = run()

    chosen_house = random.choice(random_house)
    chosen_student = random.choice(students)

    print('Who has the next turn? {}'.format(chosen_student))
    print('Which house are they in? {}'.format(chosen_house))

choose_house()