---
title: VESTA
excerpt: <excerpt or description on this script>
author: Takeru Nakashima
collection: portfolio
date: 2025-06-06
# Copyright (c) 2025-06-06 <Takeru Nakashima>. All rights reserved.
---

[🏠 Home](../../../README.md)

# Vesta
VESTA は、結晶構造や分子構造の可視化と解析を行うためのソフトウェア．
主に結晶学，材料科学，化学の研究者に利用されている．VESTA は，3D 表示，等高線図，断面図，電子密度分布の可視化など，多様な機能を提供する．

## インストール手順

``` bash
# VESTA のインストール (brewを使用している場合)
$ brew install vesta

# 下記のvestaコマンドを~/.zshrcに追加しておくと便利
$ cat <<EOF >> ~/.zshrc
alias vesta='open -a /Applications/VESTA.app'
EOF

# VESTA の起動
$ vesta
```

[🏠 Home](../../../README.md)
