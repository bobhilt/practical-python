# report.2.9.py
#
# Exercise 2.9
#       Name     Shares      Price     Change
# ---------- ---------- ---------- ----------
#         AA        100       9.22     -22.98
#        IBM         50     106.28      15.18
#        CAT        150      35.46     -47.98
#       MSFT        200      20.89     -30.34
#         GE         95      13.48     -26.89
#       MSFT         50      20.89     -44.21
#        IBM        100     106.28      35.84

from csv import reader

def read_portfolio(file_name):
    with open(file_name, 'r') as f:
        portfolio_reader = reader(f)
        portfolio =  [x for x in portfolio_reader]
    return portfolio

def read_prices(file_name):
    with open(file_name, 'r') as f:
        prices_reader = reader(f)
        prices = {row[0]: row[1] for row in prices_reader if len(row)==2}
        return prices

def make_report(portfolio, prices):
    # header
    # header1 = "        Name       Shares       Price      Change\n"
    #header2 = "  ----------   ----------  ----------  ----------\n"
    headers = headers = ('Name', 'Shares', 'Price', 'Change','----------')
    header1 = f"{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}\n"
    header2 = f"{headers[4]:>10} {headers[4]:>10} {headers[4]:>10} {headers[4]:>10}\n"
    p = portfolio
    detail = ""
    for r in p[1:]:
        name = r[0]
        shares = int(r[1])
        price = float(prices[r[0]])
        price_str = f'${price:0.2f}'    # stringify with $ so it can be right-aligned in formatted string below.
        change = float(r[2]) - float(prices[r[0]])
        detail += f"{name:>10} {shares:>10} {price_str:>10} {change:>10.2f}\n"

    return header1 + header2 + detail

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

print(report)