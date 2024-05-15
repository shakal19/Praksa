symbols='ABC,DEF,GHJ'
symlist=symbols.split(',')
print(symlist)
symlist[2]="BMW"
print(symlist)

for s in symlist:
    print('s=',s)