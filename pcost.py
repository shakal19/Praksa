sum=0
with open('portfolio.csv','rt') as file:
    headers=next(file)
    for line in file:
        print(line)
        row = line.split(',')
        sum+= int(row[1])

print(sum)
        