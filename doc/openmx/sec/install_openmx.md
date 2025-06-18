---
title: install_openmx.md
excerpt: <excerpt or description on this script>
author: Takeru Nakashima
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025-06-10 <Takeru Nakashima>. All rights reserved.
---


## 使用するパッケージのインストール
```
brew install open-mpi libomp libxc scalapack fftw gcc llvm vesta
# libxcはとりあえず，入れるだけ入れておきましょう．
```

## 🔧 インストール方法
OpenMXのインストール方法は，公式サイトの[Download](https://www.openmx-square.org/)からダウンロードし，マニュアルのインストルール手順に従ってインストールする．`wget`コマンドを用いて，以下のようにインストールすることも可能である．

```bash
# 0. homebrewの最新版への更新とsrc directoryを作成
brew update
brew doctor

mkdir -p ~/src
cd ~/src

# 1. Ver. 3.9をインストールし，ソースコードを展開
wget https://www.openmx-square.org/openmx3.9.tar.gz
tar -xvf openmx3.9.tar.gz

# 2. Ver. 3.9のREADME.txtをダウンロードし，
#    README.txtを参照してインストール手順を確認
wget https://www.openmx-square.org/bugfixed/21Oct17/README.txt

# 3. patchデータのダウンロード
wget https://www.openmx-square.org/bugfixed/21Oct17/patch3.9.9.tar.gz
mv ./patch3.9.9.tar.gz openmx3.9/source
cd openmx3.9/source
tar zxvf patch3.9.9.tar.gz
mv kpoint.in ../work/

# 4. makefileを以下のように編集してください．
#    makefileの場所は，openmx3.9/source/makefileです．
ls ./makefile  # makefileが存在することを確認

# vim ./makefile を実行して，以下のように編集してください．
# CC, FC, LIBの設定を行います．
CC = mpicc -O3 -Xpreprocessor -fopenmp \
     -I/opt/homebrew/Cellar/libomp/20.1.7/include \
     -Wno-error=implicit-function-declaration -Dnosse \
     -I/opt/homebrew/Cellar/fftw/3.3.10_2/include \
     -I/opt/homebrew/Cellar/open-mpi/5.0.7/include

FC = mpif90 -O3 -ffast-math -march=native -fopenmp -Dnosse -fallow-argument-mismatch

LIB= -L/opt/homebrew/Cellar/scalapack/2.2.2/lib -lscalapack \
     -llapack -lblas \
     -L/opt/homebrew/Cellar/fftw/3.3.10_2/lib -lfftw3_threads -lfftw3 \
     -L/opt/homebrew/Cellar/open-mpi/5.0.7/lib -lmpi_mpifh \
     -L/opt/homebrew/Cellar/llvm/20.1.7/lib -lomp -lpthread \
     -L/opt/homebrew/Cellar/gcc/15.1.0/lib/gcc/15 -lgfortran

# CC のincludeディレクトリの指定部分に，-fcommon オプションを追加します．

# 修正前）CC    += -I$(LIBELPADIR)
CC    += -I$(LIBELPADIR) -fcommon

# 5. makeコマンドでコンパイル
make clean # 念のために，以前のビルドをクリーンアップ
make all

# 6. インストール完了
make install
cd ../work
ls -l openmx # OpenMXの実行ファイルが生成されていることを確認

```

homebrew のパッケージを利用しているので，パッケージのバージョンは各自で確認して，修正してください．

## ✅ 使用例

入力ファイルを用意し，OpenMXを実行する．以下は，水分子の計算例である．

```bash
# 0. Homeディレクトリに移動し，テスト用のディレクトリを作成
cd ~
mkdir -p ./test_openmx
cd ./test_openmx

# 1. OpenMXの構造ファイルをコピー
mkdir input
cp ~/src/openmx3.9/work/H2O.in ./input/H2O.in
cat "data.path ~/src/openmx3.9/DFT_DATA19/" >> ./input/H2O.in
```

ここで，openmxを実行するためのスクリプトファイルを書いてみましょう．`go.sh`という名前で以下の内容を記述します．

```bash
#!/bin/bash
# OpenMXの実行スクリプト
mpirun -np 1 ~/src/openmx3.9/work/openmx ./input/H2O.dat -nt 1 > ./output.std

# 上記の-npオプションは，使用するプロセス数を指定l;
# -ntオプションは，スレッド数を指定する．
# 出力はoutput.stdにリダイレクトされる．
# 必要に応じて-npや-ntの値を変更してください．
```

実行権限を付与して，スクリプトを実行します．

```bash 
chmod 744 go.sh
./go.sh
```
初めての`mpirun`コマンドの実行では，実行許可の確認が求められることがあります．その場合は，許可を与えてください．


計算が終わると，`output.std`を含む出力ファイルが生成されます．
試しに，`vim h2o.out`などで出力ファイルを確認してみましょう．`open h2o.tden.cube`などをterminal上で実行すると，VESTAなどの可視化ツールでH2Oのsimulationで求めたtotal electron densityを確認できます．他にもファイルの中身を確認してみてください．

(*詳しい説明．丁寧な文章の推敲はいづれします．*）

## 注意点
OpenMXのインストールは，macOSのバージョンや使用するコンパイラによって異なる場合がある．特に，最新のmacOSではコンパイルエラーが発生することがあるため，注意が必要．以下の点に留意．
- OpenMXのバージョンによっては，特定のライブラリやコンパイラのバージョンが必要になることがある．
- コンパイル時にエラーが発生した場合は，Makefileの設定や依存関係を確認．
- OpenMXの公式ドキュメントやフォーラムを参照して，最新の情報を確認することをお勧め．


(最新のmacbookproだと，うまくコンパイルできないことが多いらしい．)

[🏠 Home](../openmx.md)
