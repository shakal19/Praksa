def greet(name):
    'Issues greeting'
    print('Hello',name)
greet('Vuk')


def portfolio_cost(filename):
    sum=0
    with open(filename,'rt') as file:
        headers=next(file)
        for line in file:
            print(line)
            row = line.split(',')
            sum+= int(row[1])

    return sum
cost = portfolio_cost('portfolio.csv')
print('Total cost: ', cost)