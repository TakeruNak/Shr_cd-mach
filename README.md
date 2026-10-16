---
title: "cd-mach group ドキュメント"
excerpt: "計算物性研究を進めるうえで必要な計算技術・計算機利用法・研究ノウハウをまとめた共有テキスト集."
author: "Takeru Nakashima"
collection: portfolio
date: 2026-10-16
# Copyright (c) 2025-2026 Takeru Nakashima. All rights reserved.
---

# cd-mach group ドキュメント

本リポジトリは，cd-mach group で共有する**実務テキスト集**である．
研究を始めた段階で必ず必要になる「計算ソフトの使い方」「外部計算機の使い方」「研究の進め方」を，
その場で引ける形でまとめることを目的とする．

---

## 📚 目次

| # | セクション | 内容 |
|---|---|---|
| 01 | [💡 計算技術](./doc/01_computations/README.md) | DFT 計算コード（OpenMX / Quantum ESPRESSO）と周辺ツールの導入・実行 |
| 02 | [🖧 外部計算機](./doc/02_external_machine/README.md) | スパコン（物性研 SystemB ほか）へのログインとジョブ投入 |
| 03 | [🔬 研究ノウハウ](./doc/03_research_hub/README.md) | 論文の読み方・書き方，研究デザイン，情報伝達 |
| 04 | [🛠️ IT・開発環境](./doc/04_IT/README.md) | macOS の環境構築，Python 仮想環境，GitHub |
| 05 | [📖 基礎理論・参考文献](./doc/05_foundations/README.md) | 固体物理・群論などの推薦図書リスト |

---

## 🚀 はじめての人向けの推奨ルート

1. **環境を整える** → [🖥️ Terminal の起動](./doc/04_IT/env4mac/sec/terminal.md) → [🍺 Homebrew](./doc/04_IT/env4mac/sec/homebrew.md) → [🐍 Python 仮想環境](./doc/04_IT/env4mac/environment.md)
2. **手元で計算を動かす** → [OpenMX](./doc/01_computations/openmx/openmx.md) または [Quantum ESPRESSO](./doc/01_computations/quantum_espresso/quantum_espresso.md)
3. **構造を見る／作る** → [VESTA](./doc/01_computations/vesta/vesta.md) → [ASE](./doc/01_computations/ase/ase.md)
4. **大きな系を外部計算機へ** → [物性研 SystemB](./doc/02_external_machine/supercom/systemb.md)
5. **並行して研究の型を学ぶ** → [論文の読み方](./doc/03_research_hub/research/how_to_read_paper.md)

---

## 🗂️ ディレクトリ構成のルール

ページが増えても迷子にならないよう，各セクションは次の3層で構成する．

```
doc/<NN_section>/
├── README.md          … セクションの目次
└── <topic>/
    ├── <topic>.md     … トピックの入口（概要とサブページへのリンク）
    ├── sec/           … 個別の解説ページ
    ├── images/        … 図・スクリーンショット
    └── src/           … サンプルの入力ファイル・スクリプト
```

* ファイル名・ディレクトリ名は **半角英小文字 + スネークケース**（日本語名はリンク切れの原因になるため使わない）．
* 各ページ先頭にはパンくずリンク，末尾には親ページへの戻りリンクを置く．
* 各ページ先頭の YAML front matter には `title` / `excerpt` / `author` / `date` を記載する．

## ✍️ 加筆の仕方

誤りの指摘・加筆は Pull Request で歓迎する．
未執筆のページには **（執筆予定）** と明記してあるので，書ける人から埋めていってほしい．
