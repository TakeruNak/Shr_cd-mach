---
title: "Quantum ESPRESSO 利用ガイド"
excerpt: "平面波基底の第一原理計算パッケージ Quantum ESPRESSO の導入から実行まで."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-24
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../README.md) › [💡 計算技術](../README.md)

# Quantum ESPRESSO 利用ガイド

Quantum ESPRESSO（QE）は，**平面波基底 + 擬ポテンシャル**に基づく第一原理計算パッケージである．
世界的に最も広く使われている DFT コードの1つで，周辺ツールと解説記事が豊富なのが強み．

| # | ページ | 得られるもの |
|---|---|---|
| 1 | [Quantum ESPRESSO とは？](./sec/what_is_qe.md) | パッケージの成り立ちと構成（なぜ実行ファイルが複数あるのか） |
| 2 | [インストールガイド](./sec/install_qe.md) | macOS 上でのビルドと，実際に踏んだビルドエラーの回避策 |
| 3 | [計算を実行してみよう](./sec/how_to_run_qe.md) | 入力ファイルの書き方と実行の流れ（執筆予定） |

> 💬 局在基底の [OpenMX](../openmx/openmx.md) と比べると，QE は計算コストが大きい一方で，
> 平面波基底ゆえに基底の収束を `ecutwfc` 1つで制御でき，精度の見積もりが素直である．

## 📁 このディレクトリの構成

```
quantum_espresso/
├── quantum_espresso.md  … 本ページ
├── sec/                 … 各解説ページ
└── images/              … 図
```

---

[⬅️ 計算技術](../README.md) ｜ [🏠 Home](../../../README.md)
