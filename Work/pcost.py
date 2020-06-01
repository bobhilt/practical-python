# pcost.py
#
# Exercise 1.27
import os

total_cost = 0
positions = []

os.getcwd()
with open('Work/Data/portfolio.csv', 'rt') as f:
    f.readline()
    for line in f.readlines():
        symbol, shares, price = line.split(',')
        total_cost += int(shares) * float(price)
print(total_cost)

