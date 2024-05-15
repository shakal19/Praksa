s={
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}
print('{name:>10s} {shares:10d} {price:10.2f}'.format_map(s))

print('{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1))


print('%0.2f' % (3.14323))


import csv





    
 


def take_prices(filename):
    dic = {}
    with open('prices.csv',"rt")as f:
        rows = csv.reader(f)
        for row in rows:
            
            if row and len(row) >= 2:
                dic[row[0]]=row[1]
    return dic


def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    # total_cost = 0.0
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            
            holdings = (row[0],int(row[1]),float(row[2]))
            portfolio.append(holdings)
    return portfolio

port = read_portfolio('portfolio.csv')
print("STOCK\n")
print(port)
print("\n\n")
prices=take_prices('prices.csv')
print("PRICES\n")
print(prices)
# print(port[0][0])
# print(prices[0])

def izvuci(port):
    temp=[]
    print("port funkcija\n")
    print(port)
    for kljuc  in port:
        
        temp.append(kljuc[0])
    return temp

def kljucevi(prices):
    lista=[]
    for key,_ in prices.items():
        lista.append(key)
    return lista



print("\nKljucevi\n")
# test = kljucevi(prices)
# print(test)

t2=izvuci(port)
print(t2)

def make_report( port, prices):
    temp = kljucevi(prices)
    temp2 = izvuci(port)
    # print(temp)
    for i in range(len(temp)):
        for j in range(len(temp2)):

            if(str(temp2[j])== str(temp[i])):
                print(temp[i])

make_report(port,prices)