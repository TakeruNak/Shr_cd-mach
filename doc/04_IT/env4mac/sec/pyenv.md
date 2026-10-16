---
title: "pyenv のインストール"
excerpt: "複数の Python バージョンを切り替えて管理する pyenv の導入と使い方."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-05
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [🛠️ IT・開発環境](../../README.md) › [Python 環境構築](../environment.md)

# 🐍 pyenv のインストール

## 1. pyenv とは？

`pyenv` は，**複数の Python バージョンを簡単に切り替えて管理できるソフトウェア**（Python バージョンマネージャ）である．

### 役割

* システムに複数の Python バージョンをインストール・管理できる
* プロジェクトごとに異なる Python バージョンを使い分けられる
* **システムの Python に影響を与えず**，安全に開発環境を構築できる

> 💬 macOS に最初から入っている Python を直接書き換えると OS 側の動作に支障が出ることがある．
> pyenv を使う最大の理由はこれを避けることにある．

### 🔧 よく使うコマンド

| 操作内容 | コマンド例 |
|---|---|
| Python のインストール | `pyenv install 3.11.9` |
| インストール可能なバージョンの一覧 | `pyenv install --list` |
| グローバル（全体）に使うバージョンを設定 | `pyenv global 3.11.9` |
| カレントディレクトリ用のバージョン設定 | `pyenv local 3.9.13` |
| 現在使っているバージョンの確認 | `pyenv version` |
| インストール済みバージョンの一覧 | `pyenv versions` |

> 💡 `pyenv local` を実行すると，そのディレクトリに `.python-version` というファイルが作られる．
> 以降，そのディレクトリ配下では自動的に指定したバージョンが使われる．

---

## 2. インストール

[Homebrew](./homebrew.md) の導入が済んでいれば，以下のコマンドだけでよい．

```bash
brew install pyenv
```

## 3. シェルの設定

インストール後，`pyenv` をシェルから使えるようにするため `~/.zshrc` に設定を追加する．

```bash
# Editor を開いて .zshrc を編集する（vim 以外の好きな Editor でもよい）
vim ~/.zshrc
```

以下の内容を `.zshrc` の末尾に追加する．

```bash
# pyenv settings
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

編集後，設定を反映させる．

```bash
source ~/.zshrc
```

## 4. ✅ 動作確認

実際に Python をインストールして，切り替えが効くことを確認する．

```bash
# 1. ホームディレクトリに移動
cd ~

# 2. 作業用ディレクトリを作成して移動
mkdir -p workspace && cd workspace

# 3. Python 3.13 をインストール（他のバージョンも入れてみるとよい）
pyenv install 3.13

# 4. インストール済みのバージョンを確認
pyenv versions

# 5. このディレクトリで Python 3.13 を使うことを宣言
pyenv local 3.13

# 6. 実際に 3.13 が使われているか確認
python --version
```

`Python 3.13.x` と表示されれば成功である．

---

次は [🐍 pyenv & pipenv を利用した仮想環境](./pyenv_pipenv.md) へ進む．

[⬅️ Python 環境構築](../environment.md) ｜ [🏠 Home](../../../../README.md)
