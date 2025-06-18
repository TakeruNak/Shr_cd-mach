---
title: "pyenvとpipenvの使い方"
excerpt: "Pythonの仮想環境を簡単に管理する方法"
author: Takeru Nakashima
collection: portfolio
date: 2025-06-05
# Copyright (c) 2025-06-05 <Takeru Nakashima>. All rights reserved.
---
[🏠 Home](../environment.md)
# pyenv & pipenv 仮想環境．

`pipenv`は，**仮想環境の作成と依存パッケージ管理を，一括で行えるコマンド**.
> 🔧 「`virtualenv` + `pip` + `requirements.txt`」 を 1 つにまとめた便利なツール.

## ✅ 主な特徴

| 機能 | 説明 |
|------|------|
| 仮想環境の自動作成 | プロジェクトごとに自動で `venv` を作成・管理してくれる |
| パッケージ管理 | `Pipfile` / `Pipfile.lock` を使って依存関係を明確に管理 |
| 再現性の高い環境構築 | `Pipfile.lock` により同じ依存関係の環境を再構築可能 |
| Python バージョン指定 | `pyenv` と連携して Python バージョンをプロジェクトごとに設定可能 |

---

## 📄 Pipfile と Pipfile.lock の違い

| ファイル | 内容 |
|---------|------|
| `Pipfile` | 開発者がインストールを指定したパッケージの一覧（ざっくり） |
| `Pipfile.lock` | すべての依存関係とバージョンを固定（再現性保証） |

---

## 🔰 よく使うコマンド一覧

| 操作 | コマンド |
|------|----------|
| 初期化（指定バージョンの Python） | `pipenv --python 3.11` |
| パッケージのインストール | `pipenv install numpy` |
| 開発用パッケージのインストール | `pipenv install --dev black` |
| 仮想環境に入る | `pipenv shell` |
| 仮想環境内でスクリプト実行 | `pipenv run python main.py` |
| 依存関係を表示 | `pipenv graph` |

---


## 💡 `pyenv` との併用例

```bash
# 1. python v.3.13 を pyenv を利用して，インストール．
pyenv install 3.13

# 2. python v.3.13 を pyenv で利用を宣言する．
pyenv local 3.13

# 3. python v.3.13 を使うことを pipenv で宣言．Pipfile などが作成される．
pipenv --python 3.13 # このコマンドはなくても，実際にいはうまくいく．

# 4. pipenv を用いて，numpy をインストール．
pipenv install numpy

# 5. pipenv の仮装環境を有効化
pipenv shell

# 6. test.py ファイルを python で実行
python test.py
```
ここで使用する `test.py` を念のために以下のように提案しておく：

``` test.py
# -*- coding: utf-8 -*-
# test.py

import numpy as np

# ベクトルの足し算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print("c:, c)

# 固有値問題を解く．
# ex: A = [[1, 2], [3, 4]]
A = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalgeig(A)

print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)

```

[🏠 Home](../environment.md)
