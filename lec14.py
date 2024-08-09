# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:22:12 2024

@author: tack1
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


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
    print(d1)

    mean1 = np.mean(d1, axis=0)
    print(f"検査値ごとの平均:{mean1}")

    A1 = d1 - mean1
    print(f"偏差行列{A1}")

    S1 = np.dot(A1.T, A1)
    print(f"偏差平方和積和:{S1}")

    # データ部を取得
    print("患者データ")
    print(d2)

    mean2 = np.mean(d2, axis=0)
    print(f"検査値ごとの平均:{mean2}")

    A2 = d2 - mean2
    print(f"偏差行列{A2}")

    S2 = np.dot(A2.T, A2)
    print(f"偏差平方和積和:{S2}")

    mean = (mean1 + mean2) / 2
    print(f"平均:{mean}")

    n1 = d1.shape[0]
    print(f"自由度(健常者):{n1}")

    n2 = d2.shape[0]
    print(f"自由度(患者):{n2}")

    siguma = (S1 + S2) / ((n1 - 1) + (n2 - 1))
    print(f"Σ:{siguma}")

    x = np.array([80, 100])
    print(x)

    z = (mean1 - mean2) @ np.linalg.inv(siguma) @ (x - mean)
    print(f"マハラノビス距離の二乗{z}")
