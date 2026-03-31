---
title: install_quantumespressso.md
excerpt: Quantum ESPRESSOのインストール方法について説明します．
author: Takeru Nakashima
collection: portfolio
date: 2025-06-24
# Copyright (c) 2025-06-24 <Takeru Nakashima>. All rights reserved.
---
[🏠 Home](../quantumespressso.md)

# Quantum ESPRESSSO のインストールガイド

## 🍺 使用するパッケージのインストール

Quantum ESPRESSOをmacOSで動かすためには，以下のパッケージをhomebrewを用いてインストールする必要がある．
|---| パッケージ名 | 説明 |
|---|---|---|
| 1 | `open-mpi` | MPI計算を行うためのOpen MPIライブラリ |
| 2 | `gcc` | GNU Compiler Collection (GCC) |
| 3 | `veclibfort` | Fortranのベクトルライブラリ |
| 4 | `wget` | ファイルをダウンロードするためのツール |

Homebrewを使用して必要なパッケージをインストールする．
   ```bash
   brew install open-mpi gcc veclibfort wget
   ```

もし，Homebrewがインストールされていない場合は，次のHomebrewのインストールについて記述した[🍺 ページ 🍺](../../env4mac/sec/homebrew.md)を参照してインストールを行うこと．


## 🔧 インストール方法

Quantum ESPRESSOのインストールには，downloadサイトへの登録が必要です．[downloadサイト](https://www.quantum-espresso.org/download-page/)にアクセスし，アカウントを作成してから，以下の手順に従ってください.

```
# 0. Quantum ESPRESSOのインストールディレクトリを作成
mkdir -p ~/src/quantum-espresso

# 1. Quantum ESPRESSOのソースコードをダウンロード
cd ~/src/quantum-espresso/
wget [Quantum ESPRESSOのSRCのダウンロードリンク（downloadページからコピー）]

# 2. ダウンロードしたファイルを解凍
tar -xzf qe-7.4.1-ReleasePack.tar.gz
cd qe-7.4.1

# 3. MPI versionのコンパイルを行うために必要な環境変数を設定
./configure MPIF90="mpif90" F90="gfortran" CC=gcc-15 CPP=cpp-15 LAPACK_LIBS="-L/opt/homebrew/Cellar/veclibfort/0.4.3/lib -lveclibFort -lblas -llapack"

# 4. Quantum ESPRESSOのコンパイル
make all

# 4.1 もしコンパイルエラーが発生した場合は，エラーメッセージを確認し，必要に応じて環境変数やライブライのパスを修正．
# 最近の場合だと，wannier90のコンパイルでエラーが出ることがある．その場合は，以下のようにして，wannier90のコンパイルを行う．
# もしくは，wannier90のコンパイルをスキップすることも可能．

# (wannier90をスキップの場合) PWscfと中核となるコードのコンパイルのみを以下のように行う．
makw pwall

# (wannier90をコンパイルする場合) wannier90を手動で再インストールして，コンパイルさせる．
rm -rf external/wannier90
# 手動でクローンする
git clone -b v3.1.0 https://github.com/wannier-developers/wannier90.git external/wannier90
# ここら辺の確認は，時間ができたらちゃんとやります．困ったら，wannier90に関しては，[Wannier90の公式サイト](https://wannier90.org/)を参照し，手でコンパイルするのが一番確実かもしれません．
make all

# 5. install directoryの指定
# makefileの中でPREFIXを指定することで，インストール先を変更できる．
make install PREFIX=../

# 6. Quantum ESPRESSOのバイナリを確認
cd ../bin
ls -l 
# おそらく，pw.x, ph.x, etc. のようなバイナリファイルが表示されるはず．

# 補足）PWscfに関する計算例は，PW directoryの中にあるexamplesディレクトリにいくつか入っているので，そちらを参考にするのも一つの手．
```


## 🧪 動作確認
http://www.cmpt.phys.tohoku.ac.jp/~koretsune/SATL_qe_tutorial/
などのチュートリアルを参考にして，動作確認を行ってください．

**後々，ちゃんと本ページを書きます．**
[🏠 Home](../quantumespressso.md)
