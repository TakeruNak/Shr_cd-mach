---
title: "ASE とは何ですか？"
excerpt: "Atomic Simulation Environment (ASE) の概要・インストール方法・主な機能と，利用できる古典力場の一覧."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-04-28
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [💡 計算技術](../../README.md) › [ASE](../ase.md)

# Atomic Simulation Environment (ASE)

[ASE](https://wiki.fysik.dtu.dk/ase/index.html) は，Python で記述された原子スケールのシミュレーション用ライブラリ．
分子・固体・界面・スラブ構造などの作成や配置の調整を，Python 上で簡便かつ効率的に扱うことを可能にする．

> The Atomic Simulation Environment (ASE) is a set of tools and Python modules for setting up, manipulating,
> running, visualizing and analyzing atomistic simulations. The code is freely available under the GNU LGPL license.
>
> ASE provides interfaces to different codes through Calculators which are used together with the central
> Atoms object and the many available algorithms in ASE.

---

## 1. インストール方法

```bash
pip install ase

# pipenv を利用できる場合は，以下を推奨
pipenv install ase
```

Python 仮想環境の準備については [🐍 pyenv & pipenv を利用した仮想環境](../../../04_IT/env4mac/sec/pyenv_pipenv.md) を参照．

## 2. ✅ 主な機能と特徴

| 機能 | 内容 |
|---|---|
| **構造モデリング** | 原子配置・結晶構造を簡単に作成・操作できる（例：表面モデルを作り，吸着原子を容易に載せる） |
| **計算コードとの連携** | VASP, Quantum ESPRESSO, GPAW, LAMMPS, OpenMX, CASTEP, CP2K, GROMACS, SIESTA など多数に対応 |
| **古典力場による計算** | 構造最適化，分子動力学 (MD)，エネルギー計算をスクリプトで実行できる |
| **ファイル形式の自由度** | 多様なフォーマットの読み書きに対応し，形式変換に使える |
| **開発のしやすさ** | Python 製のため，データ解析までを1つのスクリプト内でシームレスに行える |

## 3. 最小の計算例：H2O の構造最適化

```python
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 1. 分子を作成
h2o = molecule('H2O')

# 2. 簡単なポテンシャル（EMT）をセット
h2o.calc = EMT()

# 3. 構造最適化
opt = BFGS(h2o)
opt.run(fmax=0.05)

# 4. エネルギーを表示
print('Final energy:', h2o.get_potential_energy())
```

## 4. 応用例：Cu(111) 表面への N2 吸着エネルギー

ASE は利用者が多く，Web 上に多数のサンプルコードがある．
以下は [Cu(111) 表面への窒素分子の吸着エネルギーの計算例](https://qiita.com/cometscome_phys/items/cd1f4d5f025872dfaae5)．

```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton
from ase.build import fcc111, add_adsorbate

h = 1.85   # 吸着高さ [Ang]
d = 1.10   # N-N 結合長 [Ang]

# 1. 銅スラブを作成し，単体のエネルギーを求める
slab = fcc111('Cu', size=(4, 4, 2), vacuum=10.0)
slab.calc = EMT()
e_slab = slab.get_potential_energy()

# 2. 窒素分子を作成し，単体のエネルギーを求める
molecule = Atoms('2N', positions=[(0., 0., 0.), (0., 0., d)])
molecule.calc = EMT()
e_N2 = molecule.get_potential_energy()

# 3. スラブ上に窒素分子を載せる
add_adsorbate(slab, molecule, h, 'ontop')

# 4. 計算を軽くするため，銅原子は固定して窒素のみ緩和させる
slab.set_constraint(FixAtoms(mask=[a.symbol != 'N' for a in slab]))

# 5. 準ニュートン法で構造緩和（全原子にかかる力が fmax 以下になるまで）
dyn = QuasiNewton(slab, trajectory='N2Cu.traj')
dyn.run(fmax=0.05)

# 6. 吸着エネルギー = (スラブ単体 + 分子単体) - 吸着系
print('Adsorption energy:', e_slab + e_N2 - slab.get_potential_energy())
```

> 💬 古い記事では `slab.set_calculator(EMT())` という書き方が使われているが，
> 現在は非推奨であり `slab.calc = EMT()` を使う．

## 5. ASE で利用できる calculator（古典力場）

ASE 自体には古典力場がいくつか同梱されており，DFT を回す前の構造の下ごしらえに使える．

| 古典力場 | 特徴 | ASE 内での呼び出し |
|---|---|---|
| EMT (Effective Medium Theory) | 金属専用．非常に軽いが精度は粗い | `ase.calculators.emt.EMT` |
| EAM (Embedded Atom Method) | 金属（特に FCC 金属）向き．やや高精度 | `ase.calculators.eam.EAM` |
| Lennard-Jones (LJ) | 単純な分子間力（練習・テスト用） | `ase.calculators.lj.LennardJones` |
| Morse | 単純な二体間ポテンシャル．金属や分子に使える | `ase.calculators.morse.MorsePotential` |
| Tersoff | 半導体（Si, C, GaAs など）向き | LAMMPS 経由または外部モジュールが必要 |
| Stillinger-Weber (SW) | Si などの半導体向き | LAMMPS 経由 |
| ReaxFF | 高精度．化学反応まで扱えるが非常に重い | LAMMPS 経由または専用プログラム |
| Universal Force Field (UFF) | 汎用（ほぼ全元素に対応） | 標準ではなく追加モジュールが必要 |

> 💬 より高精度な結果が必要な場合は，calculator を DFT コード
> （[OpenMX](../../openmx/openmx.md) / [Quantum ESPRESSO](../../quantum_espresso/quantum_espresso.md)）
> に差し替えればよい．スクリプトの残りの部分はそのまま使える点が ASE の強みである．

---

[⬅️ ASE](../ase.md) ｜ [🏠 Home](../../../../README.md)
