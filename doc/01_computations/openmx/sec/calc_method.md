---
title: "各種計算ガイド"
excerpt: "OpenMX で実際に行う計算（構造最適化・NEB）ごとの入力例と勘所."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [💡 計算技術](../../README.md) › [OpenMX](../openmx.md)

# 各種計算ガイド

やりたい計算ごとに，入力ファイルの該当ブロックと設定の勘所をまとめる．
いずれも SCF 部分の設定は共通で，[パラメタ設定の勘所](./param_info.md) を前提とする．

| 計算 | 目的 | ページ |
|---|---|---|
| 構造最適化 | 安定構造（ポテンシャル面の極小点）を求める | [構造最適化](./optimize.md) |
| NEB 法 | 2つの安定構造をつなぐ反応経路と活性化障壁を求める | [Nudged Elastic Band (NEB) method](./neb.md) |

> 💬 どちらも原子座標を動かす計算なので，制御パラメタの接頭辞は `MD.###` である．

---

[⬅️ OpenMX](../openmx.md) ｜ [🏠 Home](../../../../README.md)
