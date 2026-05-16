---
title: how-to-run-qe.md
excerpt: Quantum ESPRESSO (QE) を利用して，材料の第一原理計算を行う方法を簡単に説明する．
author: Takeru Nakashima
collection: portfolio
date: 2026-03-30
# Copyright (c) 2026-03-30 <Takeru Nakashima>. All rights reserved.
---

# How to use QE
以下に，Quantum ESPRESSO (QE) を利用して，材料の第一原理計算を行う方法を簡単に説明する．

## 1. QEの計算構成．
Quantum ESPRESSOは，元々個別に存在したコードを統合して開発されたプログラム群であるため，複数の実行ファイルを個別に実行して，行いたい物性シミュレーションを実行する必要性がある．中核となる実行ファイルは，pw.x (PWscfプロジェクトのメインコード)である．
