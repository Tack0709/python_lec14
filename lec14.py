# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:22:12 2024

@author: tack1
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


if __name__ == "__main__":
    
    data_name = "lec14_test_1"
    
    file_name = data_name + ".csv"

    # CSVを読み込む
    d1 = np.loadtxt(file_name,delimiter=',')
    
    data_name = "lec14_test_2"
    
    file_name = data_name + ".csv"

    # CSVを読み込む
    d2 = np.loadtxt(file_name,delimiter=',')

    #データ部を取得
    print("健常者データ")
    print(d1)
    
# =============================================================================
#     x_11 = d1[:,0]
#     x_12 = d1[:,1]
# =============================================================================
    
    mean1 = np.mean(d1,axis = 0)
    print(f"検査値ごとの平均:{mean1}")
    
    A1 = d1 - mean1
    print(f"偏差行列{A1}")
    
    S1 = np.dot(A1.T,A1)
    print(f"偏差平方和積和:{S1}")
    
    
    
    #データ部を取得
    print("患者データ")
    print(d2)
    
    mean2 = np.mean(d2,axis = 0)
    print(f"検査値ごとの平均:{mean2}")
    
    A2 = d2 - mean2
    print(f"偏差行列{A2}")
    
    S2 = np.dot(A2.T,A2)
    print(f"偏差平方和積和:{S2}")
    
    
    mean = (mean1 + mean2) / 2
    print(f"平均:{mean}")
    
    n1 = d1.shape[0]
    print(f"自由度(健常者):{n1}")
    
    n2 = d2.shape[0]
    print(f"自由度(患者):{n2}")
    
    siguma = (S1 + S2) / ((n1 - 1) + (n2 - 1)) 
    print(f"Σ:{siguma}")
    
    x = np.array([80,100])
    print(x)
    
    z = (mean1 - mean2) @ np.linalg.inv(siguma) @ (x - mean)
    print(z)
# =============================================================================
#     x_21 = d2[:,0]
#     x_22 = d2[:,1]
# =============================================================================
    
# =============================================================================
#     #二つの検査値
#     X1 = np.concatenate((x_11,x_21))
#     X2 = np.concatenate((x_12,x_22))
#     print(f"x1{X1}")
#     print(f"x2{X2}")
#     
#     #平均
#     mean1 = np.mean(X1)
#     mean2 = np.mean(X2)
# =============================================================================
    

    
    #偏差行列
    