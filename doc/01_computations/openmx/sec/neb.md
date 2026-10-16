---
title: "Nudged Elastic Band (NEB) 法（OpenMX）"
excerpt: "OpenMX で反応経路探索（NEB 計算）を行うための固有パラメタと，C2H4 の具体例."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [💡 計算技術](../../README.md) › [OpenMX](../openmx.md) › [各種計算ガイド](./calc_method.md)

# Nudged Elastic Band (NEB) 法

NEB 法は，**与えられた始状態と終状態をつなぐ最小エネルギー経路**を求める手法である．
得られた経路上のエネルギー最大点が遷移状態に対応し，その高さが活性化障壁になる．

---

## 1. NEB 固有のパラメタ

NEB 計算は構造最適化計算と多くのパラメタを共有する（[構造最適化](./optimize.md) を参照）．
**NEB に固有で重要なのは次の2つ**である．

| パラメタ | 意味 |
|---|---|
| `MD.NEB.Number.Images` | 始状態と終状態の間に置く**中間状態（image）の個数** |
| `<NEB.Atoms.SpeciesAndCoordinates>` ブロック | **終状態**の原子座標 |

座標の対応関係は以下のとおり．書式は両ブロックで共通である．

| ブロック | 対応する状態 |
|---|---|
| `<Atoms.SpeciesAndCoordinates>` | 始状態（reactant） |
| `<NEB.Atoms.SpeciesAndCoordinates>` | 終状態（product） |

> 💬 中間状態の座標を明示的に与えない場合は，**始状態と終状態を `MD.NEB.Number.Images` の数で
> 線形補間した構造**が初期の image として使われる．

## 2. 入力例（NEB 部分のみ）

```
# ---------------------------------
# NEB: MD or Geometry Optimization
# ---------------------------------

MD.Type                     NEB        # Nomd|Opt|DIIS|NVE|NVT_VS|NVT_NH
MD.Opt.DIIS.History          4         # default=7
MD.Opt.StartDIIS            10         # default=5
MD.maxIter                  100        # default=1
MD.TimeStep                 1.0        # default=0.5 (fs)
MD.Opt.criterion         1.0e-4        # default=1.0e-4 (Hartree/bohr)

MD.NEB.Number.Images         8         # default=10

#
# The coordinates of the product (終状態)
#
<NEB.Atoms.SpeciesAndCoordinates
   1    C   -0.77755846408657   -0.00000003553856   -0.77730141035137     2.0     2.0
   2    C    0.77681707294741   -0.00000002413166   -0.77729608216595     2.0     2.0
   3    H    1.23451821718817   -0.88763832172374   -1.23464057728123     0.5     0.5
   4    H    1.23451823170776    0.88763828275851   -1.23464059022330     0.5     0.5
   5    H   -1.23506432458023   -0.88767426830774   -1.23470899088096     0.5     0.5
   6    H   -1.23506425800395    0.88767424658723   -1.23470896874564     0.5     0.5
   7    C   -0.77755854665393    0.00000000908006    0.77730136931056     2.0     2.0
   8    C    0.77681705017323   -0.00000000970885    0.77729611199476     2.0     2.0
   9    H    1.23451826851556   -0.88763828740000    1.23464060936812     0.5     0.5
  10    H    1.23451821324627    0.88763830875131    1.23464061208483     0.5     0.5
  11    H   -1.23506431230451   -0.88767430754577    1.23470894717613     0.5     0.5
  12    H   -1.23506433587007    0.88767428525317    1.23470902573029     0.5     0.5
NEB.Atoms.SpeciesAndCoordinates>
```

## 3. 具体例：C2H4 の二量化経路

本ディレクトリの [`src/`](../src/) に，そのまま流せる入力ファイルを置いてある．

| ファイル | 内容 |
|---|---|
| [`src/c2h4_neb.dat`](../src/c2h4_neb.dat) | エチレン2分子の NEB 計算入力（始状態＋終状態＋SCF/MD 設定一式） |
| [`src/si8_neb.dat`](../src/si8_neb.dat) | Si 8原子系の NEB 計算入力 |
| [`src/job_openmx_systemb.sh`](../src/job_openmx_systemb.sh) | 物性研 SystemB 向けのジョブスクリプト |

### 3.1 擬ポテンシャル・基底データの場所を指定する

計算環境ごとに `DFT_DATA19`（PAO / VPS のデータセット）の置き場所が異なるため，
入力ファイルの `DATA.PATH` に実際のパスを書く必要がある．

物性研 SystemB の場合は，`c2h4_neb.dat` の先頭に以下を追記する：

```
DATA.PATH /home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmx-3.9.9-1/DFT_DATA19
```

### 3.2 ジョブの投入

```bash
sbatch job_openmx_systemb.sh
```

ジョブスクリプトの各行の意味とノード数・並列数の決め方は，
[Queue system (Slurm) の利用](../../../02_external_machine/supercom/sec/systemb_slurm.md) を参照．

---

[⬅️ 各種計算ガイド](./calc_method.md) ｜ [🏠 Home](../../../../README.md)
