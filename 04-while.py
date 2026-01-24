import os

x=0
tem=''

while x < 10:
    tem+=str(x)+"+"
    x+=1
    
os.system('cls')    
print(tem)