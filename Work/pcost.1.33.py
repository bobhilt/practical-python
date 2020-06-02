# pcost.py
#
# Exercise 1.33
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                symbol, shares, price = row
                total_cost += int(shares) * float(price)
            except(ValueError):
                print(f'Warning: invalid value in symbol {symbol}, shares {shares}, price {price}')
    return total_cost
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/missing.csv'
cost = portfolio_cost(filename)
print(cost)

