---
title: "OpenMX とは？"
excerpt: "OpenMX の手法上の位置づけ（量子化学計算との対比）と，主な機能・制約を整理する."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-09
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [💡 計算技術](../../README.md) › [OpenMX](../openmx.md)

# OpenMX とは？

<br/>
<img src="../images/openmx_logo.png" width="20%">
<br/>

---

## 1. 前提：材料計算の2つの流儀

材料計算のシミュレーション手法は，大きく**量子化学計算**と**第一原理計算**の2つに分けられる．
両者は計算精度と計算コストのバランスにおいて対照的な性格を持つ．
慣例としては，量子化学計算は分子系に，第一原理計算は結晶系に適用されることが多い．

| 手法 | 基礎 | 長所 | 短所 |
|---|---|---|---|
| 量子化学計算 | 波動関数 | 電子状態を直接扱う高精度手法が多い | 計算コストが大きくなりがち |
| 第一原理計算 | 密度汎関数理論（DFT） | 擬ポテンシャルの活用により高効率な手法が多い | 計算精度が交換相関汎関数に依存する |

> 💬 現代ではこの2つの境界は曖昧になっており，手法・適用範囲が重なる場合も少なくない．

## 2. OpenMX の位置づけ

[OpenMX](https://www.openmx-square.org/openmx_man3.9jp/) は，日本で開発された第一原理計算ソフトウェアであり，
東京大学物性研究所の尾崎泰助教授らを中心に研究・開発が進められてきた．

本ソフトの最大の特徴は，孤立原子系の擬ポテンシャル法に基づき
**有効擬原子軌道（PAO: Pseudo-Atomic Orbital）を局在基底として用いる**点にある．
これにより Kohn-Sham 方程式を自己無撞着に解く際の計算コストを大幅に低減でき，
平面波基底法を用いる VASP や Quantum ESPRESSO に比べて計算コストが非常に小さい．

## 3. ✅ 主な機能

| 分類 | 機能 |
|---|---|
| 交換相関エネルギー | 局所密度近似（LDA, LSDA）／一般化勾配近似（GGA） |
| 擬ポテンシャル | Vanderbilt 型のノルム保存擬ポテンシャル |
| 強相関系 | DFT+U 計算 |
| 電気化学・表面 | [Effective Screening Medium (ESM) method](https://sugino.issp.u-tokyo.ac.jp/esm/) |
| 分子動力学 | NVE アンサンブル，NVT アンサンブル（速度スケーリング法・Nosé-Hoover 法） |
| バンド解析 | スーパーセルのバンド構造を任意の k 空間バンドへ変換する band unfolding method |
| 分光 | core-hole を考慮した擬ポテンシャルによる XPS 計算 |
| 後処理連携 | Wannier90, BoltzTraP などの post-processing コードとの連携 |

v3.9 では Berry 位相を用いた巨視的分極率の計算も可能である．

## 4. ⚠️ 注意点

> 💬 これはすべての第一原理計算ソフトウェアに共通することだが，擬ポテンシャルの導入や種々の近似，
> 数値的誤差が含まれるため，**計算結果が必ずしも実験結果を正確に再現するとは限らない**．
> 得られた数値を鵜呑みにせず，収束性の確認と実験・文献値との突き合わせを必ず行うこと．

## 5. 📖 マニュアル

[日本語版](https://www.openmx-square.org/openmx_man3.9jp/)・[英語版](https://openmx-square.org/openmx_man3.9/index.html)
ともに非常に充実しており，分からないことはまずマニュアルを引くのが近道である．

---

[⬅️ OpenMX](../openmx.md) ｜ [🏠 Home](../../../../README.md)
