---
title: systemb_slurm.md
excerpt: "物性研 SystemB で利用されている Slurm Workload Manager の利用方法について解説"
author: Takeru Nakashima
collection: portfolio
date: 2025-06-10
# Copyright (c) 2025-06-10 <Takeru Nakashima>. All rights reserved.
---

[🏠 Home](systemb.md)

# Queue system (Slurm Workload Manager) の利用．
大規模計算機は多くの研究者によって利用されるが，実際に使えるCPU・GPU/nodeの数には限りがある．そこで，一般に複数人で共有されるような大規模計算機には，queue systemという計算シミュレーションの実行順序を管理するようなスケジュール機能が導入されている．
物性研 systemB では，queue systemの一つである [**Slurm Workload Manager**](https://mdcl.issp.u-tokyo.ac.jp/scc/system/systembinfo/software) が導入されており，systemBの利用者はslurmに計算シミュレーションの予約を投げることで，計算シミュレーションを大勢で効率良く実行している．詳細は以下の[website](http://www.dna-ltd.co.jp/slurm_doc/20.02.04/overview.html)を参照．

## ✅  重要なslurm commandを以下に列挙する：

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

## 🔰 具体的なjob scriptの書き方

slurm systemへのjob scriptの環境変数の定義をいちから覚えて自分で書くのは，
あまり効率的ではないので以下に実際のスクリプトファイルを示す．本スクリプトを参考に，自分なりにスクリプトファイルを編集していくのが良い．

``` sh
#!/bin/sh

#SBATCH -p F4cpu # 使用するクラス選択
#SBATCH -N 4    # 使用するNode数
#SBATCH -n 16   # 使用するMPIプロセス数の合計；　4 (nodes) x 4 (MPI processes per node)
#SBATCH -c 32   # 32 threads per MPI process
#SBATCH -t 00:30:00 # 最大実行時間

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

[🏠 Home](systemb.md)
