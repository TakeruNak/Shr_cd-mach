#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2サイトハバードモデルのKohn-Sham SCF
"""

import numpy as np
import matplotlib.pyplot as plt

# =========================
# パラメータ
# =========================
t = 1.0
U = 2.0
A = 1.0

max_iter = 100
alpha = 0.7
tol = 1e-8

n1, n2 = 1.0, 0.0

# =========================
# ポテンシャル
# =========================
def V_H(n):
    return U * n

def V_xc(n):
    return -A * np.sqrt(max(n, 1e-12))

def V_eff(n):
    return V_H(n) + V_xc(n)

# =========================
# 初期履歴
# =========================
history_n1 = [n1]
history_n2 = [n2]
history_vxc1 = [V_xc(n1)]
history_vxc2 = [V_xc(n2)]
history_totalN = [n1 + n2]

history_energy = []
history_residual = []

# =========================
# SCF step
# =========================
def scf_step(n1, n2):
    H = np.array([
        [V_eff(n1), -t],
        [-t, V_eff(n2)]
    ])

    eigvals, eigvecs = np.linalg.eigh(H)
    psi = eigvecs[:, 0]
    energy_ks = eigvals[0]

    new_n1 = abs(psi[0])**2
    new_n2 = abs(psi[1])**2

    return new_n1, new_n2, energy_ks

# =========================
# エネルギー=
# Kohn-Sham 固有値 - ハートリーエネルギー + 交換相関エネルギー
# =========================
def total_energy(n1, n2, energy_ks):
    E_H = 0.5 * U * (n1**2 + n2**2)
    E_xc = - (2/3) * A * (n1**1.5 + n2**1.5)
    return energy_ks - E_H + E_xc

# =========================
# SCFループ
# =========================
for i in range(max_iter):

    new_n1, new_n2, energy_ks = scf_step(n1, n2)

    mixed_n1 = alpha * new_n1 + (1 - alpha) * n1
    mixed_n2 = alpha * new_n2 + (1 - alpha) * n2

    residual = np.sqrt((mixed_n1 - n1)**2 + (mixed_n2 - n2)**2)
    E_tot = total_energy(mixed_n1, mixed_n2, energy_ks)

    # 更新
    n1, n2 = mixed_n1, mixed_n2

    # 履歴（すべて同タイミングで記録）
    history_n1.append(n1)
    history_n2.append(n2)
    history_vxc1.append(V_xc(n1))
    history_vxc2.append(V_xc(n2))
    history_totalN.append(n1 + n2)

    history_energy.append(E_tot)
    history_residual.append(residual)

    if residual < tol:
        print(f"Converged at iteration {i}")
        break

# =========================
# プロット
# =========================

# 密度
plt.figure()
plt.plot(history_n1, marker='o', label='n1')
plt.plot(history_n2, marker='s', label='n2')
plt.xlabel('Iteration')
plt.ylabel('Density')
plt.legend()
plt.grid()
plt.savefig("density.png", dpi=300)

# エネルギー
plt.figure()
plt.plot(history_energy, marker='o')
plt.xlabel('Iteration')
plt.ylabel('Energy')
plt.grid()
plt.savefig("energy.png", dpi=300)

# 残差
plt.figure()
plt.plot(history_residual, marker='o')
plt.yscale('log')
plt.xlabel('Iteration')
plt.ylabel('Residual')
plt.grid()
plt.savefig("residual.png", dpi=300)

# Vxc (iteration)
plt.figure()
plt.plot(history_vxc1, marker='o', label='Vxc1')
plt.plot(history_vxc2, marker='s', label='Vxc2')
plt.xlabel('Iteration')
plt.ylabel('V_xc')
plt.legend()
plt.grid()
plt.savefig("vxc.png", dpi=300)

# 粒子数保存
plt.figure()
plt.plot(history_totalN, marker='o')
plt.axhline(y=1.0, linestyle='--')
plt.xlabel('Iteration')
plt.ylabel('Total N')
plt.grid()
plt.savefig("totalN.png", dpi=300)

# =========================
# V_xc vs density
# =========================
n_vals = np.linspace(0.0, 1.5, 200)
vxc_vals = [V_xc(n) for n in n_vals]

plt.figure()
plt.plot(n_vals, vxc_vals, label='V_xc(n)')
plt.scatter(history_n1, history_vxc1, label='site1')
plt.scatter(history_n2, history_vxc2, label='site2')
plt.xlabel('Density')
plt.ylabel('V_xc')
plt.legend()
plt.grid()
plt.savefig("vxc_vs_density.png", dpi=300)

# =========================
# V_eff vs density
# =========================
veff_vals = [V_eff(n) for n in n_vals]
veff1 = [V_eff(n) for n in history_n1]
veff2 = [V_eff(n) for n in history_n2]

plt.figure()
plt.plot(n_vals, veff_vals, label='V_eff(n)')
plt.scatter(history_n1, veff1, label='site1')
plt.scatter(history_n2, veff2, label='site2')
plt.xlabel('Density')
plt.ylabel('V_eff')
plt.legend()
plt.grid()
plt.savefig("veff_vs_density.png", dpi=300)

plt.show()
