'''
Docstring for practica1

pedir dos numeros

'''

import os

num1=int(input("Dame num1: "))
num2=int(input("Dame num2: "))
tem=''
res=0
x=0

while x < num2:
    x+=1
    tem+=str(num1)+"+"
    res+=num1
    
os.system('cls')
print(tem + "=" + str(res))

