#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipenv で入れた numpy が動くかを確認するためのスクリプト.

使い方:
    pipenv install numpy
    pipenv run python test.py
"""

import numpy as np

# --- 1. ベクトルの足し算 ---
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print("c:", c)

# --- 2. 固有値問題を解く ---
# ex: A = [[1, 2], [3, 4]]
A = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)
