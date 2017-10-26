# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:24:07 2017

@author: Vyky
"""
# 0, 1, 1, 2, 3, 5, 8, 13, 21
l = int(input("Dej sem nějaký číslo skřete > "))
x = 0
y = 1
z = 0
for z in range(l):
    z = x + y
    y = x
    x = z
    print(z)
    