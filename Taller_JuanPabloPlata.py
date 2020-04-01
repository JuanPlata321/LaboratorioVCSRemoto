# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:53:21 2020

@author: JuanPa
"""

import numpy as np

libros = np.array([29.62, 36.88, 22.93, 39.78, 33.15, 18.37, 44.82, 14.29, 11.53, 50.00])

long = len(libros)

minimo = libros[0]
for number in libros:
    if minimo > number:
        minimo = number

maximo = libros[0]
for number in libros:
    if maximo < number:
        maximo = number

def sumarlista(lista):
    Suma = 0
    for i in lista:
        Suma = Suma + i
    return Suma

def sumarListaPares(lista):
    suma = 0
    for i in range(0, long, 2):
        suma = suma + lista[i]
    return suma

def sumarListaImpares(lista):
    suma = 0
    for i in range(1, long, 2):
        suma = suma + lista[i]
    return suma

print ("El minimo de los libros es: "+ str(minimo))
print ("el maximo de los libros es: "+ str(maximo))
print ("El promedio de los 10 libros es: "+ str((sumarlista(libros))/long)) 
print ("La diferencia entre el libro maximo y el minimo es: "+ str((maximo)-(minimo)))
print ("La suma de los libros en posiciones pares es: "
       + str((sumarListaPares(libros))))
print ("La suma de los libros en posiciones impares es: "
       + str(sumarListaImpares(libros)))
    