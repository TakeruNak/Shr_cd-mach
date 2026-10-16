---
title: "GitHub とは何だろな？"
excerpt: "Git / GitHub の役割と，研究で使い始めるための最初の手順."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-12
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../README.md) › [🛠️ IT・開発環境](../README.md)

# GitHub とは何だろな？

GitHub は，ソフトウェア開発のためのプラットフォームで，コードのバージョン管理や共同作業を支援するツールである．
**Git** というバージョン管理システムを基盤にしており，開発者がコードを共有し，協力してプロジェクトを進められる．

> 💬 用語の区別：**Git** は手元でバージョンを管理する仕組み，**GitHub** はそれをネット上で共有する場所．

---

## 1. なんで便利なの？

| 機能 | 研究における利点 |
|---|---|
| **バージョン管理** | コードの変更履歴を追跡でき，過去の状態に戻したり，いつ何を変えたかを確認できる |
| **共同作業** | 複数人が同じプロジェクトで同時に作業でき，Pull Request を通じて変更を提案・レビューできる |
| **コードの共有** | 公開することで他の研究者とコードを共有し，フィードバックや共同研究につなげられる |

> 💬 研究の文脈では「論文の図を作ったスクリプトが，半年後にどの版だったか分からなくなる」問題を
> 防げるのが大きい．本リポジトリ自体も GitHub で管理されている．

## 2. まず初めに何をすればいいの？

[Homebrew](../env4mac/sec/homebrew.md) を使って，最新版の `git` と `git-open` をインストールする．

```bash
brew install git git-open
```

インストール後，コミットに記録される名前とメールアドレスを設定しておく．

```bash
git config --global user.name  "Your Name"
git config --global user.email "your_address@example.com"
```

## 3. アカウントを作成しよう

> 📝 **（執筆予定）** アカウント作成と SSH 鍵の登録手順をまとめる予定．
> SSH 鍵の作り方自体は [SystemB へのログイン方法](../../02_external_machine/supercom/sec/systemb_login.md) と共通である．

## 4. 基本操作

> 📝 **（執筆予定）** `clone` / `add` / `commit` / `push` / `pull` と，ブランチ運用についてまとめる予定．

## 5. GitHub Copilot

学生・教員は GitHub Copilot の [Copilot Pro](https://docs.github.com/ja/education/about-github-education) を
無料で利用できる．興味があれば[手順](https://docs.github.com/ja/education/about-github-education)に従って導入してみてほしい．

> 💬 研究活動における AI 利用の考え方については
> [どのように AI を活用するか](../../03_research_hub/research/how_to_utilize_ai.md) を参照．

---

[⬅️ IT・開発環境](../README.md) ｜ [🏠 Home](../../../README.md)
