# pcost.py
#
# Exercise 1.27
import os

positions = []

os.getcwd()
def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        f.readline()
        for line in f.readlines():
            try:
                symbol, shares, price = line.split(',')
                total_cost += int(shares) * float(price)
            except(ValueError):
                print(f'Warning: invalid value in symbol {symbol}, shares {shares}, price {price}')
    return total_cost
    
cost = portfolio_cost('Work/Data/missing.csv')
print(cost)

