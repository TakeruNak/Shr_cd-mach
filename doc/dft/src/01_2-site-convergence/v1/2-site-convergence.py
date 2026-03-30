#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: 2-site-convergence.py
Description: 2サイトハバードモデルの自己無撞着計算の収束過程を示すコード。ミキシングを導入して、発散や対称性破れを防止しながら収束させる様子を可視化します。
Author: Takeru Nakashima
Date: 2026-03-19

Copyright (c) 2026-03-19 <Takeru Nakashima>. All rights reserved.

"""

import numpy as np
import matplotlib.pyplot as plt

# =========================
# パラメータ設定
# =========================
t = 1.0          # ホッピングパラメータ
U = 2.0          # ← ここを 大きくしたり小さくしたりすると発散が見やすい
max_iter = 10000 # 最大反復回数
alpha = 0.5      # ミキシング係数（0〜1）この値を小さくすると収束が遅くなりますが、発散を防止できます。大きくすると収束が速くなりますが、発散しやすくなります。
tol = 1e-6       # 収束判定

# 初期値（非対称にするのがポイント）
n1, n2 = 1.0, 0.0

# 履歴保存
history_n1 = [n1]
history_n2 = [n2]
history_energy = []
history_diff = []

# =========================
# SCF 1ステップ
# =========================
def scf_step(n1, n2):
    H = np.array([
        [U * n1, -t],
        [-t, U * n2]
    ])

    eigvals, eigvecs = np.linalg.eigh(H)

    # 基底状態
    psi = eigvecs[:, 0]
    energy = eigvals[0]

    # 密度
    new_n1 = abs(psi[0])**2
    new_n2 = abs(psi[1])**2

    return new_n1, new_n2, energy

# =========================
# SCFループ
# =========================
for i in range(max_iter):
    new_n1, new_n2, energy = scf_step(n1, n2)

    # ミキシング（重要）
    mixed_n1 = alpha * new_n1 + (1 - alpha) * n1
    mixed_n2 = alpha * new_n2 + (1 - alpha) * n2

    # 履歴保存
    history_n1.append(mixed_n1)
    history_n2.append(mixed_n2)
    history_energy.append(energy)
    # 差分（収束指標）
    diff = max(abs(mixed_n1 - n1), abs(mixed_n2 - n2))
    history_diff.append(diff)

    # 収束判定
    if abs(mixed_n1 - n1) < tol and abs(mixed_n2 - n2) < tol:
        print(f"Converged at iteration {i}")
        print(f"Final densities: n1 = {mixed_n1:.6f}, n2 = {mixed_n2:.6f}")
        break

    # 更新
    n1, n2 = mixed_n1, mixed_n2

# =========================
# プロット
# =========================

# --- 密度の収束 ---
plt.figure()
plt.plot(history_n1, marker='o', label='n1')
plt.plot(history_n2, marker='s', label='n2')
plt.xlabel('Iteration')
plt.ylabel('Density')
plt.title('SCF Convergence (Density)')
plt.legend()
plt.grid()

plt.savefig("density.png", dpi=300)

# --- エネルギーの収束 ---
plt.figure()
plt.plot(history_energy, marker='o')
plt.xlabel('Iteration')
plt.ylabel('Energy')
plt.title('SCF Convergence (Energy)')
plt.grid()

plt.savefig("energy.png", dpi=300)

# --- 残差の収束 ---
plt.figure()
plt.plot(history_diff, marker='o')
plt.xlabel('Iteration')
plt.ylabel('Residual (|Δn|)')
plt.title('SCF Convergence (Residual)')
plt.yscale('log')   
plt.grid()

plt.savefig("residual.png", dpi=300, bbox_inches='tight')

plt.show()
