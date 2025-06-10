---
title: "Openmx Calculation note"
excerpt: "第一原理計算プログラムの一種であるOpenMXを用いた計算演習を通して，第一原理計算の肌感覚を掴む."
collection: portfolio
data: 2025-04-08 10:52
---

[🏠 Home](../../README.md)

# OpenMX 計算概論

以下項目の共有を本稿の目的とする:

1. [OpenMXの基礎理論.](#OpenMXの基礎理論)
2. [基本的なパラメタ設定の勘所・収束のスキル．](#基本的なパラメタ設定の勘所・収束のスキル)
3. [物性研へのログイン方法.](#物性研へのログイン方法)
4. [実計算手法．](#実計算手法)
   1. ~~計算対象をデータベースより取得方法．~~
   2. ~~VESTAを用いた可視化 & ファイル形式の変換スキル~~
   3. [構造最適化の計算スキル．](#構造最適化の計算スキル)
   4. ~~VESTAを用いたスーパーセルの構築スキル．~~
   5. [外部計算機のログイン方法.](#外部計算機のログイン方法)
   6. [Nudged Elastic Band (NEB) methodの計算手法．](#Nudged_Elastic_Band)
---

## OpenMXの基礎理論
<a id="Openmxの基礎理論"></a>

材料計算のシミュレーション手法には，量子化学計算と第一原理計算の二種類がある．
両者は，計算精度と計算コストのバランスにおいて対照的な特性を持つ点が大きな特徴である．
一般に，量子化学計算は主に分子系に適用され，一方で第一原理計算は結晶系に適用されることが多い．
ただし，現代においては量子化学計算と第一原理計算の定義の境界はあやふやになっており，両者の手法や適用範囲が重なる場合も少なくない．

|手法|長所|短所|
|---|---|---|
|量子化学計算|波動関数ベースの議論で，実際の電子状態を扱った高精度計算手法が多い.|計算コストが大きくなりがち．|
|第一原理計算|密度汎関数理論ベースの議論で，多様な擬ポテンシャルを用いた高効率計算手法が多い．|計算精度が汎函数に依存．|

<br/>
<img src="./250408_openmx_image/OpenMX_LOGO_S.png" width="20%">
<br/>

[OpenMX](https://www.openmx-square.org/openmx_man3.9jp/) は，日本で開発された第一原理計算ソフトウェアであり，東京大学物性研究所の尾崎泰助教授らを中心に研究・開発が進められてきた．本ソフトの大きな特徴は，孤立原子系の擬ポテンシャル法に基づき，有効擬原子軌道（PAO:Pseduo-Atomic orbital）を局在基底として用いることで，Kohn-Sham方程式を自己無撞着に解き，計算コストを大幅に低減できる点にある—平面波基底法を用いるVASPやQuantum ESPRESSOに比べて，計算コストが非常に小さい．
主な機能と特徴を以下に列挙する：
- 交換相関エネルギーに対しては，局所密度近似（LDA, LSDA）と一般化勾配近似（GGA）計算
- 擬ポテンシャルに対してはVernderbiltのノルム保存型近似
- DFT+U 計算
- [Effective screening medium mothod](https://sugino.issp.u-tokyo.ac.jp/esm/)
- 速度スケーリング法やNose-Hoover法によるNVTアンサンブル分子動力学
- NEVアンサンブル分子動力学
- スーパーセルより得られるバンド構造を，任意のk-space バンドに変換するband unfolding method
- core-holeを考慮した擬ポテンシャルを利用したXPS計算
- Wannier90, BoltzTrap などの post-processing code の利用計算

注意すべき点として,（これはすべての第一原理計算ソフトウェアに共通することだが,）擬ポテンシャルの導入や種々の近似，数値的誤差などが含まれるため，計算結果が必ずしも実験結果を正確に再現するとは限らない．

OpenMX は現在v.3.9まで出ており，最新のversionではBerry phaseを用いた巨視的分極率計算が可能であり，[日本語](https://www.openmx-square.org/openmx_man3.9jp/)・[英語](https://openmx-square.org/openmx_man3.9/index.html)両方のマニュアルも非常に充実している．基本わからないことなどは，マニュアルを一度参照してみると結構わかりやすい．

---

## 基本的なパラメタ設定の勘所・収束のスキル
<a id="基本的なパラメタ設定の勘所・収束のスキル"></a>

OpenMX における重要なパラメタを以下に列挙し，順に説明していく:

 - 擬ポテンシャル (Definition.of.Atomic.Species)
     - **従来型擬ポテンシャル**
     - オープンコア型擬ポテンシャル
     - 内殻準位励起のための擬ポテンシャル
 - 有効擬原子基底 (Definition.of.Atomic.Species)
     - Quick
     - **Standard**
     - Precise
 - 交換相関エネルギー(scf.XcType)
     - LDA
     - LSDA-CA
     - LSDA-PW
     - **GGA-PBE**
 - カットオフエネルギー（scf.energycutoff）
 - 電子温度 （scf.ElectronicTemperature）
 - K空間メッシュ （scf.Kgrid）
 - Kohn-Sham方程式のバンドエネルギートータル差分の収束条件 (scf.criterion)

Kohn-Sham方程式の自己無撞着計算(SCF, self-consistent field)に関連するパラメタは，`scf.###`という入力パラメタ変数が採用されている．一方で，構造最適化やNEB計算などの原子座標を動かす計算に関連するパラメタは,`MD.###`という入力パラメタ変数が採用されている．
**そのため，SCF計算で問題が生じた場合は`scf.###`パラメタを，MD計算に問題が生じた場合は`MD.###`パラメタをそれぞれ精査することが，計算エラー解決のための一つの有効な指針になる．**

- *擬ポテンシャル*  
    擬ポテンシャルは，入力パラメタ`Definition.of.Atomic.Species`の1列目で定義する．
    擬ポテンシャルの選択肢には，従来型擬ポテンシャル，オープンコア型擬ポテンシャル，内殻準位励起のための擬ポテンシャルの3種類がある．基底状態の計算には，従来型の擬ポテンシャルを用いれば良い．
    図1はOpenMXの[website](https://www.openmx-square.org/openmx_man3.9jp/node27.html)から持ってきたものであり，Table1,2のVPS欄を参照して選択するとよい．

- *有効擬原子軌道*  
    有効擬原子軌道は，入力パラメタ`Definition.of.Atomic.Species`の２列目で定義する．
    有効擬原子軌道は，すでにベンチマーク計算（図1参照）により最適化された[データベース](https://www.openmx-square.org/openmx_man3.9jp/node27.html)が提供されているので，そちらを利用するとよい．基本はStandardの利用で良い．

- *交換相関エネルギー*  
    交換相関エネルギーは，入力パラメタ`scf.XcType`で定義する．
    交換相関エネルギーには，GGA-PBEかLDAの選択を初めての計算では利用しすると良い．

- [*カットオフエネルギー*](https://www.openmx-square.org/openmx_man3.8jp/node37.html)  
    カットオフエネルギーは，入力パラメタ`scf.energycutoff`によって制御される．私の経験では，`200~250 Ry`程度の値を用いることで，多くの系は十分な収束が得られる印象である．
    **特に構造最適化計算においては重要なパラメタであり，値を大きく設定することで計算の収束性が向上する場合がある．**
    これは，カットオフエネルギーの値が小さいと実空間メッシュが粗くなり，その結果として原子位置が最適化プロセス中に振動しやすくなるためである．

- *電子温度*  
    電子温度は，入力パラメタ`scf.ElectronicTemperature`で定義する．
    Kohn-Sham方程式の自己無撞着計算では，Fermiエネルギー近傍でのバンドの取り扱いには工夫が必要である．初めての計算では，電子温度は300K程度で計算をすることを推奨．

- *K空間メッシ*  
    K空間メッシュは，入力パラメタ`scf.KGrid`で定義される．
    K空間メッシュは，k-spaceにおける格子の差分を定義しており，セルの大きい系や構造最適化計算には関与しない．今回は説明を省略（2025.04.21:いづれ追記する）．

- *Kohn-Sham方程式のバンドエネルギーのトータル差分についての，収束条件*  
    Kohn-Sham方程式のSCF計算の収束条件は，入力パラメタ`scf.criterion`によって定義される．
Default値は`1.0E-6 [Hrtree]`．基本的に，デフォルト値よりも深い値を設定したほうが良い．`1.0 [Hartree] = 27.21 [eV]`である．仮に`100`原子のモデルを考えた際に，`1.0E-3 [eV]`のオーダーまで収束させたい場合は，以下のような概算を行なうことで，citerioaの値の定義の概算を算出できる．

$$ \rm{eV}における欲しい精度の桁数 /(原子数\times 30) [\rm{Hartree}] $$
$$= 1.0\times 10^{-3}/(100\times 30) [\rm{Hartree}]\simeq 1.0\times 10^{-7} [Hartree]$$

- *Kohn-Sham方程式の自己無撞着計算の際の電子密度推定のパラメタ*   
   電子密度によって，Kohn-Shamの有効ポテンシャルは決定づけられるがそのうち，
    Kohn-Sham方程式の自己無撞着計算を行う際には，各SCF計算のステップごとに電子密度を新しいものに更新する．電子密度を過去の電子密度と混ぜて，新しい電子密度を作成し，汎函数理論の枠組みから交換相関ポテンシャルを作成し，再びKohn-Sham方程式を
    具体的には，`scf.Mixing.Type`は電子密度の更新手法を意味し，`scf.###.Mixing.Weight`は電子密度の
    ```
    # -----------------------------------------------------------
    # Example of mixing parameters for Update of electron density
    # -----------------------------------------------------------

    scf.Mixing.Type               rmm-diisk # 基本) rmm-diiskを使用
    scf.Init.Mixing.Weight        0.05      # 初期の電子密度の混合比
    scf.Min.Mixing.Weight         0.01      # 混合比の最小比
    scf.Max.Mixing.Weight         0.30      # 混合比の最大比
    scf.Mixing.History            25        # 混合時の参照履歴の定義
    scf.Mixing.StartPulay         15        # 気にしない（他パラメタチューニングでうまくいく）
    ```


<figure style="text-align:center;">
  <img src="./250408_openmx_image/openmx_basis_table.png" width="100%">
  <figcaption style="font-size:20px; margin-top:5px;">図1: OpenMX VPS & PAO Tables</figcaption>
</figure>

---


## 補足) 物性研へのログイン方法
<a id="物性研へのログイン方法"></a>

大規模計算の実行には，一般に外部計算機を利用する．ここでは物性研 [systemB Ohtaka](https://mdcl.issp.u-tokyo.ac.jp/scc/system/systembinfo) でアカウントを取得した場合の簡単なログイン方法と，Quesub systemの利用と並列化に関して記述する．

systemB ohtaka の入門マニュアルは，[website](https://mdcl.issp.u-tokyo.ac.jp/scc/system/systembinfo/manual) で入手可能であるので各自で参考にすると利用がスムーズになる:特に，[利用の手引き](https://mdcl.issp.u-tokyo.ac.jp/scc/manual-B/SystemB_User%27s_Guide_Rev2.7_JP.pdf)と[利用講習会のスライド](https://mdcl.issp.u-tokyo.ac.jp/scc/manual-B/ISSP20201127_B_Dell.pdf)では，頻繁に使うコマンドがまとめて紹介されており，初学者には参考になる．

### ssh 接続を行うための公開鍵の登録．
利用者登録が完了すると，各登録メールアドレス宛にSSH公開鍵登録システムへのURLが送られてくる（図2参照）．これらのwebsiteの指示にしたがって，SSH公開鍵の登録をすすめる（図3）．
ssh鍵の登録は，Qiitaの記事などを参考にすると良い．**注意しべき点として，決して秘密鍵の登録をしないようにお願いします．**

- [Mac用](https://qiita.com/soma_sekimoto/items/35845495bc565c38ae9d)
- [Windos用](https://qiita.com/digdagdag/items/9e5c061e7d86e0af9a57)

<figure style="text-align:center;">
  <img src="./250408_openmx_image/公開鍵登録システム_1.png" width="80%">
  <figcaption style="font-size:20px; margin-top:5px;">図2: 公開鍵登録システムログイン画面</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="./250408_openmx_image/公開鍵登録システム_2.png" width="80%">
  <figcaption style="font-size:20px; margin-top:5px;">図3: 公開鍵登録画面</figcaption>
</figure>

鍵の登録後，sshでのアクセスが可能となる．ログイン方法は以下のコマンドをターミナルソフト上で入力：
``` zsh
ssh -l {username} ohtaka.issp.u-tokyo.ac.jp
or
ssh {username}@ohtaka.issp.u-tokyo.ac.jp
or
ssh -i{ssh-key_path} {username}@ohtaka.issp.u-tokyo.ac.jp
```
Windows利用者は，可能であれば Windows Terminal + WSL のセットアップを推奨．
個人的には，[Windows Terminal + WSL](https://www.nedia.ne.jp/blog/tech/2022/06/07/19314)環境下で，Linuxコマンドを使えるようにすると便利だと思う．

---

### Queue system (Slurm Workload Manager) の利用．
大規模計算機は多くの研究者によって利用されるが，実際に使えるCPU・GPU/nodeの数には限りがある．そこで，一般に複数人で共有されるような大規模計算機には，queue systemという計算シミュレーションの実行順序を管理するようなスケジュール機能が導入されている．
物性研 systemB では，queue systemの一つである [**Slurm Workload Manager**](https://mdcl.issp.u-tokyo.ac.jp/scc/system/systembinfo/software) が導入されており，systemBの利用者はslurmに計算シミュレーションの予約を投げることで，計算シミュレーションを大勢で効率良く実行している．詳細は以下の[website](http://www.dna-ltd.co.jp/slurm_doc/20.02.04/overview.html)を参照．

実際に,重要なslurm commandを以下に列挙する：

|Slurm command | Output |
|---|---|
|squeue| `squeue` confirms the state of jobs.|
|sbatch (Scrath name)| `sbatch` subimits a batch script to Slurm.|
|scancel (JOB ID)| `scancel` cancels the runnnig job.|
|point -g |    `point` informs the points of group. |
|module avail |    `module avail` lists the available module. |
|module show (Name of Module) |    `module show` displays the details of module. |
|module load (Name of Module) |    `module load` loads the module. |
|module list |    `module list` lists the modules the system loaded. |
|module purge |    `module purge` unload all modules. |
|pstat -a |    `pstat` show the each classs status |

主に使用するcommandは `sbatch`, `squeue`, `scancel` の3つのみである．具体的には，
```
#  1. job script を sbatch でslurmに投入：
sbatch job.sh 

# 2. 計算状況の確認：
squeue

# 3. 計算のキャンセル，JOBIDはsqueueを入力した際に出力される：
scancel {jobID}
```

slurm systemへのjob scriptの環境変数の定義を覚えるのは，あまり効率的ではないので以下に実際のスクリプトファイルを示す：

``` sh
#!/bin/sh

#SBATCH -p F4cpu # 使用するクラス選択
#SBATCH -N 4    # 使用するNode数
#SBATCH -n 16   # 使用するMPIプロセス数の合計；　4 (nodes) x 4 (MPI processes per node)
#SBATCH -c 32   # 32 threads per MPI process
#SBATCH -t 00:30:00

set -e
source /home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmxvars.sh
module list
openmx_PATH=/home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmx-3.9.9-1/bin

srun -n 16 --cpus-per-task=32 ${openmx_PATH}/openmx ./input/O_Cu8B14Cu111.dat -nt 32

# 
# srun -n 16 --cpus-per-task=32 openmx ./input/O_Cu8B14Cu111.dat -nt 32
#
```

下記にコマンドの詳細を部分ごとに説明する：

|Command|Description|
|---|---|
|srun| slurm commandで、指定されたプロセスを並列に実行. 指定されたリソース（プロセス数やスレッド数など）に基づいて,計算を分散して実行する.|
|-n 16| MPIプロセスの総数を指定.この場合，全体で16個のMPIプロセスが実行される．4ノードにそれぞれ4つのプロセスが割り当てられ，合計16プロセスになる．|
|--cpus-per-task=8| 各MPIプロセスに対して割り当てるCPUコア（スレッド）の数を指定する．ここでは，各プロセスに8つのスレッドが割り当てられている．このスレッド数は，OpenMPなどのマルチスレッド並列化に使用される．|
|${openmx_PATH}/openmx| OpenMX実行ファイルのパス.${openmx_PATH} はOpenMXの実行ファイルが存在するディレクトリのパスを表し，その中の openmx が実行ファイル．|
|./input/O_Cu8B14Cu111.dat| OpenMXに入力として渡されるデータファイル．このファイルには，計算する構造や条件などの情報が含まれている．|
|-nt 8| OpenMXに渡されるオプションで，OpenMPスレッドの数を指定する．この場合，8つのスレッドが指定されている． これは，各MPIプロセスが8つのOpenMPスレッドを使って並列計算を行うことを意味する．|

まとめると， このコマンドは，4ノードにまたがって合計16個のMPIプロセスを並列に実行し，各プロセスは8つのOpenMPスレッドを使用して計算を行う．これにより，全体の計算が効率的に分散処理される．
systemB は 1 nodeあたり128 cpu coreを持つことから, $N_{MPI}，N_{OpenMP}, N_{Node}$ をそれぞれMPIプロセス数，OpenMPプロセス数，Node数としたとき，
$$ N_{MPI} \times N_{OpenMP}. = 128 \times N_{Node}.$$
を満たすように，それぞれのパラメタを設定するのが良い．
**ただし，並列数をあまり上げすぎてもcpu間，node間のデータ通信時間が増えてしまう問題もあるため，並列数は徐々に増やしていくのが良い．**

---


## 実計算手法.
<a id="実計算手法"></a>

以下に，構造最適化とNEB計算のコツを記述する．

### 構造最適化
<a id="構造最適化の計算スキル"></a>

[構造最適化](https://www.openmx-square.org/openmx_man3.9jp/node47.html)に関する詳細は，OpenMXのwebsiteを参照．
MD.Typeは，構造最適化の手法はまずはRFで実行するのが良い．収束が悪い場合は，`MD.Opt.DIIS.History` を増やしてみると良い．

``` openmx.dat
# ---------------------------------------------
# INPUT EXAMPLE| OpenMX params. for Optimizaion
# ---------------------------------------------

# ------------------------------------
# Geometry Optimization and Molecular dynamics
# ------------------------------------
MD.Type                      RF     # Opt|DIIS|BFGS|RF|EF
MD.Opt.DIIS.History          3      # default=3
MD.Opt.StartDIIS             5      # default=5
MD.Opt.EveryDIIS            200     # default=200
MD.maxIter                  100     # default=1
MD.Opt.criterion            1.0e-4  # default=0.0003 (Hartree/Bohr)

# ----------------------------------
# Deepest layer is fiexed in the optimization
# ----------------------------------
<MD.Fixed.XYZ
1 1 1 1
2 0 0 0
3 0 0 0
4 0 0 0
5 0 0 0
6 0 0 0
7 0 0 0
MD.Fixed.XYZ>
```

### Nudged Elastic Band (NEB) method
NEB計算と構造最適化計算の間には，共通したパラメタが存在する．
NEB計算特有のパラメタで重要となるものは，`MD.NEB.Number.Images`と
`NEB.Atoms.SpeciesAndCoordinates`ブロックである．
`MD.NEB.Number.Images` はNEB計算の際の初状態と終状態の間の中間状態の個数を示す．
`NEB.Atoms.SpeciesAndCoordinates`ブロックは，終状態の結晶構造を定義する．定義方法は，
`Atoms.SpeciesAndCoordinates`ブロックでの結晶構造の書式と同様．
`Atoms.SpeciesAndCoordinates`が始状態に対応し，`NEB.Atoms.SpeciesAndCoordinates`が終状態の結晶構造に対応する．

中間状態のimage座標を与えない場合は，始状態と終状態を`MD.NEB.Number.Images`数で線形補間した構造が
初期のimage構造（中間状態）に対応する．


```
# ---------------------------------
# NEB: MD or Geometry Optimization
# ---------------------------------

MD.Type                     NEB        # Nomd|Opt|DIIS|NVE|NVT_VS|NVT_NH
MD.Opt.DIIS.History          4         # default=7
MD.Opt.StartDIIS            10         # default=5
MD.maxIter                  100        # default=1
MD.TimeStep                 1.0        # default=0.5 (fs)
MD.Opt.criterion         1.0e-4        # default=1.0e-4 (Hartree/bohr)

MD.NEB.Number.Images        8         # default=10


#
# The coordinates of product
#
<NEB.Atoms.SpeciesAndCoordinates
   1    C   -0.77755846408657   -0.00000003553856   -0.77730141035137     2.0     2.0
   2    C    0.77681707294741   -0.00000002413166   -0.77729608216595     2.0     2.0
   3    H    1.23451821718817   -0.88763832172374   -1.23464057728123     0.5     0.5
   4    H    1.23451823170776    0.88763828275851   -1.23464059022330     0.5     0.5
   5    H   -1.23506432458023   -0.88767426830774   -1.23470899088096     0.5     0.5
   6    H   -1.23506425800395    0.88767424658723   -1.23470896874564     0.5     0.5
   7    C   -0.77755854665393    0.00000000908006    0.77730136931056     2.0     2.0
   8    C    0.77681705017323   -0.00000000970885    0.77729611199476     2.0     2.0
   9    H    1.23451826851556   -0.88763828740000    1.23464060936812     0.5     0.5
  10    H    1.23451821324627    0.88763830875131    1.23464061208483     0.5     0.5
  11    H   -1.23506431230451   -0.88767430754577    1.23470894717613     0.5     0.5
  12    H   -1.23506433587007    0.88767428525317    1.23470902573029     0.5     0.5
NEB.Atoms.SpeciesAndCoordinates>
```

## 具体例コード
東京大学物性研systemB Ohtaka上での計算を念頭におき，NEB計算用のインプットファイルを`c2h4_neb.dat`とする．

<details><summary> c2h4_neb.dat </summary>

``` 
#
# File Name
#

DATA.PATH {PATH OF DFT_DATA19}

System.CurrrentDirectory         ./    # default=./
System.Name                      c2h4
level.of.stdout                   1    # default=1 (1-3)
level.of.fileout                  1    # default=1 (0-2)

#
# Definition of Atomic Species
#

Species.Number       2
<Definition.of.Atomic.Species
 C   C7.0-s2p2d1    C_PBE19
 H   H6.0-s2p1      H_PBE19
Definition.of.Atomic.Species>

#
# Atoms
#

Atoms.Number         12
Atoms.SpeciesAndCoordinates.Unit   Ang # Ang|AU
<Atoms.SpeciesAndCoordinates
   1    C   -0.66829065594143    0.00000000101783   -2.19961193219289     2.0     2.0
   2    C    0.66817412917689   -0.00000000316062   -2.19961215251205     2.0     2.0
   3    H    1.24159214112072   -0.92942544650857   -2.19953308980064     0.5     0.5
   4    H    1.24159212192367    0.92942544733979   -2.19953308820323     0.5     0.5
   5    H   -1.24165800644131   -0.92944748269232   -2.19953309891389     0.5     0.5
   6    H   -1.24165801380425    0.92944749402510   -2.19953309747076     0.5     0.5
   7    C   -0.66829065113509    0.00000000341499    2.19961191775648     2.0     2.0
   8    C    0.66817411530651   -0.00000000006073    2.19961215383949     2.0     2.0
   9    H    1.24159211310925   -0.92942539308841    2.19953308889301     0.5     0.5
  10    H    1.24159212332935    0.92942539212392    2.19953308816332     0.5     0.5
  11    H   -1.24165799549343   -0.92944744948986    2.19953310195071     0.5     0.5
  12    H   -1.24165801426648    0.92944744880542    2.19953310162389     0.5     0.5
Atoms.SpeciesAndCoordinates>
Atoms.UnitVectors.Unit             Ang # Ang|AU
<Atoms.UnitVectors
 11.0  0.0  0.0
  0.0 10.0  0.0
  0.0  0.0 14.0
Atoms.UnitVectors>

#
# SCF or Electronic System
#

scf.XcType                 GGA-PBE     # LDA|LSDA-CA|LSDA-PW|GGA-PBE
scf.SpinPolarization       off         # On|Off|NC
scf.ElectronicTemperature  600.0       # default=300 (K)
scf.energycutoff           170.0       # default=150 (Ry)
scf.maxIter                100         # default=40
scf.EigenvalueSolver       cluster     # DC|GDC|Cluster|Band
scf.Kgrid                  1 1 1       # means n1 x n2 x n3
scf.Mixing.Type           rmm-diisk    # Simple|Rmm-Diis|Gr-Pulay|Kerker|Rmm-Diisk
scf.Init.Mixing.Weight     0.05        # default=0.30
scf.Min.Mixing.Weight      0.001       # default=0.001
scf.Max.Mixing.Weight      0.400       # default=0.40
scf.Mixing.History          20         # default=5
scf.Mixing.StartPulay       6          # default=6
scf.Mixing.EveryPulay       1          # default=6
scf.Kerker.factor          8.0         # default=1.0
scf.criterion             1.0e-8       # default=1.0e-6 (Hartree)

##

MD.Type                     NEB        # Nomd|Opt|DIIS|NVE|NVT_VS|NVT_NH
MD.Opt.DIIS.History          4         # default=7
MD.Opt.StartDIIS            10         # default=5
MD.maxIter                  100        # default=1
MD.TimeStep                 1.0        # default=0.5 (fs)
MD.Opt.criterion         1.0e-4        # default=1.0e-4 (Hartree/bohr)

MD.NEB.Number.Images        8         # default=10

<NEB.Atoms.SpeciesAndCoordinates
   1    C   -0.77755846408657   -0.00000003553856   -0.77730141035137     2.0     2.0
   2    C    0.77681707294741   -0.00000002413166   -0.77729608216595     2.0     2.0
   3    H    1.23451821718817   -0.88763832172374   -1.23464057728123     0.5     0.5
   4    H    1.23451823170776    0.88763828275851   -1.23464059022330     0.5     0.5
   5    H   -1.23506432458023   -0.88767426830774   -1.23470899088096     0.5     0.5
   6    H   -1.23506425800395    0.88767424658723   -1.23470896874564     0.5     0.5
   7    C   -0.77755854665393    0.00000000908006    0.77730136931056     2.0     2.0
   8    C    0.77681705017323   -0.00000000970885    0.77729611199476     2.0     2.0
   9    H    1.23451826851556   -0.88763828740000    1.23464060936812     0.5     0.5
  10    H    1.23451821324627    0.88763830875131    1.23464061208483     0.5     0.5
  11    H   -1.23506431230451   -0.88767430754577    1.23470894717613     0.5     0.5
  12    H   -1.23506433587007    0.88767428525317    1.23470902573029     0.5     0.5
NEB.Atoms.SpeciesAndCoordinates>
```
</details>

計算環境によっては，basisと擬ポテンシャルのデータセットを特定の場所に置いていると思うので，以下のような`DATA.PATH`変数にDFT_DATA19などのPAO, VPSのパスを定義する必要性がある．
systemBでは下記のように，`c2h4_neb.dat` に追記すれば良い:
```
DATA.PATH /home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmx-3.9.9-1/DFT_DATA19
```

<details><summary> job-openmx.sh </summary>

```
#SBATCH -p i8cpu
#SBATCH -N 4
#SBATCH -n 16
#SBATCH -c 32
#SBATCH -t 00:30:00
 
set -e
source /home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmxvars.sh
module list

# DATA.PATH /home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmx-3.9.9-1/DFT_DATA19
 
# srun openmx input/###.dat
srun -n 16 --cpus-per-task=32 openmx c2h4.dat -nt 32
```

</details>

を用いて，以下のコマンドを入力する．
```sh
sbatch job-opemx.sh
```

---

## プログラミングのコツ書き
<a id="プログラミングのコツ書き"></a>
出力ファイルに定義のわからない変数が出た場合は，以下の手順で調べるとうまくいく．

1. マニュアルを読む．
2. 計算ソフトのForumを確認する．例として以下のforumをあげる:[OpenMX](https://www.openmx-square.org/forum/patio.cgi), [Quantum EPSRESSO](https://lists.quantum-espresso.org/mailman/listinfo/users).
3. grep コマンドを利用して，変数の定義されている場所を探す: 具体例として，Utotがわからない場合の例，
    ` grep -5 "Utot" *.out` or `grep -5 "Utot" *.c`
4. 出力中のファイルの状況などは，`tail`コマンドを利用して確認するとよい．
    ```
    tail -f 出力ファイル名
    ```
5. プログラミング開発は，テスト駆動型開発(test-driden development; TDD)を推奨．参考資料は，藤堂眞治先生（Department of Phys. UTokyo）が提供している[プログラム開発の技術](https://hohno0223.github.io/comp_phys_spring_school2023/materials/tdd-tutorial.pdf)を参照．
6. Python codeを用いた開発には，[pytest](https://qiita.com/Renki/items/825890f7662ea3ca6850)を用いたTDDを推奨．Fortranに対しては，[pFUnit](https://github.com/Goddard-Fortran-Ecosystem/pFUnit).

[🏠 Home](../../README.md)
