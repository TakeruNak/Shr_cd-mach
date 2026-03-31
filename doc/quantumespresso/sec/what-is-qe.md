---
title: what-is-qe.md
excerpt: <excerpt or description on this script>
author: Takeru Nakashima
collection: portfolio
date: 2026-03-30
# Copyright (c) 2026-03-30 <Takeru Nakashima>. All rights reserved.
---

# 🐣 What is Quantum ESPRESSO?

## 👾　Quantum ESPRESSOの概要
[Quantum ESPROSSO (QE)](http://dx.doi.org/10.1088/0953-8984/21/39/395502)は，Density Functional Theory (DFT, 密度汎関数理論）を基礎とし，Plane-wave method (平面波法）とPseudopotential method (擬ポテンシャル法）を中核とした，第一原理計算を行うためのソフトウェアパッケージ．

イタリアで，元々個別に存在したプロジェクトコード群–PWscf(Plane-Wave Self-Consistent Field)がメイン–を統合して開発されたソフトウェアで，名前の由来は「opEn Source Package for Research in Electronic Structure, Simulation, and Optimization」の頭文字から来ている．　

開発チームは，Scuola Internazionale Superiore di Studi Avanzati (SISSA)，Abdus Salam International Centre for Theoretical Physics (ICTP)，CINECA国立スーパーコンピューティングセンター，ローザンヌ連邦工科大学，Oden Institute for Computational Engineering and Sciences，テキサス大学オースティン校などが含まれ，イタリア国立研究評議会 (CNR) と提携している.

-- [QE-web](https://www.quantum-espresso.org/manifesto/)

## 👾　Quantum ESPRESSOの特徴

Quantum ESPRESSOは，元々個別に存在したコードを統合して開発されたプログラム群であるため，複数の実行ファイルを個別>に実行して，行いたい物性シミュレーションを実行する必要性がある．中核となる実行ファイルは，pw.x (PWscfプロジェクト
のメインコード)である．この点から，複数の実行ファイルに対して，複数のインプットファイルを用意する必要性があり，初心者にとっては，やや敷居が高いと感じるかもしれない．
