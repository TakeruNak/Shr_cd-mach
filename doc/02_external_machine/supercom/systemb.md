---
title: "物性研 SystemB の利用方法"
excerpt: "東京大学物性研究所 SystemB (ohtaka) へのログインと，Slurm によるジョブ投入の手順."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../README.md) › [🖧 外部計算機](../README.md)

# 物性研 SystemB (ohtaka)

SystemB は東京大学物性研究所の共用計算機システムの1つで，物性物理・材料科学の計算に広く使われている．
**1ノードあたり 128 CPU コア**を持ち，ジョブの実行順序は Slurm Workload Manager が管理する．

| # | ページ | 得られるもの |
|---|---|---|
| 1 | [SystemB へのログイン方法](./sec/systemb_login.md) | SSH 公開鍵の登録と，ssh コマンドでの接続 |
| 2 | [Queue system (Slurm) の利用](./sec/systemb_slurm.md) | ジョブスクリプトの書き方と，並列数の決め方 |

## 📖 公式マニュアル

本ページは要点の抜粋である．正確な情報と最新の仕様は公式資料を参照すること．

* [SystemB システム概要](https://mdcl.issp.u-tokyo.ac.jp/scc/system/systembinfo)
* [マニュアル一覧](https://mdcl.issp.u-tokyo.ac.jp/scc/system/systembinfo/manual)
* [利用の手引き (PDF)](https://mdcl.issp.u-tokyo.ac.jp/scc/manual-B/SystemB_User%27s_Guide_Rev2.7_JP.pdf) — 頻用コマンドが一通りまとまっている
* [利用講習会スライド (PDF)](https://mdcl.issp.u-tokyo.ac.jp/scc/manual-B/ISSP20201127_B_Dell.pdf) — 初学者はこちらが読みやすい

---

[⬅️ 外部計算機](../README.md) ｜ [🏠 Home](../../../README.md)
