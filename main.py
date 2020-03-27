# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:12:19 2020

@author: JuanPa
"""
#%% Punto 1
a = float(input("Ingrese el número a: "))
c = float(input("Ingrese el número c: "))

print("El resultado de a por c es: " + str (a*c))
print("El doble del número a es: " + str (a*2))

#%% Punto 2

b = float(input("Ingrese el número b: "))
d = float(input("Ingrese el número d: "))

print("El cuadrado de b es: "+ str(b**2))
print("La raiz cuadrada de d es: "+ str(d**(1/2))) 

#%% Punto 3

a = float(input("Ingrese el número a: "))
b = float(input("Ingrese el número b: "))
c = float(input("Ingrese el número c: "))
d = (-4*a*c+b**2)**0.5

if ((-4*a*c+b**2))<0:
    print("La ecuación no tiene solución")
else:
    if d>0:
        print("La solucion de la ecuación cuadrática positiva es: "+ str((-b+(d))/(2*a)))
        print("La solucion de la ecuación cuadrática negativa es: "+ str((-b-(d))/(2*a)))

    if d==0:
        print("X1 y X2 son iguales y corresponden a -b/2a: ")