---
title: "ASE 利用ガイド"
excerpt: "原子スケールのシミュレーションを Python から扱うライブラリ ASE の導入と基本的な使い方."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-06
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../README.md) › [💡 計算技術](../README.md)

# ASE 利用ガイド

ASE（Atomic Simulation Environment）は，**原子スケールのシミュレーションを Python から統一的に扱う**ためのライブラリである．
構造の生成・操作から各種計算コードの入出力，可視化，データ解析までを1つのスクリプトの中で完結させられるため，
「構造を作る」「結果をまとめる」といった前後の作業コストが大きく下がる．

| # | ページ | 得られるもの |
|---|---|---|
| 1 | [ASE とは何ですか？](./sec/what_is_ase.md) | 導入方法，主な機能，利用できる calculator の一覧 |
| 2 | [ASE を利用したモデル構造の可視化](./sec/visualization.md) | Jupyter 上での構造表示と，画像ファイルへの書き出し |

## 📁 このディレクトリの構成

```
ase/
├── ase.md     … 本ページ
├── sec/       … 各解説ページ
└── images/    … 図
```

---

[⬅️ 計算技術](../README.md) ｜ [🏠 Home](../../../README.md)
