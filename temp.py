# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file. For Q2
"""
import numpy as np
import scipy.linalg as lg
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