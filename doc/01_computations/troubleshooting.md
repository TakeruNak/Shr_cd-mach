---
title: "計算のデバッグと開発の作法"
excerpt: "計算コードの出力が読めないとき・自作スクリプトを書くときの調べ方と開発の進め方."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-04-08
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../README.md) › [💡 計算技術](./README.md)

# 計算のデバッグと開発の作法

計算コードを使っていると「出力ファイルに知らない変数が出てきた」「計算が進んでいるのか分からない」
という場面に必ず当たる．ここでは，その都度の調べ方と，自分でスクリプトを書くときの作法をまとめる．

---

## 1. 定義の分からない出力変数を調べる

上から順に試すと，たいていどこかで解決する．

1. **マニュアルを読む．** まずはこれ．多くの変数は索引から引ける．
2. **フォーラムを検索する．** 同じ疑問は先人が投げていることが多い．
   * [OpenMX Forum](https://www.openmx-square.org/forum/patio.cgi)
   * [Quantum ESPRESSO users ML](https://lists.quantum-espresso.org/mailman/listinfo/users)
3. **`grep` でソースと出力を直接探す．** 変数が計算中のどの段階で書かれているかが分かる．

   ```bash
   # 出力ファイル中で Utot が現れる箇所を前後5行つきで表示
   grep -n -C 5 "Utot" *.out

   # ソースコード中の定義箇所を探す
   grep -rn -C 5 "Utot" ~/src/openmx3.9/source/*.c
   ```

## 2. 実行中の計算を監視する

`tail -f` は出力ファイルの末尾を追記されるたびに表示し続ける．SCF が収束に向かっているかを眺めるのに使う．

```bash
tail -f output.std

# SCF の収束履歴だけを追いたい場合
tail -f output.std | grep "NormRD"
```

終了は `Ctrl + C`（計算そのものは止まらない）．

## 3. 自作スクリプトはテスト駆動で書く

解析スクリプトは「一度書いて終わり」ではなく，論文の図を作り直すたびに使い回すことになる．
最初に小さなテストを書いておくと，後からの変更で壊れたことに気づける．

* **考え方**：テスト駆動開発（Test-Driven Development; TDD）．
  藤堂眞治先生（東京大学 物理学専攻）の[プログラム開発の技術](https://hohno0223.github.io/comp_phys_spring_school2023/materials/tdd-tutorial.pdf)が分かりやすい．
* **Python**：[pytest](https://qiita.com/Renki/items/825890f7662ea3ca6850) を使う．
* **Fortran**：[pFUnit](https://github.com/Goddard-Fortran-Ecosystem/pFUnit) を使う．

---

[⬅️ 計算技術](./README.md) ｜ [🏠 Home](../../README.md)
