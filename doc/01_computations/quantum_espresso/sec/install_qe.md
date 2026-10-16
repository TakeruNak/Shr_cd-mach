---
title: "Quantum ESPRESSO のインストールガイド（macOS）"
excerpt: "QE 7.5 を macOS (Apple Silicon) 上にビルドする手順と，実際に踏んだビルドエラーの回避策."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-24
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [💡 計算技術](../../README.md) › [Quantum ESPRESSO](../quantum_espresso.md)

# Quantum ESPRESSO のインストールガイド（macOS）

> 本ページの手順は **QE 7.5 / macOS 15.7.9 (Apple Silicon, arm64)** で実際に最後まで通して確認している．
> 確認時のツールチェーンは Homebrew の open-mpi 5.0.9 / gcc 15.2.0 / veclibfort 0.4.3 / libxc 7.0.0．

## 🍺 使用するパッケージのインストール

Quantum ESPRESSOをmacOSで動かすためには，以下のパッケージをhomebrewを用いてインストールする必要がある．

| # | パッケージ名 | 説明 |
|---|---|---|
| 1 | `open-mpi` | MPI計算を行うためのOpen MPIライブラリ |
| 2 | `gcc` | GNU Compiler Collection (GCC) |
| 3 | `veclibfort` | Fortranのベクトルライブラリ |
| 4 | `wget` | ファイルをダウンロードするためのツール |
| 5 | `libxc` | 交換相関汎関数のライブラリ （Optional）|

Homebrewを使用して必要なパッケージをインストールする．
   ```bash
   brew install open-mpi gcc veclibfort wget libxc
   ```

`libxc` を使わない場合は末尾の `libxc` を外してよい．ただしその場合は後述の configure から
`--with-libxc` 系のオプションも必ず外すこと．

もし，Homebrewがインストールされていない場合は，次のHomebrewのインストールについて記述した[🍺 ページ 🍺](../../../04_IT/env4mac/sec/homebrew.md)を参照してインストールを行うこと．


## 🔧 インストール方法

