---
title: "Quantum ESPRESSO とは？"
excerpt: "Quantum ESPRESSO の成り立ち，名前の由来，開発体制と，実行ファイル群としての構成."
author: "Takeru Nakashima"
collection: portfolio
date: 2026-03-30
# Copyright (c) 2026 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [💡 計算技術](../../README.md) › [Quantum ESPRESSO](../quantum_espresso.md)

# 🐣 Quantum ESPRESSO とは？

<br/>
<img src="../images/quantum_espresso_logo.jpg" width="50%">
<br/>

---

## 1. 👾 概要

[Quantum ESPRESSO (QE)](http://dx.doi.org/10.1088/0953-8984/21/39/395502) は，
**密度汎関数理論（DFT）**を基礎とし，**平面波法（plane-wave method）**と
**擬ポテンシャル法（pseudopotential method）**を中核とする第一原理計算ソフトウェアパッケージである．

名前の由来は "**opEn Source Package for Research in Electronic Structure, Simulation, and Optimization**" の頭文字．
イタリアで，元々個別に存在したプロジェクトコード群——メインは
PWscf (Plane-Wave Self-Consistent Field)——を統合する形で開発された．

## 2. 🏛️ 開発体制

開発チームには以下の機関が参加しており，イタリア国立研究評議会 (CNR) と提携している．

* Scuola Internazionale Superiore di Studi Avanzati (SISSA)
* Abdus Salam International Centre for Theoretical Physics (ICTP)
* CINECA 国立スーパーコンピューティングセンター
* ローザンヌ連邦工科大学 (EPFL)
* Oden Institute for Computational Engineering and Sciences／テキサス大学オースティン校

-- [QE manifesto](https://www.quantum-espresso.org/manifesto/)

## 3. 🛠️ 構成：なぜ実行ファイルが複数あるのか

**QE は単一のプログラムではなく，実行ファイル群である．**
前述のとおり個別のコードを統合して作られた経緯から，
行いたい計算に応じて**複数の実行ファイルを順番に実行する**設計になっている．

| 実行ファイル | 役割 |
|---|---|
| `pw.x` | SCF 計算・構造最適化（PWscf のメインコード．ほぼすべての計算の起点） |
| `ph.x` | フォノン計算（密度汎関数摂動論） |
| `dos.x` / `projwfc.x` | 状態密度・射影状態密度の算出 |
| `bands.x` | バンド構造の整形 |
| `pp.x` | 電子密度などの後処理・可視化用ファイルの出力 |

したがって「まず `pw.x` で SCF を収束させ，その出力を次のコードに渡す」というのが基本の流れになる．

---

[⬅️ Quantum ESPRESSO](../quantum_espresso.md) ｜ [🏠 Home](../../../../README.md)
