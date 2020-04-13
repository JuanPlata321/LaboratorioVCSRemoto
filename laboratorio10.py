# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:50:59 2020

@author: JuanPa
"""



a = int(input("introduce el numero base: "))
b = int(input("introduce el exponente: "))

def a_power_b(a, b):
    acum = 0
    mult = 0
    for i in range(0, b-1, 1):
        mult = a * a
        acum = mult + acum
    return acum
    print(acum)

print("El resultado de la potencia es: "+ str(a_power_b(a, b)))
