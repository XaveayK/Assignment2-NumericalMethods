# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file. For Q2
"""
import numpy as np
import scipy.linalg as lg
import scipy as sp
def QuestionDoooose():
    a = np.array([[21.0,67.0,88.0,73.0],
                  [76.0,63.0,7.0,20.0],
                  [0.0,85.0,56.0,54.0],
                  [19.3,43.0,30.2,29.4]])
    b = np.array([141.0,109.0,218.0,93.7])
    
    a1 = a.astype(np.float32)
    b1 = b.astype(np.float32)
    a2 = a.astype(np.float64)
    x = lg.solve(a1,b1)
    print(x)
    r = (b-a2@x).astype(np.float64).astype(np.float32)
    while np.count_nonzero(r)!=0:
        y = lg.solve(a1, r).astype(np.float64)
        x+=y
        r = (b-(a2@(x)).astype(np.float64)).astype(np.float32)
    print(x)
    return 

def Q3():
    for i in range(1, 11):
        e = 10**(-2*i)
        a = np.array([[e, 1], [1, 1]])
        b = np.array([1+e, 2])
        x = np.array([0.0,0.0])
        a2= a
        b2 = b
        
        a[1][0]=a[0][0]*a[1][0]-a[0][0]
        a[1][1]=a[1][1]*a[0][0]-a[0][1]
        b[1]=b[1]*a[0][0]-b[0]
        x[1]=b[1]/a[1][1]
        x[0]=(b[0]-x[1])/a[0][0]
        
        print(x)
        #Part B
        r=b2-a2@x
        z=sp.linalg.solve(a2, r)
        x+=z
        print(x, '\n')
    return

def Q4():
    n=10
    
    matrix = np.zeros(shape=(n,n))
    matrix2 = np.zeros(shape=(5,n))
    matrix[0][0] = 9
    matrix[0][1] = -4
    matrix[0][2] = 1
    
    matrix2[0][0] = 9
    matrix2[0][1] = -4
    matrix2[0][2] = 1
    
    matrix[1][0] = -4
    matrix[1][1] = 6
    matrix[1][2] = -4
    matrix[1][3] = 1
    
    matrix2[1][0] = -4
    matrix2[1][1] = 6
    matrix2[1][2] = -4
    matrix2[1][3] = 1
    
    matrix[2][0] = 1
    matrix[2][1] = -4
    matrix[2][2] = 6
    matrix[2][3] = -4
    matrix[2][4] = 1
    
    matrix2[2][0] = 1
    matrix2[2][1] = -4
    matrix2[2][2] = 6
    matrix2[2][3] = -4
    matrix2[2][4] = 1
    
    count=1
    for i in range(3,n-3):
        for j in range(0,5):
            matrix[i][j+count] = matrix[2][j]
        count += 1
    
    matrix[3][n-5] = 1
    matrix[3][n-4] = -4
    matrix[3][n-3] = 6
    matrix[3][n-2] = -3
    matrix[3][n-1] = 1
    
    matrix2[3][n-5] = 1
    matrix2[3][n-4] = -4
    matrix2[3][n-3] = 6
    matrix2[3][n-2] = -3
    matrix2[3][n-1] = 1
    
    matrix[2][n-4] = 1
    matrix[2][n-3] = -4
    matrix[n-2][n-2] = 5
    matrix[n-2][n-1] = -2
    
    matrix2[2][n-4] = 1
    matrix2[2][n-3] = -4
    matrix2[2][n-2] = 5
    matrix2[2][n-1] = -2
    
    matrix[n-1][n-3] = 1
    matrix[n-1][n-2] = -2
    matrix[n-1][n-1] = 1
    
    matrix2[1][n-3] = 1
    matrix2[1][n-2] = -2
    matrix2[1][n-1] = 1
    print(matrix)