Quantum ESPRESSOのインストールには，downloadサイトへの登録が必要です．[downloadサイト](https://www.quantum-espresso.org/download-page/)にアクセスし，アカウントを作成してから，以下の手順に従ってください.

```bash
# 0. Quantum ESPRESSOのインストールディレクトリを作成
mkdir -p ~/src/quantum-espresso

# 1. Quantum ESPRESSOのソースコードをダウンロード
cd ~/src/quantum-espresso/
wget [Quantum ESPRESSOのSRCのダウンロードリンク（downloadページからコピー）]

# 2. ダウンロードしたファイルを解凍
tar -xzf qe-7.5-ReleasePack.tar.gz
cd qe-7.5

# 3. MPI versionのコンパイルを行うために必要な環境変数を設定
./configure --with-libxc --with-libxc-prefix='/opt/homebrew/opt/libxc' MPIF90="mpif90" F90="gfortran" CC=gcc-15 CPP=cpp-15 LAPACK_LIBS="-L/opt/homebrew/lib -lveclibFort -lblas -llapack"
# libxcを使用しない場合は，以下のようにしてconfigureを行う．
./configure MPIF90="mpif90" F90="gfortran" CC=gcc-15 CPP=cpp-15 LAPACK_LIBS="-L/opt/homebrew/lib -lveclibFort -lblas -llapack"

# 成功すると DFLAGS = -D__FFTW -D__LIBXC -D__MPI -D__MPI_MODULE と表示される．
# gcc-15 / cpp-15 のバージョン番号は Homebrew の gcc の更新で変わるので，
# `ls /opt/homebrew/bin/gcc-*` で実在するものに合わせること．

# 4. ★ 先に下記「よくあるビルドエラー」の 4.1〜4.3 に目を通すこと ★
make -j8 all

# 5. install directoryの指定
# makefileの中でPREFIXを指定することで，インストール先を変更できる．
make install PREFIX=../

# 6. Quantum ESPRESSOのバイナリを確認
cd ../bin
ls -l
# おそらく，pw.x, ph.x, etc. のようなバイナリファイルが表示されるはず．

# 補足）PWscfに関する計算例は，PW directoryの中にあるexamplesディレクトリにいくつか入っているので，そちらを参考にするのも一つの手．
```


## ⚠️ よくあるビルドエラー

いずれも QE 7.5 / macOS で実際に踏んだもの．

### 4.1 `w90lib` で止まる（wannier90）

初回の `make all` が以下で停止する．

```
fatal: 'origin' does not appear to be a git repository
make[1]: *** [w90lib] Error 128
```

原因はリリースパックの `.gitmodules` に wannier90 のエントリが無く，`install/install_utils` の
`update_submodule` が**空のURLに対して `git fetch` を実行してしまう**ため．

**wannier90 のソースは tarball に同梱済みなので，手動で clone し直す必要はない．**
`make` の前に空の `.git` を作っておけば submodule 初期化がスキップされて通る．

```bash
mkdir -p external/wannier90/.git
```

（なお，エラーで停止した際にも空の `external/wannier90/.git` が作られるため，
そのまま `make all` を再実行すると2回目は通る．上はそれを先回りしているだけである．）

wannier90 を使わないのであれば，PWscfと中核となるコードのみをビルドしてもよい．

```bash
make pwall
```

### 4.2 `pioud` で止まる（`-pg` 非対応）

macOS では `-pg` がサポートされていないため，`PIOUD/src/Makefile` の2行をコメントアウトする．

```diff
-F90FLAGS += -pg
-LDFLAGS += -pg
+# F90FLAGS += -pg
+# LDFLAGS += -pg
```

### 4.3 `make install` が実行ファイルを壊す（macOS 固有・QE本体のバグ）

**エラーは出ないが，インストールされたバイナリが壊れるので注意が必要．**

ルートの `Makefile` の `install` ターゲットは `*.x` を `find` で集めるが，macOS で生成される
デバッグ情報 `*.dSYM/Contents/Resources/DWARF/*.x` も拾ってしまい，**本物の実行ファイルを
上書きする**．実際に `wannier90.x` が 68KB の dSYM companion に置き換わった．

```diff
-	for x in `find * ! -path "test-suite/*" -name *.x -type f` ; do \
+	for x in `find * ! -path "test-suite/*" ! -path "*.dSYM/*" -name *.x -type f` ; do \
```

パッチを当てずにインストールしてしまった場合も含め，インストール後に必ず検証しておくとよい．
Mach-O 実行ファイル以外が出てこなければ正常である．

```bash
file <PREFIX>/bin/* | grep -v "Mach-O 64-bit executable arm64"
```

### 4.4 `-lblas` の重複警告

リンクのたびに以下が大量に出るが，**ビルドは正常に完了する**ので無視してよい．

```
ld: warning: ignoring duplicate libraries: '-lblas'
```

上記 configure の `LAPACK_LIBS` に含まれる `-lblas` が，configure が自動設定する
`BLAS_LIBS = -lblas` と重複するために出る．`LAPACK_LIBS` から `-lblas` を外せば
解消すると思われるが，**その構成はまだ検証していない**．


## 🧪 動作確認

`PREFIX` 配下の `bin/` にバイナリが揃ったら，簡単な系で1本流して確認する．
同梱の ONCV 擬ポテンシャル（`QEHeat/examples/pseudo/`）を使えば追加のダウンロードは要らない．

```bash
mpirun -np 4 <PREFIX>/bin/pw.x -in si.scf.in
```

確認時の参考値として，Si（ダイヤモンド構造，`ibrav=2`, `celldm(1)=10.20`, `ecutwfc=25`,
4x4x4 k-points, ONCV PBE）の全エネルギーは以下であった．

| `input_dft` | total energy |
|---|---|
| `PBE`（QE内蔵） | -15.74870539 Ry |
| `XC-000i-000i-101l-130l-000i-000i`（libxc経由のPBE） | -15.74870377 Ry |

両者が 1e-6 Ry の精度で一致していれば，libxc の実行時リンクも正常に効いている．

より本格的なチュートリアルは
http://www.cmpt.phys.tohoku.ac.jp/~koretsune/SATL_qe_tutorial/
などを参照．

[⬅️ Quantum ESPRESSO](../quantum_espresso.md) ｜ [🏠 Home](../../../../README.md)
