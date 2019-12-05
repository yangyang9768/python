#1. Read the data from the spreadsheet
#2. Collect all of the sales from each month into a single list
#3. Output the total sales across all months

import csv
from collections import OrderedDict
from typing import Any


def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def run():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    print('Total sales: {}'.format(total))

    monthly_sales = []
    for row in data:
        print('Monthly Sales: {}'.format(int(row['sales'])))

run()