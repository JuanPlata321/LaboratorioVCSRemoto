# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:34:01 2020

@author: JuanPa
"""
#%% Punto 19

x1 = float(input("Ingrese la coordenada x1: "))
x2 = float(input("Ingrese la coordenada x2: "))
y1 = float(input("Ingrese la coordenada y1: "))
y2 = float(input("Ingrese la coordenada y2: "))

print("la distancia euclidiana es: "+ str(((x2-x1)**2+(y2-y1)**2)**(1/2)))

#%% Punto 23

n = int(input("Ingrese el número de 4 cifras: "))

if 999<n<10000:
    n1 = n//1000
    n2 = n%1000//100
    n3 = n%100//10
    n4 = n%10

    m = n4*10**3+n3*10**2+n2*10**1+n1

    print("El número inverso es: "+ str(m))
else:
    print("El número no es valido")

#%% Punto 30

c1 = float(input("Ingrese la primera nota: "))
c2 = float(input("Ingrese la segunda nota: "))
c3 = float(input("Ingrese la tercera nota: "))
c4 = float(input("Ingrese la cuarta nota: "))
c5 = float(input("Ingrese la quinta nota: "))

rf = (c1*15/100)+(c2*20/100)+(c3*15/100)+(c4*30/100)+(c5*20/100)

if 0<rf<5.1:
    if rf>=4.5:
         print("Felicidades, saco una alta nota en el curso")
         
    if 4.5>rf>=3.0:
        print("El estudiante aprobo")
        
    if 2.0<=rf<3.0:
        print("El estudiante reprobo, pero podra habilitar")
    
    if rf<2.0:
        print ("El estudiante no podra habilitar")
    
else:
    print("Las notas ingresadas no son validas")
    
#%% Punto 60

r = 0
s = 0
p = 0
n = 0
f = int(input("Ingrese el número de filas: "))

while n!=f:
    n = n + 1
    s = s + 10**p
    r = s + r
    p = p + 1
    print(r)
