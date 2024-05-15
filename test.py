import csv

def read_prices(filename):
    dic = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        for row in rows:
            if row and len(row) >= 2:  # Check if row is not empty and has at least two elements
                dic[row[0]] = row[1]
    return dic

recnik = read_prices('prices.csv')
print(recnik)