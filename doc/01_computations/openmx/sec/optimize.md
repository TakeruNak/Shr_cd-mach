---
title: "構造最適化（OpenMX）"
excerpt: "OpenMX で構造最適化を行う際の MD.Type の選び方と，入力ファイルの記述例."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [💡 計算技術](../../README.md) › [OpenMX](../openmx.md) › [各種計算ガイド](./calc_method.md)

# 構造最適化

公式マニュアルの[構造最適化](https://www.openmx-square.org/openmx_man3.9jp/node47.html)の節も併せて参照．

## 設定の勘所

* **`MD.Type` はまず `RF` で試す．** 多くの系でこれが素直に収束する．
* **収束が悪い場合は `MD.Opt.DIIS.History` を増やす．** 過去の履歴を多く参照させることで振動を抑えられる．
* それでも原子位置が振動する場合は，`scf.energycutoff` を上げて実空間メッシュを細かくする
  （[パラメタ設定の勘所 §2.4](./param_info.md) を参照）．
* 基板など動かしたくない原子は `MD.Fixed.XYZ` ブロックで固定する．

## 入力例

```
# ---------------------------------------------
# INPUT EXAMPLE| OpenMX params. for optimization
# ---------------------------------------------

# ------------------------------------
# Geometry optimization and molecular dynamics
# ------------------------------------
MD.Type                      RF     # Opt|DIIS|BFGS|RF|EF
MD.Opt.DIIS.History          3      # default=3
MD.Opt.StartDIIS             5      # default=5
MD.Opt.EveryDIIS            200     # default=200
MD.maxIter                  100     # default=1
MD.Opt.criterion            1.0e-4  # default=0.0003 (Hartree/Bohr)

# ----------------------------------
# The deepest layer is fixed in the optimization
#   列の意味: 原子番号 / x / y / z     （1 = 固定, 0 = 可動）
# ----------------------------------
<MD.Fixed.XYZ
1 1 1 1
2 0 0 0
3 0 0 0
4 0 0 0
5 0 0 0
6 0 0 0
7 0 0 0
MD.Fixed.XYZ>
```

---

[⬅️ 各種計算ガイド](./calc_method.md) ｜ [🏠 Home](../../../../README.md)
