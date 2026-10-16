---
title: "pyenv & pipenv を利用した仮想環境"
excerpt: "pipenv による仮想環境の作成と依存パッケージ管理，pyenv との併用手順."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-05
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [🛠️ IT・開発環境](../../README.md) › [Python 環境構築](../environment.md)

# 🐍 pyenv & pipenv を利用した仮想環境

## 1. pipenv とは？

`pipenv` は，**仮想環境の作成と依存パッケージ管理を，一括で行えるコマンド**である．

> 🔧 `virtualenv` + `pip` + `requirements.txt` を1つにまとめた便利なツール．

[pyenv](./pyenv.md) が **Python 本体のバージョン**を管理するのに対し，
pipenv は **その上に入れるパッケージ**を管理する．担当する層が違うので，両者は併用する．

### ✅ 主な特徴

| 機能 | 説明 |
|---|---|
| 仮想環境の自動作成 | プロジェクトごとに自動で仮想環境を作成・管理してくれる |
| パッケージ管理 | `Pipfile` / `Pipfile.lock` を使って依存関係を明確に管理 |
| 再現性の高い環境構築 | `Pipfile.lock` により同じ依存関係の環境を再構築できる |
| Python バージョン指定 | `pyenv` と連携して Python バージョンをプロジェクトごとに設定できる |

### 📄 Pipfile と Pipfile.lock の違い

| ファイル | 内容 |
|---|---|
| `Pipfile` | 開発者がインストールを指定したパッケージの一覧（ざっくり） |
| `Pipfile.lock` | すべての依存関係とバージョンを固定（再現性を保証） |

> 💡 この2ファイルがあれば，別のマシンでも `pipenv install` だけで同じ環境を再現できる．
> **どちらも Git の管理対象に含めること．**

---

## 2. 🔰 よく使うコマンド一覧

| 操作 | コマンド |
|---|---|
| 初期化（指定バージョンの Python） | `pipenv --python 3.11` |
| `Pipfile` から環境を再現 | `pipenv install` |
| パッケージのインストール | `pipenv install numpy` |
| 開発用パッケージのインストール | `pipenv install --dev black` |
| パッケージのアンインストール | `pipenv uninstall numpy` |
| 依存関係を表示 | `pipenv graph` |
| 仮想環境に入る | `pipenv shell` |
| 仮想環境に入らずにスクリプトを実行 | `pipenv run python main.py` |
| 仮想環境（shell）を終了する | `exit` |
| 仮想環境を削除する（`Pipfile` 等は残る） | `pipenv --rm` |

> ⚠️ `pipenv --rm` は慣れないうちは使わないほうがよい．
> 引数なしの `pipenv install` は，ディレクトリ内の `Pipfile` / `Pipfile.lock` をもとに
> 必要なパッケージを一括インストールしてくれる．

---

## 3. 💡 pyenv との併用例

```bash
# 1. pyenv で Python 3.13 をインストール
pyenv install 3.13

# 2. このディレクトリで Python 3.13 を使うことを宣言
pyenv local 3.13

# 3. pipenv に Python 3.13 を使うことを宣言（Pipfile が作成される）
pipenv --python 3.13   # 省略しても動くことが多い

# 4. pipenv で numpy をインストール
pipenv install numpy

# 5. 仮想環境を有効化
pipenv shell

# 6. スクリプトを実行
python test.py

# 7. 仮想環境を終了
exit
```

## 4. ✅ 動作確認用スクリプト

上記手順の `test.py` として，[`src/test.py`](../src/test.py) を用意してある．
numpy のベクトル演算と固有値問題が解ければ環境構築は成功である．

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# --- 1. ベクトルの足し算 ---
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print("c:", c)

# --- 2. 固有値問題を解く ---
# ex: A = [[1, 2], [3, 4]]
A = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)
```

期待される出力：

```
c: [5 7 9]
Eigenvalues:  [-0.37228132  5.37228132]
Eigenvectors:  [[-0.82456484 -0.41597356]
 [ 0.56576746 -0.90937671]]
```

> 💬 固有ベクトルの符号は規格化の取り方によって反転しうるため，環境によって `-` が入れ替わって見えることがある．

---

[⬅️ Python 環境構築](../environment.md) ｜ [🏠 Home](../../../../README.md)
