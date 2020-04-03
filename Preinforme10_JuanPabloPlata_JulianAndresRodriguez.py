# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:47:13 2020

@author: JuanPa
"""
import numpy as np

UPKellogs=np.array([27834, 23789, 30189, 30967, 32501, 32701, 31665, 17155, 4614, 834])#Array usado para calcular el resto de datos que se piden
MKellogs=np.array([27834, 23789, 30189, 30967, 32501, 32701, 31665, 17155, 4614, 834]) #Array usado para calcular la mediana de las utilidades

def sumarPrAños(lista):
    a = (lista[0] + lista[1])/2
    return a
                                       #en estas dos funciones se suman los primeros
def sumarUlAños(lista):                #y los ultimos años para luego sacar su diferencia
    a = (lista [8] + lista [9])/2
    return a

def UtilidadesOperacionales(lista):    #Como su nombre lo dice con esta  funcion se saca
    a = lista.max() - lista.min()      #la diferencia entre el año con mayor utilidad y el 
    return a                           #de menor utilidad

def MedianaUtilidad(lista):
    for i in range(1, len(lista)):
        for j in range(len(lista) - i):
            if lista[j] > lista[j + 1]:    #Con esta funcion se organizan los datos y de
                a = lista[j]               #la tabla ordenada se toman los datos de la 
                lista[j] = lista[j + 1]    #mitad y se dividen en dos para saber la mediana
                lista[j + 1] = a           #de la utilidad
    return (lista[4] + lista [5]) / 2

def PorcentajeUtilidad(lista):
    acumulada = np.sum(lista)             #Con esta funcion conseguimos los porcentajes
    for i in range (len(lista)):          #que aportan cada año a la utilidad total                       
        z = lista[i] / acumulada * 100
        print("El año:", 1 + i,"aporta un ->"+ str(z) + "%")
        
def DeficitUtilidad(lista):
    a = lista[9] - lista[8]               #Aqui se calcula el deficit entre el 2017 y el
    return a                              #año pasado

def DeficitAño(lista):
    for i in range (1, len(lista)):                #Con esta funcion se consiguen los porcentajes de deficit
        z = lista[i] / lista[i-1] * 100 - 100      #y ganancias que se consiguen en las utilidades
        print("El deficit en el año", 1 + i, "es de: " + str(z) + "%")
        
print("La diferencia de la media entre los ultimos dos años y los primeros es: " 
      + str(sumarUlAños(UPKellogs)-sumarPrAños(UPKellogs)), "millones de COP")

print("La diferencia entre el año con mayor utilidad y el año de menor utilidad es: "
      + str(UtilidadesOperacionales(UPKellogs)), "millones de COP")

print("La mediana de la utilidad de Kellogs es: "
      +str(MedianaUtilidad(MKellogs)), "millones de COP")

print("La media de la utilidad de Kellogs es: "
      +str(UPKellogs.sum()/10), "millones de COP")

print("entre el valor de la media y la mediana hay: "
      + str( MedianaUtilidad(MKellogs) - (UPKellogs.sum()/10)), "millones de COP")

print(PorcentajeUtilidad(UPKellogs))

print("El deficit entre el 2017 y el año pasado es de: "
      + str(DeficitUtilidad(UPKellogs)), "millones de COP")

print(DeficitAño(UPKellogs))
