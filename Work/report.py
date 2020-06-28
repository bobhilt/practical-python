# report.py
#
# Through Exercise 2.9
#       Name     Shares      Price     Change
# ---------- ---------- ---------- ----------
#         AA        100       9.22     -22.98
#        IBM         50     106.28      15.18
#        CAT        150      35.46     -47.98
#       MSFT        200      20.89     -30.34
#         GE         95      13.48     -26.89
#       MSFT         50      20.89     -44.21
#        IBM        100     106.28      35.84

from fileparse import parse_csv

def make_report(portfolio, prices):
    col_width=10
    headers = list(portfolio[0].keys())
    headers.append('Change')
    border = '-' * col_width
    header1 = f"{headers[0]:>{col_width}} {headers[1]:>{col_width}} {headers[2]:>{col_width}} {headers[3]:>{col_width}}\n"
    separator = f"{border:>{col_width}} {border:>{col_width}} {border:>{col_width}} {border:>{col_width}}\n"
    p = portfolio
    detail = ""
    for r in p[1:]:
        price = prices[r['name']]
        change = r['price'] - price
        detail += f"{r['name']:>{col_width}} {r['shares']:>{col_width}} {r['price']:>{col_width}.2f} {change:>{col_width}.2f}\n"
    return header1 + separator + detail

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')

    portfile = argv[1]
    pricefile = argv[2]
    portfolio = parse_csv(portfile,has_headers=True,recast=[str,int,float])
    prices = dict(parse_csv(pricefile,has_headers=False, recast=[str,float]))
    report = make_report(portfolio, prices)
    print(report)

if __name__ == '__main__':
    import sys
    main(sys.argv)