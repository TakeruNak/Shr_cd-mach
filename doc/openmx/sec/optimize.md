---
title: optimize.md
excerpt: <excerpt or description on this script>
author: Takeru Nakashima
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025-06-10 <Takeru Nakashima>. All rights reserved.
---

[🏠 Home](calc_method.md)

# 構造最適化

[構造最適化](https://www.openmx-square.org/openmx_man3.9jp/node47.html)に関する詳細は，OpenMXのwebsiteを参照．
MD.Typeは，構造最適化の手法はまずはRFで実行するのが良い．収束が悪い場合は，`MD.Opt.DIIS.History` を増やしてみると良い．

``` openmx.dat
# ---------------------------------------------
# INPUT EXAMPLE| OpenMX params. for Optimizaion
# ---------------------------------------------

# ------------------------------------
# Geometry Optimization and Molecular dynamics
# ------------------------------------
MD.Type                      RF     # Opt|DIIS|BFGS|RF|EF
MD.Opt.DIIS.History          3      # default=3
MD.Opt.StartDIIS             5      # default=5
MD.Opt.EveryDIIS            200     # default=200
MD.maxIter                  100     # default=1
MD.Opt.criterion            1.0e-4  # default=0.0003 (Hartree/Bohr)

# ----------------------------------
# Deepest layer is fiexed in the optimization
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

[🏠 Home](calc_method.md)
