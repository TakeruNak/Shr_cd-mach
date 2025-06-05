---
title: homebrew.md
excerpt: <excerpt or description on this script>
author: Takeru Nakashima
collection: portfolio
date: 2025-06-05
# Copyright (c) 2025-06-05 <Takeru Nakashima>. All rights reserved.
---

# pyenvのインストール
`pyenv`は，**複数のpython versionを簡単に切り替えて管理することができるソフト（Python バージョンマネージャー）**.

## 🐍 pyenv の役割

- システムに複数の Python バージョンをインストール・管理できる
- プロジェクトごとに異なる Python バージョンを使い分けられる
- システムの Python に影響を与えず、安全に開発環境を構築できる

## 🔧 よく使うコマンド

| 操作内容                 | コマンド例                  |
| -------------------- | ---------------------- |
| Python のインストール       | `pyenv install 3.11.9` |
| グローバル（全体）に使うバージョンを設定 | `pyenv global 3.11.9`  |
| カレントディレクトリ用のバージョン設定  | `pyenv local 3.9.13`   |
| 現在使っているバージョンの確認      | `pyenv version`        |
| インストール済みバージョンの一覧     | `pyenv versions`       |

## 🐍 pyenv のインストール

Homebrew のインストールに成功していれば， `pyenv` は以下のコマンドをTerminalに入力することで簡単にインストールすることが可能である．

``` zsh
# ... pyenv インストール ...
brew install pyenv
```
インストールが終了した後に，以下のコマンドを入力して，pyenvの環境を設定してください．
```
# ... pyenv の設定を.zshrcに追加 ...
$ cat <<'EOF' >> ~/.zshrc
# ... pyenv ...
export PYENV_ROOT="\$HOME/.pyenv"
export PATH="\$PYENV_ROOT/bin:\$PATH"
eval "\$(pyenv init --path)"
eval "\$(pyenv init -)"
EOF
```

## 🐍 pyenv の確認
pyenvがうまくインストールできてるか実際に，python をインストールして確認してみましょう．
```
# 1. Home directory に移動
$ cd ~

# 2. workspace 用の directory を作成
$ mkdir workspace

# 3. 作成した workspace に移動
$ cd workspace

# 4. python version 3.13 をインストールしてみよう．（version 3.13以外にも入れてみてください．）
$ pyenv install 3.13

# 5. インストールした pyenv の version を確認してみよう．
$ pyenv version

# 6. python v.3.13 を workspace directory で使ってみよう.
$ pyenv local 3.13

# 7. python 3.13 が workspace directory でちゃんと使えるか確認してみとう．
$ python --version
```

[🏠 Home](../environment.md)