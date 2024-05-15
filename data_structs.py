s=('GOOG',100,490.1)
print(s)

name,shares, price =s
print('Cost',shares*price)
s={
    'name': 'GOG',
    'shares':100,
    'price': 490.1
}

print(s['name'])
s['date']='6/6/2007'

print(s)

import csv
with open('portfolio.csv','rt') as f:
    rows = csv.reader(f)
    next(rows)
    row = next(rows)
    tuple = (int(row[1]),float(row[2]))
    cost = tuple[0]*tuple[1]
    print(cost)

list(s)
print(s)

for key in s:
    print('key = ',key)

for key in s :
    print(key , "= " ,s[key])


    keys=s.keys()

for key,value in s.items():
    print(key,'=',value)

print('Zadatak ')

prices = {}
with open('prices.csv', 'rt') as f:
    for line in f:
            row = line.split(',')
            if(row[0] != '\n' and row[1]!='\n'):

                prices[row[0]] = float(row[1])

print(prices)


# Sets
names=['IBM','BMW',"APPLE","IBM","APPLE"]
set = set(names)
print(set)


set.add("ABCD")
set2 = {"a","b","c"}
print(set | set2)
print(set & set2)



print("READ PRICES")

def read_prices(filename):
    dic = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        for row in rows:
            if row :
                dic[row[0]]=row[1]
    return dic 



recnik = read_prices('prices.csv')
print(recnik)