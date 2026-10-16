---
title: "計算技術"
excerpt: "第一原理計算コードと周辺ツールの導入・実行方法をまとめたセクション."
author: "Takeru Nakashima"
collection: portfolio
date: 2026-10-16
# Copyright (c) 2026 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../README.md)

# 💡 計算技術

材料計算を実際に回すために必要な知識を，**①理論の土台 → ②計算コード → ③周辺ツール → ④困ったとき**の順にまとめる．

---

## 1. 理論と計算機の土台

まず「何を計算しているのか」と「どう並列に回すのか」を押さえる．

| ページ | 内容 |
|---|---|
| [Density Functional Theory — materials](https://github.com/TakeruNak/DFT_seminar_materials.git) | DFT セミナーの講義資料（別リポジトリ） |
| [並列計算の利用方法](./parallel_computing/parallel_computing_guide.md) | MPI / OpenMP の考え方と使い分け |

## 2. 第一原理計算コード

本グループで常用する DFT コードは以下の2つ．局在基底の OpenMX と平面波基底の Quantum ESPRESSO で，
得意な系と計算コストの性格が異なる．

| コード | 基底 | ページ |
|---|---|---|
| OpenMX | 擬原子軌道（局在基底） | [OpenMX 利用ガイド](./openmx/openmx.md) |
| Quantum ESPRESSO | 平面波 | [Quantum ESPRESSO 利用ガイド](./quantum_espresso/quantum_espresso.md) |

## 3. 周辺ツール

構造を作る・見る，そして探索を自動化するためのツール群．

| ツール | 用途 | ページ |
|---|---|---|
| VESTA | 結晶・分子構造の可視化とファイル変換 | [VESTA 利用ガイド](./vesta/vesta.md) |
| ASE | Python からの構造生成・操作・可視化 | [ASE 利用ガイド](./ase/ase.md) |
| PhysBO | ベイズ最適化による材料探索 | [PhysBO 利用ガイド](./physbo/physbo_guide.md) |

## 4. 困ったとき

| ページ | 内容 |
|---|---|
| [計算のデバッグと開発の作法](./troubleshooting.md) | 未知の出力変数の調べ方，ジョブの監視，テスト駆動開発 |

---

[🏠 Home](../../README.md)
