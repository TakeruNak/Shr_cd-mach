---
title: "Python 環境構築ガイド"
excerpt: "macOS / Linux での開発環境構築に必要なツールの導入手順と，その役割分担."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-05
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../README.md) › [🛠️ IT・開発環境](../README.md)

# Python 環境構築ガイド

macOS や Linux での開発環境構築に必要なツールの導入手順をまとめる．

## 全体像：4つのツールの役割分担

ツールが4つ出てくるが，それぞれ担当する層が違う．この関係を掴んでおくと迷わない．

```
Terminal   … 操作する窓口
  └ Homebrew  … マシン全体のソフトウェアを管理（brew install ...）
      └ pyenv     … Python 本体のバージョンを管理（3.11 / 3.13 ...）
          └ pipenv    … プロジェクトごとのパッケージを管理（numpy, ase ...）
```

| ソフトウェア | 役割 |
|---|---|
| Terminal | コマンドライン（CUI）でマシンを操作するためのソフトウェア |
| Homebrew | パッケージ管理ソフト．アプリケーションのインストールとバージョン管理を一括で担う |
| pyenv | Python 本体のバージョンを切り替えるためのソフトウェア |
| pipenv | プロジェクトごとに，インストールするパッケージを管理する仮想環境を構築するソフトウェア |

## 導入手順

**上から順に実施すること**（下のツールは上のツールに依存している）．

| # | ページ | 内容 |
|---|---|---|
| 1 | [🖥️ Terminal の開き方](./sec/terminal.md) | ターミナルを起動する |
| 2 | [🍺 Homebrew のインストール](./sec/homebrew.md) | パッケージマネージャを入れる |
| 3 | [🐍 pyenv のインストール](./sec/pyenv.md) | Python のバージョンを管理する |
| 4 | [🐍 pyenv & pipenv を利用した仮想環境](./sec/pyenv_pipenv.md) | プロジェクトの依存関係を管理する |

## 📁 このディレクトリの構成

```
env4mac/
├── environment.md  … 本ページ
├── sec/            … 各解説ページ
├── images/         … 図
└── src/            … 動作確認用のサンプルスクリプト（test.py）
```

---

[⬅️ IT・開発環境](../README.md) ｜ [🏠 Home](../../../README.md)
