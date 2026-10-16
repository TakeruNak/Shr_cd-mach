---
title: "VESTA 利用ガイド"
excerpt: "結晶・分子構造の可視化と解析を行う VESTA の導入方法."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-06
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../README.md) › [💡 計算技術](../README.md)

# VESTA 利用ガイド

[VESTA](https://jp-minerals.org/vesta/jp/) は，**結晶構造や分子構造の可視化と解析**を行うソフトウェアである．
結晶学・材料科学・化学の分野で広く使われており，3D 表示のほか，等高線図，断面図，
電子密度分布の可視化など多様な機能を備える．

計算との関係では，主に次の2つの用途で使う．

| 用途 | 具体例 |
|---|---|
| **入力の下ごしらえ** | データベースから取得した構造の確認，スーパーセルの構築，ファイル形式の変換 |
| **出力の可視化** | OpenMX の `*.cube`，QE の電荷密度など，計算結果の空間分布を見る |

---

## インストール手順（macOS）

```bash
# 1. Homebrew でインストール
brew install vesta

# 2. ターミナルから起動できるよう ~/.zshrc にエイリアスを追加しておくと便利
cat <<'EOF' >> ~/.zshrc
alias vesta='open -a /Applications/VESTA.app'
EOF

# 3. 設定を読み込んで起動
source ~/.zshrc
vesta
```

> 💬 エイリアスを登録しておくと，`open hoge.cube` あるいは Finder からのダブルクリックで
> そのまま VESTA が開くようになる．OpenMX の出力確認が一気に楽になる．

Homebrew が未導入の場合は [🍺 Homebrew のインストール](../../04_IT/env4mac/sec/homebrew.md) を参照．

---

[⬅️ 計算技術](../README.md) ｜ [🏠 Home](../../../README.md)
