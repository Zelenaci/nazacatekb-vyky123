# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:30:02 2017

@author: Vyky
"""

import random
s = [random.randint(1,50) for i in range(20)] #seznam kladných celých čísel

print(s)

print("Sudá čísla jsou:")
for x in s:
    if x % 2 == 0:
        print(x, end= " ")
print()
print()
print("Čísla větší než 11 a menší než 19 jsou:")
for x in s:
    if x < 19:
        if x > 11:
            print(x, end= " ")
print()
print()
print("Čísla dělitelné třemi a čtyřmi jsou:")
for x in s:
    if x % 3 == 0:
        if x % 4 == 0:
            print(x, end=" ")
print()
print()           
s2 = [random.randint(-50,50) for i in range(20)]     #seznam celých čísel (i záporných)        
print(s2)
print("Součet kladných čísel je:")
kladsoucet = 0
for cislo in s2:
    if cislo > 0:
        kladsoucet = kladsoucet + cislo
print(kladsoucet)
print()
print("Součet záporných čísel je:")
zapsoucet = 0
for cislo in s2:
    if cislo < 0:
        zapsoucet = zapsoucet + cislo
print(zapsoucet)
print()

mocnina = []
for cislo in s2:
   mocnina.append(cislo*cislo)
   soucetmocnin = sum(mocnina)
print(mocnina)
print("Součet mocnin je:")
print(soucetmocnin)
print()

soucet = 0
for cislo in s:
    soucet = cislo + soucet
print("Součet je:", soucet)
aritm = (soucet/len(s))
print("Aritmetický průměr je:")
print(aritm)