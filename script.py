import os 
with open('files.txt' ,'rt') as f:
    lines = f.readlines()
    for line in lines:
        

        for i in range(len(line)):
            if line[i]=='_':
                l=str(line.strip())

               
                new_name=line[i+1:len(line)].strip()
                if(os.path.exists(l)):
                    os.rename(l,new_name)
        
        
with open('files2.txt' ,'rt') as f:
    lines = f.readlines()
    for line in lines:
        name=str(line.strip())
        if(name.endswith('.pdf')):
            print(name)
        else:
            os.remove(name)



       
        



