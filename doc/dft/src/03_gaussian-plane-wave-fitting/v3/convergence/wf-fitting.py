#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: wf-fitting.py
Description: <Description on this script>
Author: Takeru Nakashima
Date: 2026-03-23

Copyright (c) 2026-03-23 <Takeru Nakashima>. All rights reserved.
"""

import numpy as np
import matplotlib.pyplot as plt

# =========================
# Parameters
# =========================
L = 20.0
N = 400
x = np.linspace(-L, L, N)
dx = x[1] - x[0]

# =========================
# Gaussian
# =========================
def gaussian(x, A=1.0, x0=0.0, sigma=1.0):
    return A * np.exp(-(x - x0)**2 / (2 * sigma**2))

wf_x = gaussian(x)

# =========================
# Another Gaussian (for testing)
# ========================
# def wf(x):
#     return gaussian(x, A=1.0, x0=0.0, sigma=1.0) + 0.5 * gaussian(x, A=0.5, x0=3.0, sigma=0.5)
# wf_x = wf(x)

# =========================
# Function: plane wave expansion
# =========================
def plane_wave_expand(E_cut):

    # k_max from energy
    k_max = np.sqrt(2 * E_cut)

    # allowed k (periodic box)
    n_max = int(np.floor(k_max * L / (2*np.pi)))
    n_vals = np.arange(-n_max, n_max+1)
    k_vals = 2 * np.pi * n_vals / (2*L)

    # coefficients
    c_k = np.array([
        np.sum(wf_x * np.exp(-1j * k * x)) * dx / (2*L)
        # np.sum(g_x * np.exp(-1j * k * x)) * dx / (2*L)
        for k in k_vals
    ])

    # reconstruction
    g_fit = np.sum(
        c_k[:, None] * np.exp(1j * k_vals[:, None] * x),
        axis=0
    )

    return g_fit, k_vals

# =========================
# Convergence study
# =========================
E_list = [0.5, 1, 2, 5, 10, 20]
errors = []

plt.figure(figsize=(10, 6))

# original
plt.plot(x, wf_x, 'k', linewidth=2, label="Original Gaussian")
# plt.plot(x, g_x, 'k', linewidth=2, label="Original Gaussian")
for E_cut in E_list:
    g_fit, k_vals = plane_wave_expand(E_cut)

    # --- error (RSE) ---
    error = np.linalg.norm(np.real(g_fit) - wf_x) / np.linalg.norm(wf_x)
    # error = np.linalg.norm(np.real(g_fit) - g_x) / np.linalg.norm(g_x)
    errors.append(error)

    # --- plot ---
    plt.plot(x, np.real(g_fit), '--', label=f"E_cut={E_cut}")

def error_checker(E_cut,errors):
    # Here, print the energy cutoff and the corresponding relative squared error
    print("Energy Cutoff (E_cut) and Relative Squared Error (RSE):")
    print("E_cut\tRSE")
    for E_cut, error in zip(E_list, errors):
        print(f"{E_cut:.2f}\t{error:.2e}")
    
error_checker(E_list, errors)

plt.title("Plane Wave Expansion Convergence")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(loc="upper right")
plt.savefig("convergence_wave.png", dpi=300)
plt.show()
plt.close()

# =========================
# Error vs E_cut
# =========================
plt.figure(figsize=(8, 5))
plt.semilogy(E_list, errors, 'o-')

plt.xlabel("Energy cutoff (E_cut)")
plt.ylabel("Relative error (RSE)")
plt.title("Convergence vs Energy Cutoff")

plt.grid()
plt.savefig("convergence.png", dpi=300)
plt.show()
plt.close()
