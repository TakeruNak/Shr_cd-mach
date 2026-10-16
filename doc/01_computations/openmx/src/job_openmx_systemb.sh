#!/bin/sh
# ---------------------------------------------------------------
# 物性研 SystemB (ohtaka) 向け OpenMX ジョブスクリプト
#   投入:   sbatch job_openmx_systemb.sh
#   確認:   squeue
#   取消:   scancel <jobID>
# ---------------------------------------------------------------

#SBATCH -p i8cpu      # 使用するクラス
#SBATCH -N 4          # ノード数
#SBATCH -n 16         # MPI プロセス数の合計 (4 nodes x 4 processes)
#SBATCH -c 32         # 1 MPI プロセスあたりの OpenMP スレッド数
#SBATCH -t 00:30:00   # 最大実行時間

set -e

# OpenMX の環境設定（PATH / ライブラリ）を読み込む
source /home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmxvars.sh
module list

# 入力ファイル中の DATA.PATH には下記を指定しておくこと:
#   DATA.PATH /home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5/openmx/openmx-3.9.9-1/DFT_DATA19

# -n (MPI) x --cpus-per-task (OpenMP) = 128 x ノード数 となるよう揃える
srun -n 16 --cpus-per-task=32 openmx ./c2h4_neb.dat -nt 32
