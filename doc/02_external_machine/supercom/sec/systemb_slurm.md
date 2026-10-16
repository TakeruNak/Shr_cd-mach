---
title: "Queue system (Slurm Workload Manager) の利用"
excerpt: "物性研 SystemB で使われる Slurm の主要コマンド，ジョブスクリプトの書き方，並列数の決め方."
author: "Takeru Nakashima"
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025 Takeru Nakashima. All rights reserved.
---

[🏠 Home](../../../../README.md) › [🖧 外部計算機](../../README.md) › [SystemB](../systemb.md)

# Queue system (Slurm Workload Manager) の利用

## なぜキューシステムがあるのか

大規模計算機は多くの研究者が共有して使うため，使える CPU・GPU・ノードの数には限りがある．
そこで，計算の実行順序を管理する**キューシステム（ジョブスケジューラ）**が導入されている．

利用者は計算を直接実行するのではなく，**「この計算をこの資源で回してほしい」という予約票（ジョブスクリプト）を
スケジューラに投げる**．スケジューラは空き資源ができ次第，順番に計算を実行する．

物性研 SystemB では [**Slurm Workload Manager**](https://mdcl.issp.u-tokyo.ac.jp/scc/system/systembinfo/software) が
採用されている（[Slurm の概要](http://www.dna-ltd.co.jp/slurm_doc/20.02.04/overview.html)）．

---

## 1. ✅ 主要なコマンド

実際に日常的に使うのは **`sbatch` / `squeue` / `scancel` の3つだけ**である．

```bash
# 1. ジョブスクリプトを投入する
sbatch job.sh

# 2. 自分のジョブの状況を確認する（JOBID はここに表示される）
squeue

# 3. ジョブをキャンセルする
scancel {jobID}
```

### ジョブ操作

| コマンド | 説明 |
|---|---|
| `sbatch <script>` | ジョブスクリプトを Slurm に投入する |
| `squeue` | ジョブの実行状況（待機中／実行中）を確認する |
| `scancel <JOBID>` | 実行中・待機中のジョブをキャンセルする |
| `pstat -a` | 各クラスの混雑状況を表示する |
| `point -g` | グループの残ポイント（計算資源の残量）を表示する |

### 環境構築（Environment Modules）

計算コードは `module` コマンドで読み込む．自前でビルドする必要はない．

| コマンド | 説明 |
|---|---|
| `module avail` | 利用可能なモジュールの一覧を表示する |
| `module show <name>` | モジュールの詳細（設定されるパス等）を表示する |
| `module load <name>` | モジュールを読み込む |
| `module list` | 現在読み込まれているモジュールを一覧表示する |
| `module purge` | 読み込み済みのモジュールをすべて解除する |

---

## 2. 🔰 ジョブスクリプトの書き方

Slurm の指示行（`#SBATCH`）を一から覚えるのは効率的ではないので，
以下の実例をコピーして書き換えていくのがよい．

```sh
#!/bin/sh

#SBATCH -p F4cpu     # 使用するクラス（キュー）
#SBATCH -N 4         # 使用するノード数
#SBATCH -n 16        # MPI プロセス数の合計；4 (nodes) x 4 (MPI processes per node)
#SBATCH -c 32        # 1 MPI プロセスあたりの OpenMP スレッド数
#SBATCH -t 00:30:00  # 最大実行時間（この時間を超えると強制終了される）

set -e   # 途中でエラーが出たら以降を実行せず止める

# 計算コードの環境設定を読み込む
source /home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmxvars.sh
module list

openmx_PATH=/home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmx-3.9.9-1/bin

srun -n 16 --cpus-per-task=32 ${openmx_PATH}/openmx ./input/O_Cu8B14Cu111.dat -nt 32
```

### 実行行の読み方

上の `srun` 行を部分ごとに分解すると以下のとおり．

| 要素 | 説明 |
|---|---|
| `srun` | Slurm のコマンド．確保した資源（プロセス数・スレッド数）に従って計算を分散実行する |
| `-n 16` | **MPI プロセスの総数**．4 ノードに 4 プロセスずつ割り当てて合計 16 プロセスになる |
| `--cpus-per-task=32` | **1 MPI プロセスあたりに割り当てる CPU コア数**．OpenMP によるスレッド並列に使われる |
| `${openmx_PATH}/openmx` | 実行ファイルのパス |
| `./input/O_Cu8B14Cu111.dat` | 入力ファイル．計算する構造や計算条件が書かれている |
| `-nt 32` | **OpenMX に渡す OpenMP スレッド数**．`--cpus-per-task` と同じ値にそろえる |

> 💬 まとめると，このジョブは **4 ノードにまたがって 16 個の MPI プロセスを並列実行し，
> 各プロセスがさらに 32 スレッドの OpenMP 並列で計算する**（合計 512 コア）．

---

## 3. 並列数の決め方

SystemB は **1 ノードあたり 128 CPU コア**を持つ．
$N_{\rm MPI}, N_{\rm OpenMP}, N_{\rm Node}$ をそれぞれ MPI プロセス数，OpenMP スレッド数，ノード数とすると，
確保したコアを余らせないためには次を満たすように設定するのがよい．

$$ N_{\rm MPI} \times N_{\rm OpenMP} = 128 \times N_{\rm Node} $$

上の例では $16 \times 32 = 512 = 128 \times 4$ となっており，この関係が満たされている．

> ⚠️ **並列数を上げすぎると，かえって遅くなる．**
> コア間・ノード間のデータ通信時間が増えるためである．
> いきなり大きな並列数で本番を回さず，**小さい系で並列数を段階的に上げて実測し**，
> 効率の落ち始める手前を使うこと．

---

## 4. 実例

OpenMX の NEB 計算を SystemB に投入する例は
[Nudged Elastic Band (NEB) 法 §3](../../../01_computations/openmx/sec/neb.md) を参照．
ジョブスクリプトの実体は
[`openmx/src/job_openmx_systemb.sh`](../../../01_computations/openmx/src/job_openmx_systemb.sh) に置いてある．

---

[⬅️ SystemB](../systemb.md) ｜ [🏠 Home](../../../../README.md)
