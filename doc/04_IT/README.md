---
title: "IT・開発環境"
excerpt: "macOS での開発環境構築，Python 仮想環境，GitHub の使い方をまとめたセクション."
author: "Takeru Nakashima"
collection: portfolio
date: 2026-10-16
# Copyright (c) 2026 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../README.md)

# 🛠️ IT・開発環境

計算を始める前に整えておく土台．**このセクションは一番最初にやる作業**である．

```
① ターミナルを開く ──> ② Homebrew を入れる ──> ③ Python 環境を作る ──> ④ Git / GitHub を使う
```

---

## 1. 開発環境の構築（macOS / Linux）

| ページ | 内容 |
|---|---|
| [Python 環境構築ガイド](./env4mac/environment.md) | ターミナル・Homebrew・pyenv・pipenv の導入（入口ページ） |

個別のページへ直接飛ぶ場合は以下．

| # | ページ | 内容 |
|---|---|---|
| 1 | [🖥️ Terminal の起動](./env4mac/sec/terminal.md) | ターミナルの開き方 |
| 2 | [🍺 Homebrew のインストール](./env4mac/sec/homebrew.md) | パッケージマネージャの導入とよく使うコマンド |
| 3 | [🐍 pyenv のインストール](./env4mac/sec/pyenv.md) | Python バージョンの管理 |
| 4 | [🐍 pyenv & pipenv を利用した仮想環境](./env4mac/sec/pyenv_pipenv.md) | プロジェクトごとの依存パッケージ管理 |

> 💬 Homebrew は [OpenMX](../01_computations/openmx/sec/install_openmx.md) や
> [Quantum ESPRESSO](../01_computations/quantum_espresso/sec/install_qe.md) のビルドにも必要になるため，
> 最初に入れておくこと．

## 2. バージョン管理

| ページ | 内容 |
|---|---|
| [GitHub とは何だろな？](./github/github.md) | Git / GitHub の役割と導入 |

---

[🏠 Home](../../README.md)
