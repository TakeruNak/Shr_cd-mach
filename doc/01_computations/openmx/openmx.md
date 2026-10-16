---
title: "OpenMX 利用ガイド"
excerpt: "第一原理計算プログラムの一種である OpenMX を用いた計算演習を通して，第一原理計算の肌感覚を掴む."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-04-08
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../README.md) › [💡 計算技術](../README.md)

# OpenMX 利用ガイド

OpenMX は，擬原子軌道を局在基底に用いる第一原理計算コードである．
平面波基底のコードに比べて計算コストが小さく，**手元の Mac でも第一原理計算の感覚を掴める**のが利点である．

本ガイドは，次の4ステップで「動かせるようになる」ことを目的とする．

| # | ページ | 得られるもの |
|---|---|---|
| 1 | [OpenMX とは？](./sec/what_is_openmx.md) | 手法の位置づけと，できること・できないこと |
| 2 | [インストール方法](./sec/install_openmx.md) | macOS 上にビルドして `H2O` を1本流すところまで |
| 3 | [パラメタ設定の勘所・収束のスキル](./sec/param_info.md) | 入力パラメタの意味と，収束しないときの打ち手 |
| 4 | [各種計算ガイド](./sec/calc_method.md) | 構造最適化・NEB の具体的な入力例 |

> 💬 大きな系を回す段階になったら，[物性研 SystemB の利用方法](../../02_external_machine/supercom/systemb.md) へ進む．

## 📁 このディレクトリの構成

```
openmx/
├── openmx.md    … 本ページ
├── sec/         … 各解説ページ
├── images/      … 図
└── src/         … サンプル入力ファイル（c2h4_neb.dat, si8_neb.dat）
```

---

[⬅️ 計算技術](../README.md) ｜ [🏠 Home](../../../README.md)
