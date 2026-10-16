---
title: "PhysBO 利用ガイド"
excerpt: "ベイズ最適化により材料探索を効率化する Python ライブラリ PHYSBO の利用ガイド."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-26
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../README.md) › [💡 計算技術](../README.md)

# PhysBO 利用ガイド

**PHYSBO (PHYSics-inspired Bayesian Optimization)** は，ベイズ最適化を用いて
材料設計・探索などにおける**高コストなシミュレーション・実験の試行回数を減らす**ための Python ライブラリである．
物性・材料科学分野での応用を念頭に開発されている．

## 位置づけ

第一原理計算は1点あたりのコストが高いため，組成や構造のパラメタ空間を総当たりで走査することは現実的でない．
PhysBO は「次にどの点を計算すべきか」を代理モデル（ガウス過程）から提案することで，
**少ない計算回数で目的の物性値を持つ候補に到達する**ことを狙う．

## 📝 本ページは執筆予定

以下の項目を順にまとめる予定．

1. インストールと動作確認
2. ベイズ最適化の最小構成（探索空間の定義・獲得関数・初期サンプル）
3. 第一原理計算（[OpenMX](../openmx/openmx.md) / [Quantum ESPRESSO](../quantum_espresso/quantum_espresso.md)）との連携
4. 実際の探索例

それまでは[公式ドキュメント](https://issp-center-dev.github.io/PHYSBO/manual/master/ja/index.html)を参照．

---

[⬅️ 計算技術](../README.md) ｜ [🏠 Home](../../../README.md)
