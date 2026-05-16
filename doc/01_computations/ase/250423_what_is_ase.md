---
title: 250423_what_is_ase.md
excerpt: <excerpt or description on this script>
author: Takeru Nakashima
collection: portfolio
date: 2025-04-28
# Copyright (c) 2025-04-28 <Takeru Nakashima>. All rights reserved.
---

[🏠 Home](ase.md)

# Atomic Simulation Environment (ASE)
[Atomic Simulation Environment (ASE)](https://wiki.fysik.dtu.dk/ase/index.html)は，Pythonで記述された原子スケールのシミュレーション用ライブラリ．

具体的には，分子，固体，界面，スラブ構造などの作成や配置の調整を，Python上で簡便かつ効率的に扱うことを可能にする．

> The Atomic Simulation Environment (ASE) is a set of tools and Python modules for setting up, manipulating, running, visualizing and analyzing atomistic simulations. The code is freely available under the GNU LGPL license.
> 
> ASE provides interfaces to different codes through Calculators which are used together with the central Atoms object and the many available algorithms in ASE.


## インストール方法
``` bash
$ pip install ase

# pipenv を利用できる場合は，以下を推奨．
$ pipenv install ase
```

## ✅ 主な機能と特徴
ASEのもつ主な機能と特徴を以下に列挙する：

- **構造モデリング**  
    原子配置，結晶構造を簡単に作成・操作可能（ex. 表面モデルを作成し，吸着原子を容易につけることが可能．）
- **連携機能**  
    さまざまな計算ソフトと連携可能（ex. VASP, Quantum ESPRESSO, GPAW, LAMMPS, OpenMX, CASTEP, CP2K, GROMACS, siesta, blah blah blah）
- **簡単な古典力場を用いた計算**  
    構造最適化，分子動力学(MD)，エネルギー計算などをスクリプトで実行可能.
- **file形式の自由度**  
    さまざまなファイルフォーマットへ読み書き可能．
- **開発のしやすさ**  
    pythonで書かれたコードであることから，python script上でseamlessに，データ解析に利用できる．

下記に計算コードの一例(H2分子の構造最適化）を示す：

``` python
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 分子を作成
h2o = molecule('H2O')

# 簡単なポテンシャル（EMT）をセット
h2o.calc = EMT()

# 最適化
opt = BFGS(h2o)
opt.run(fmax=0.05)

# エネルギーを表示
print('Final energy:', h2o.get_potential_energy())
```

ASEの利用者数は多く，web上で様々なsample codeを見つけることができる．
[Cu(111)表面への窒素原子の吸着エネルギーの計算例](https://qiita.com/cometscome_phys/items/cd1f4d5f025872dfaae5)なども共有されている．下記のsample codeでは
``` python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton
from ase.build import fcc111, add_adsorbate

h = 1.85
d = 1.10

slab = fcc111('Cu', size=(4, 4, 2), vacuum=10.0) #銅原子スラブのセット

# slab.set_calculator(EMT()) #銅原子スラブの計算にはEMTを使用
slab.calc = EMT()#銅原子スラブの計算にはEMTを使用
e_slab = slab.get_potential_energy() #スラブのポテンシャルエネルギーを計算

molecule = Atoms('2N', positions=[(0., 0., 0.), (0., 0., d)]) #窒素分子のセット。(0,0,0)が一つ目のNの位置、(0,0,d)が二つ目のNの位置。
molecule.set_calculator(EMT()) #窒素分子の計算にはEMTを使用
e_N2 = molecule.get_potential_energy() #窒素分子のポテンシャルエネルギーの計算

add_adsorbate(slab, molecule, h, 'ontop') #窒素分子を上にのせる
constraint = FixAtoms(mask=[a.symbol != 'N' for a in slab]) #拘束条件としては、計算を高速化するため、銅原子の位置を緩和させずに固
slab.set_constraint(constraint) #拘束条件をセット
dyn = QuasiNewton(slab, trajectory='N2Cu.traj') #準ニュートン法を設定
dyn.run(fmax=0.05) #構造緩和スタート。全ての原子に働く力がfmax以下になるまで。

print('Adsorption energy:', e_slab + e_N2 - slab.get_potential_energy()) #ポテンシャルエネルギーを計算し、先ほどの二つとの差を取る

```

## ASEで利用できるcalculators
ASEでは様々な古典力場を利用することが可能である．以下に実装されている古典力場を列挙する：
| 古典力場 | 特徴 | ASE内での呼び出し例 |
|---|---|---|
| EMT (Effective Medium Theory) | 金属専用、非常に軽い、粗い精度 | ase.calculators.emt.EMT |
| EAM (Embedded Atom Method) | 金属（特にFCC金属）向き、やや高精度 | ase.calculators.eam.EAM |
| Lennard-Jones (LJ) | 簡単な分子間力（練習・テスト用） | ase.calculators.lj.LennardJones |
| Tersoff | 半導体（Si, C, GaAsなど）向き | LAMMPS経由または外部モジュール必要 |
| Stillinger-Weber (SW) | Siなどの半導体向き | LAMMPS経由 |
| ReaxFF | 高精度、化学反応まで扱えるが非常に重い | LAMMPS経由、または専用プログラム（reaxff）|
| Morse | 単純な二体間ポテンシャル、金属や分子に使える | ase.calculators.morse.MorsePotential |
| Universal Force Field (UFF) | 汎用（ほぼ全元素に対応） | ase.calculators.uff.UFF（ただし標準ではない、追加モジュール要）|

[🏠 Home](ase.md)
