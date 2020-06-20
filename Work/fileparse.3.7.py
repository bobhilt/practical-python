# fileparse.py
#
# Exercise 3.7
#
''' parse a csv file into a list of records
    (passes has_header flag), optional delimiter.
'''

import csv
def parse_csv(filename, select=None, recast=None, has_headers=False, delimiter=','):
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
    
        if has_headers:
            headers = next(rows)

            if select:              # return only passed columns
                indices = [headers.index(column_name) for column_name in select]
                headers  = select

        records = []
        for row in rows:
            if not row:         #skip empty rows
                continue
            
            # Filter row if select columns were 
            if select:
                row = [row[index] for index in indices]

            if recast:
                row = [f(value) for f,value in zip(recast, row)]

            if has_headers:
                record = dict(zip(headers,row))
            else:
                record = tuple(row)

            records.append(record)
    
    return records
