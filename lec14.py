# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:22:12 2024

@author: tack1
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# 平均


def getMean(data):
    matrix_mean = np.mean(data, axis=0)
    print(f"検査値ごとの平均:{matrix_mean}")
    return matrix_mean

# 偏差行列


def getDevmatrix(data, mean):
    A = data - mean
    print(f"偏差行列{A}")
    return A

# 偏差平方積和


def getDevSumOfSquares(A):
    S = np.dot(A.T, A)
    print(f"偏差平方和積和:{S}")

    return S


def getData(data_name):
    file_name = data_name + ".csv"
    data = np.loadtxt(file_name, delimiter=',')
    return data


if __name__ == "__main__":

    # CSVを読み込む
    d1 = getData("lec14_1")
    d2 = getData("lec14_2")

    # データ部を取得
    print("健常者データ")
    print(data1)

    mean1 = getMean(data1)

    A1 = getDevmatrix(data1, mean1)

    S1 = getDevSumOfSquares(A1)

    # データ部を取得
    print("患者データ")
    print(data2)

    mean2 = getMean(data2)

    A2 = getDevmatrix(data2, mean2)

    S2 = getDevSumOfSquares(A2)

    mean = (mean1 + mean2) / 2
    print(f"平均:{mean}")

    n1 = data1.shape[0]
    print(f"自由度(健常者):{n1}")

    n2 = data2.shape[0]
    print(f"自由度(患者):{n2}")

    siguma = (S1 + S2) / ((n1 - 1) + (n2 - 1))
    print(f"Σ:{siguma}")

    x = np.array([80, 100])
    print(x)

    z = (mean1 - mean2) @ np.linalg.inv(siguma) @ (x - mean)
    print(f"マハラノビス距離の二乗{z}")
