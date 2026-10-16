---
title: "外部計算機"
excerpt: "スーパーコンピュータへのログイン方法とジョブ投入手順をまとめたセクション."
author: "Takeru Nakashima"
collection: portfolio
date: 2026-10-16
# Copyright (c) 2026 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../README.md)

# 🖧 外部計算機

手元の Mac で回せる規模を超えたら，外部の大規模計算機（スパコン）を使う．
どの計算機でも，使い始めるまでの流れは共通である．

```
① 利用者登録 ──> ② SSH 公開鍵の登録 ──> ③ ssh でログイン ──> ④ ジョブスケジューラへ投入
```

---

## 利用できる計算機

| 計算機 | 運用機関 | スケジューラ | ページ |
|---|---|---|---|
| SystemB (ohtaka) | 東京大学 物性研究所 | Slurm | [利用方法](./supercom/systemb.md) |
| Genkai | 九州大学 情報基盤研究開発センター | — | [利用方法](./supercom/genkai.md)（執筆予定） |
| TSUBAME 4.0 | Institute of Science Tokyo | — | [利用方法](./supercom/tsubame.md)（執筆予定） |

## 共通の前提

* **SSH 公開鍵認証**が必要．鍵の作り方と登録手順は
  [SystemB へのログイン方法](./supercom/sec/systemb_login.md) にまとめてあり，他の計算機でもほぼ同じである．
* **秘密鍵は絶対に登録・送信しない．** 登録するのは必ず公開鍵（`.pub`）側．
* 並列数の決め方の考え方は [並列計算ガイド](../01_computations/parallel_computing/parallel_computing_guide.md) を参照．

---

[🏠 Home](../../README.md)
