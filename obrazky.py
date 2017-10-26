# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:55:26 2017

@author: Vyky
"""
radek = ("*")
mezera = (" ")
n = input("Zadejte počet řádků > ") #musí být liché, jinak bude mít poslední trojúhelník o řádek méně                                  
n = int(n)
m = 1
pamet = n
while n > 0:
    print(n*radek)
    n = n - 1
print()

n = pamet   
while n > 0:
    print((n-1)*mezera, radek*m)
    n = n - 1
    m = m + 2
print()

m = 1
n = pamet
polovina = n/2
while n > polovina:
    print(m*radek)
    m = m + 1
    n = n - 1
m = m - 1    
while n > 0:
    m = m - 1
    n = n - 1
    print(m*radek)
    
    