# pcost.py
#
# Exercise 1.27
import os
import csv

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
    
cost = portfolio_cost('Work/Data/missing.csv')
print(cost)

