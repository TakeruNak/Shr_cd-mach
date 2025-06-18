---
title: install_openmx.md
excerpt: <excerpt or description on this script>
author: Takeru Nakashima
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025-06-10 <Takeru Nakashima>. All rights reserved.
---


## 🔧 インストール方法
OpenMXのインストール方法は，公式サイトの[Download](https://www.openmx-square.org/)からダウンロードし，マニュアルのインストルール手順に従ってインストールする．`wget`コマンドを用いて，以下のようにインストールすることも可能である．

```bash
# 0. src directoryを作成
$ mkdir -p ~/src
$ cd ~/src

# 1. Ver. 3.9をインストールし，ソースコードを展開
$ wget https://www.openmx-square.org/openmx3.9.tar.gz
$ tar -xvf openmx3.9.tar.gz

# 2. Ver. 3.9のREADME.txtをダウンロードし，
#    README.txtを参照してインストール手順を確認
$ wget https://www.openmx-square.org/bugfixed/21Oct17/README.txt

# 3. patchデータのダウンロード
$ wget https://www.openmx-square.org/bugfixed/21Oct17/patch3.9.9.tar.gz
$ mv ./patch3.9.9.tar.gz openmx3.9/source
$ cd openmx3.9/source
# tar zxvf patch3.9.9.tar.gz
# mv kpoint.in ../work/

# 4. makefileを以下のように編集してください．
CC = mpicc -O2 -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include \
     -Wno-error=implicit-function-declaration -Dnosse -I/opt/homebrew/opt/fftw/include \
     -I/opt/homebrew/opt/libxc/include \
     -I/opt/homebrew/opt/open-mpi/include
FC = mpif90 -O2 -ffast-math -march=native -fopenmp -Dnosse -fallow-argument-mismatch \
     -I/opt/homebrew/opt/libomp/include \
     -I/opt/homebrew/opt/libxc/include \
     -I/opt/homebrew/opt/open-mpi/include

LIB= -L/opt/homebrew/opt/scalapack/lib -lscalapack -llapack -lblas \
     -L/opt/homebrew/opt/fftw/lib -lfftw3 -lmpi_mpifh -L/opt/homebrew/opt/llvm/lib -lomp -lpthread \
     -L/opt/homebrew/opt/gcc/lib/gcc/current -lgfortran \
     -L/opt/homebrew/opt/open-mpi/lib/ -lmpi_mpifh

# 5. makeコマンドでコンパイル
make clean
make

# 6. インストール完了
make install
cd ../work
ls -l openmx # OpenMXの実行ファイルが生成されていることを確認

```

(最新のmacbookproだと，うまくコンパイルできないことが多いらしい．)

[🏠 Home](../openmx.md)
