---
title: "What is Openmx?"
excerpt: "OpenMXについて解説する．"
collection: portfolio
data: 2025-06-09
---

[🏠 Home](03_permanent_notes/250605_cd-mb/environment_setting/doc/openmx/openmx.md)

# OpenMXの基礎理論
<a id="Openmxの基礎理論"></a>

材料計算のシミュレーション手法には，量子化学計算と第一原理計算の二種類がある．
両者は，計算精度と計算コストのバランスにおいて対照的な特性を持つ点が大きな特徴である．
一般に，量子化学計算は主に分子系に適用され，一方で第一原理計算は結晶系に適用されることが多い．
ただし，現代においては量子化学計算と第一原理計算の定義の境界はあやふやになっており，両者の手法や適用範囲が重なる場合も少なくない．

|手法|長所|短所|
|---|---|---|
|量子化学計算|波動関数ベースの議論で，実際の電子状態を扱った高精度計算手法が多い.|計算コストが大きくなりがち．|
|第一原理計算|密度汎関数理論ベースの議論で，多様な擬ポテンシャルを用いた高効率計算手法が多い．|計算精度が汎函数に依存．|


## OpenMXとは何ですか？

<br/>
<img src="../250408_openmx_image/OpenMX_LOGO_S.png" width="20%">
<br/>

[OpenMX](https://www.openmx-square.org/openmx_man3.9jp/) は，日本で開発された第一原理計算ソフトウェアであり，東京大学物性研究所の尾崎泰助教授らを中心に研究・開発が進められてきた．本ソフトの大きな特徴は，孤立原子系の擬ポテンシャル法に基づき，有効擬原子軌道（PAO:Pseduo-Atomic orbital）を局在基底として用いることで，Kohn-Sham方程式を自己無撞着に解き，計算コストを大幅に低減できる点にある—平面波基底法を用いるVASPやQuantum ESPRESSOに比べて，計算コストが非常に小さい．

## ✅ 主な機能と特徴

主な機能と特徴を以下に列挙する：

- 交換相関エネルギーに対する，局所密度近似（LDA, LSDA）と一般化勾配近似（GGA）計算
- 擬ポテンシャルに対するVernderbiltのノルム保存型近似
- DFT+U 計算
- [Effective screening medium mothod](https://sugino.issp.u-tokyo.ac.jp/esm/)
- 速度スケーリング法やNose-Hoover法によるNVTアンサンブル分子動力学
- NEVアンサンブル分子動力学
- スーパーセルより得られるバンド構造を，任意のk-space バンドに変換するband unfolding method
- core-holeを考慮した擬ポテンシャルを利用したXPS計算
- Wannier90, BoltzTrap などの post-processing code の利用計算

> 💬 注意）これはすべての第一原理計算ソフトウェアに共通することだが，擬ポテンシャルの導入や種々の近似，数値的誤差などが含まれるため，計算結果が必ずしも実験結果を正確に再現するとは限らない．

OpenMX は現在v.3.9まで出ており，最新のversionではBerry phaseを用いた巨視的分極率計算が可能であり，[日本語](https://www.openmx-square.org/openmx_man3.9jp/)・[英語](https://openmx-square.org/openmx_man3.9/index.html)両方のマニュアルも非常に充実している．基本わからないことなどは，マニュアルを一度参照してみると結構わかりやすい．

[🏠 Home](03_permanent_notes/250605_cd-mb/environment_setting/doc/openmx/openmx.md)
