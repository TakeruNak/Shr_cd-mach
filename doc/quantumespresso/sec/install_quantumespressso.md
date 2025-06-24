---
title: install_quantumespressso.md
excerpt: <excerpt or description on this script>
author: Takeru Nakashima
collection: portfolio
date: 2025-06-24
# Copyright (c) 2025-06-24 <Takeru Nakashima>. All rights reserved.
---

# Quantum ESPRESSSO のインストールガイド

## 🍺 使用するパッケージのインストール

Quantum ESPRESSOをmacOSで動かすためには，以下のパッケージをhomebrewを用いてインストールする必要がある．
|---| パッケージ名 | 説明 |
|---|---|---|
| 1 | `open-mpi` | MPI計算を行うためのOpen MPIライブラリ |
| 2 | `gcc` | GNU Compiler Collection (GCC) |
| 3 | `veclibfort` | Fortranのベクトルライブラリ |

1. Homebrewを使用して必要なパッケージをインストールします。
   ```bash
   brew install open-mpi gcc veclibfort
   ```

## 🔧 インストール方法

```
mkdir -p ~/src/quantum-espresso
cd ~/src/quantum-espresso/

wget https://www.quantum-espresso.org/rdm-download/488/v7-4-1/00e9e79464ea139d4bc84b2e452cb797/qe-7.4.1-ReleasePack.tar.gz
tar -xzf qe-7.4.1-ReleasePack.tar.gz
cd qe-7.4.1

# MPI version
./configure MPIF90="mpif90" F90="gfortran" CC=gcc-15 CPP=cpp-15 LAPACK_LIBS="-L/opt/homebrew/Cellar/veclibfort/0.4.3/lib -lveclibFort -lblas -llapack"

# Quantum ESPRESSOのコンパイル
make all

# Quantum ESPRESSOのバイナリを確認
ls -l bin
```
