import csv
import re
from collections import namedtuple

# with open('stocks.csv') as f:
#     f_csv = csv.reader(f, delimiter='\t')
#     headers = next(f_csv)
#     for row in f_csv:
#         print(row)

# col_types = [str, float, str, str, float, int]
# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         row = tuple(convert(value) for convert, value in zip(col_types, row))
#         print(row)

# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     # headers = next(f_csv)
#     headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
#     Row = namedtuple('Row', headers)
#     for r in f_csv:
#         row = Row(*r)
#         print(row)

# headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
# rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
#         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
#         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
#         ]
#
# with open('dane.csv', 'w') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
        {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
        {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
        ]

# with open('dane2.csv', 'w') as f:
#     f_csv = csv.DictWriter(f, headers)
#     f_csv.writeheader()
#     f_csv.writerows(rows)

fields_type = [('Price', float), ('Change', float), ('Volume', int)]
with open('dane2.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in fields_type)
        print(row)
