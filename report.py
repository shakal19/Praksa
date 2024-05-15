import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    # total_cost = 0.0
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # nshares = int(row[1])
            # price = float(row[2])
            # total_cost += nshares * price
            holdings = (row[0],int(row[1]),float(row[2]))
            portfolio.append(holdings)
    return portfolio

port = read_portfolio('portfolio.csv')
print(port)


def read_portfolio2(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    # total_cost = 0.0
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # nshares = int(row[1])
            # price = float(row[2])
            # total_cost += nshares * price
            holdings = {row[1]:row[0],row[2]:int(row[1]),row[2]: float(row[2])}
            portfolio.append(holdings)
    return portfolio

port = read_portfolio2('portfolio.csv')
print(port)