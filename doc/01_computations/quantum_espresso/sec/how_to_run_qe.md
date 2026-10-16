---
title: "Quantum ESPRESSO で計算を実行してみよう"
excerpt: "Quantum ESPRESSO を利用して材料の第一原理計算を行う手順."
author: "Takeru Nakashima"
collection: portfolio
date: 2026-03-30
# Copyright (c) 2026 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [💡 計算技術](../../README.md) › [Quantum ESPRESSO](../quantum_espresso.md)

# Quantum ESPRESSO で計算を実行してみよう

## 1. 計算の全体構成

QE は実行ファイル群であり，**`pw.x` による SCF 計算を起点**として，
後段の解析コードへ出力を引き渡していく．各実行ファイルの役割は
[Quantum ESPRESSO とは？ §3](./what_is_qe.md) を参照．

```
入力ファイル (*.in)  ──> pw.x ──> 波動関数・電荷密度 (*.save/) ──> dos.x / bands.x / ph.x / pp.x
                                        └──> 標準出力 (*.out)  … 全エネルギー・力・応力
```

## 2. 最小限の実行例

インストール直後の動作確認手順（Si の SCF 計算）は
[インストールガイド §動作確認](./install_qe.md#-動作確認) にまとめてある．

```bash
mpirun -np 4 <PREFIX>/bin/pw.x -in si.scf.in > si.scf.out
```

## 3. 入力ファイルの書き方

> 📝 **（執筆予定）** `&CONTROL` / `&SYSTEM` / `&ELECTRONS` 各ネームリストと
> `ATOMIC_SPECIES` / `ATOMIC_POSITIONS` / `K_POINTS` カードの書き方をまとめる予定．

それまでは以下を参照．

* ソース同梱の例：`PW/examples/` 以下に，計算の種類ごとの入力例が揃っている．
* [SATL QE tutorial（東北大・是常研）](http://www.cmpt.phys.tohoku.ac.jp/~koretsune/SATL_qe_tutorial/)
* [公式ドキュメント](https://www.quantum-espresso.org/documentation/)

---

[⬅️ Quantum ESPRESSO](../quantum_espresso.md) ｜ [🏠 Home](../../../../README.md)
