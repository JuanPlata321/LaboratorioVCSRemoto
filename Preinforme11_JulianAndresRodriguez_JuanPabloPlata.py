# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:09:19 2020

@author: JuanPa
"""

import numpy as np
def gaussJordan(matriz, vector):

    matrix = np.array(matriz, dtype=np.float64)
    vector = np.array(vector, dtype=np.float64)

    m = len(vector)
    x = np.zeros(m)

    for k in range(0, m):
        for r in range(k+1, m):
            factor=(matrix[r,k]/matrix[k,k])
            vector[r]=vector[r]-(factor*vector[k])
            for c in range(0,m):
                matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])

    x[m-1]=vector[m-1]/matrix[m-1, m-1]

    for r in range(m-2, -1, -1):
        suma = 0
        for c in range(0,m):
            suma=suma+matrix[r,c]*x[c]
        x[r]=(vector[r]-suma)/matrix[r, r]  
    return x

print(gaussJordan([[16.98,9,9],[15.90,8.72,8.52],[14.08,8.20,8.76]],[138900,131220,121280]))
