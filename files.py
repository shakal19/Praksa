# f = open('temp.txt','rt')
# print(f)
# f2=open('bar.txt','wt')
# f2.write('some text')

# f.close()
# f2.close()

# with open('bar.txt','rt') as file :
#     data=file.read()
#     print(data)


# with open('outfile','wt') as out:
#     print("Hello world",file=out)


import os
os.getcwd()

with open('portfolio.csv','rt') as f:
    data = f.read()
    print(data)

print("GZIP")
import gzip 
with gzip.open('portfolio.csv.gz','rt') as f:
    for line in f:
        print(line,end=" ")