---
title: "OpenMX のインストールガイド（macOS）"
excerpt: "Homebrew で依存パッケージを揃え，makefile を編集して OpenMX 3.9 を macOS 上にビルドする手順."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [💡 計算技術](../../README.md) › [OpenMX](../openmx.md)

# OpenMX のインストールガイド（macOS）

次の3ステップで OpenMX を macOS に導入する．

1. **依存パッケージの準備** — Homebrew で MPI・線形代数・FFT のライブラリを入れる
2. **ビルド** — `makefile` のコンパイラ設定を書き換えて `make`
3. **動作確認** — 水分子を1本流して出力を確認する

> ⚠️ 本手順は Apple Silicon（`/opt/homebrew` 配下）を前提に書いている．
> Intel Mac の場合はパスを `/usr/local` に読み替えること．

---

## 1. 🍺 依存パッケージのインストール

| # | パッケージ | 役割 |
|---|---|---|
| 1 | `open-mpi` | MPI 並列計算用のライブラリ |
| 2 | `libomp` | OpenMP 並列計算用のライブラリ |
| 3 | `scalapack` | 並列線形代数（固有値問題の求解） |
| 4 | `fftw` | 高速フーリエ変換 |
| 5 | `gcc` | GNU Compiler Collection（`gfortran` を含む） |
| 6 | `llvm` | `libomp` のリンクに使う Clang ツールチェーン |
| 7 | `vesta` | 出力（電子密度など）の可視化 |
| 8 | `wget` | ソースコードの取得 |
| 9 | `libxc` | 交換相関汎関数のライブラリ（OpenMX には必須ではない） |

```bash
brew install open-mpi libomp libxc scalapack fftw gcc llvm vesta wget
```

> 💬 `libxc` は OpenMX のビルドには不要だが，Quantum ESPRESSO など他のコードで使うため入れておいて損はない．
> すでに入っているパッケージはコマンドから省いてよい．

Homebrew 自体が未導入の場合は，先に [🍺 Homebrew のインストール](../../../04_IT/env4mac/sec/homebrew.md) を参照．

**インストールに失敗する場合**，多くは Xcode（Command Line Tools）のバージョンが古いことが原因である．
Xcode を最新版に更新したうえで再試行し，それでも解決しない場合は Homebrew の出力メッセージに従って対処する．

## 2. 🔧 ソースコードの取得とビルド

ソースコードは公式サイトの [Download](https://www.openmx-square.org/) から取得する．
以下は `wget` でコマンドラインから取得する手順である．

### 2.1 ソースと修正パッチの展開

```bash
# 0. Homebrew を最新化し，作業用ディレクトリを作成
brew update
brew doctor
mkdir -p ~/src && cd ~/src

# 1. Ver. 3.9 の取得と展開
wget https://www.openmx-square.org/openmx3.9.tar.gz
tar -xvf openmx3.9.tar.gz

# 2. バグ修正パッチの README を取得（手順の最新情報はここに書かれている）
wget https://www.openmx-square.org/bugfixed/21Oct17/README.txt

# 3. パッチの適用
wget https://www.openmx-square.org/bugfixed/21Oct17/patch3.9.9.tar.gz
mv ./patch3.9.9.tar.gz openmx3.9/source
cd openmx3.9/source
tar zxvf patch3.9.9.tar.gz
mv kpoint.in ../work/
```

### 2.2 `makefile` の編集

`~/src/openmx3.9/source/makefile` を開き，`CC` / `FC` / `LIB` の3変数を以下のように書き換える．

```makefile
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
```

さらに，`LIBELPADIR` のインクルード指定に `-fcommon` を追加する．

```diff
-CC    += -I$(LIBELPADIR)
+CC    += -I$(LIBELPADIR) -fcommon
```

> ⚠️ **上記のバージョン番号はそのままでは通らない．**
> Homebrew のパッケージは頻繁に更新されるため，`ls /opt/homebrew/Cellar/<package>/` で
> 実際に入っているバージョンを確認し，自分の環境の値に置き換えること．

### 2.3 コンパイル

```bash
make clean   # 念のため以前のビルドをクリーンアップ
make all
make install

cd ../work
ls -l openmx   # 実行ファイルが生成されていることを確認
```

リンクされている共有ライブラリを確認したい場合は `otool -L openmx` を使う．

## 3. ✅ 動作確認：水分子の計算

付属のサンプル入力 `H2O.dat` を使って，1本流してみる．

```bash
# 0. テスト用ディレクトリを作成
mkdir -p ~/test_openmx/input && cd ~/test_openmx

# 1. サンプル入力をコピー
cp ~/src/openmx3.9/work/H2O.dat ./input/H2O.dat

# 2. 擬ポテンシャル・基底データの場所を指定
#    入力ファイル中の DATA.PATH 行を，実際の DFT_DATA19 のパスに書き換える
sed -i '' "s|^DATA.PATH.*|DATA.PATH  $HOME/src/openmx3.9/DFT_DATA19|" ./input/H2O.dat
grep DATA.PATH ./input/H2O.dat   # 書き換わったことを確認
```

次に，実行用のスクリプト `go.sh` を用意する．
ターミナルに直接コマンドを打っても動くが，外部計算機ではジョブスクリプトを書くことになるため，
ここで練習しておくとよい．

```bash
#!/bin/bash
# OpenMX 実行スクリプト
# -np : MPI プロセス数，-nt : OpenMP スレッド数
mpirun -np 1 ~/src/openmx3.9/work/openmx ./input/H2O.dat -nt 1 > ./output.std
```

```bash
chmod 744 go.sh
./go.sh
```

> 💬 初回の `mpirun` 実行時に，macOS からネットワーク接続の許可を求められることがある．許可してよい．

### 3.1 並列数（`-np` と `-nt`）の意味

並列計算には **MPI** と **OpenMP** の2通りがあり，`-np` と `-nt` はそれぞれに対応する．

| オプション | 指定するもの | 単位の性質 |
|---|---|---|
| `-np` | MPI プロセス数 | 独立した実行単位．メモリ空間を共有**しない** |
| `-nt` | OpenMP スレッド数 | プロセス内の実行単位．同じメモリ空間を**共有する** |

> 💡 **イメージ**：Mac の中には複数の小さなパソコン（CPU コア）が入っている．
> 小さなパソコン同士に仕事を分けるのが MPI，1つの小さなパソコンの中で仕事を分けるのが OpenMP．

詳細は [並列計算の利用方法](../../parallel_computing/parallel_computing_guide.md) を参照．

### 3.2 出力の確認

計算が終わると `output.std` のほか，系名を接頭辞とした各種ファイルが生成される．

```bash
vim h2o.out          # 全エネルギー・構造などの主要な結果
open h2o.tden.cube   # 全電子密度を VESTA で可視化
```

## 4. ⚠️ うまくいかないとき

OpenMX のビルドは macOS のバージョンとコンパイラの組み合わせに敏感で，特に新しい macOS では
コンパイルエラーが起きやすい（最新の MacBook Pro ではビルドが通りにくいという報告がある）．

* バージョンの組み合わせによって，要求されるライブラリ・コンパイラが異なることがある．
* コンパイルエラーが出た場合は，まず `makefile` のパス指定と依存関係を疑う．
* 解決しない場合は，公式の[マニュアル](https://www.openmx-square.org/openmx_man3.9jp/node1.html)と
  [フォーラム](https://www.openmx-square.org/forum/patio.cgi)を確認する．

---

[⬅️ OpenMX](../openmx.md) ｜ [🏠 Home](../../../../README.md)
