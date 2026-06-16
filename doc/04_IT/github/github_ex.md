---
title: "github_ex.md"
author: "Takeru Nakashima"
date: "2026-06-16"
excerpt: <excerpt or description on this script>
collection: portfolio

# --- 🌐 Language & Document Settings (Pandoc / LuaLaTeX) ---
# [Default: English style] ---
documentclass: article
classoption: a4paper

# [Alternative: Japanese style] If writing in Japanese, comment out 2 lines above and uncomment below:
# documentclass: ltjsarticle
# lang: ja
# mainfont: "Harano Aji Mincho"  # Or your preferred Japanese font (e.g., IPAexMincho)
# sansfont: "Harano Aji Gothic"  # Or your preferred Japanese Gothic font

# [Conversion from markdown to text style]
# pandoc %.md -o %.tex -s --pdf-engine=lualatex
---

# Main Text
以下にgithubを利用する際に，覚えておくと便利なコマンドを簡単に記述する．

## git clone
リポジトリをクローンするコマンド．

```bash
git clone <repository_url>
```
## git add
変更をステージングエリアに追加するコマンド．

```bash
git add <file_name>
```
## git commit
変更をコミットするコマンド．

```bash
git commit -m "Commit message"
```
## git push
リモートリポジトリに変更をプッシュするコマンド．

```bash
git push origin <branch_name>
```
## git pull
リモートリポジトリから変更をプルするコマンド．

```bash
git pull origin <branch_name>
```
## git status
現在のリポジトリの状態を確認するコマンド．

```bash
git status
```
## git log
コミット履歴を表示するコマンド．

```bash
git log
```
## git branch
ブランチを管理するコマンド．

```bash
git branch <branch_name>  # ブランチの作成
git branch -d <branch_name>  # ブランチの削除
```

## git checkout
ブランチを切り替えるコマンド．

```bash
git checkout <branch_name>
```
## git merge
ブランチをマージするコマンド．

```bash
git merge <branch_name>
```
## git stash
変更を一時的に保存するコマンド．

```bash
git stash
```
## git stash pop
保存した変更を復元するコマンド．

```bash
git stash pop
```
## git remote
リモートリポジトリを管理するコマンド．

```bash
git remote add <remote_name> <repository_url>  # リモートリポジトリの追加
git remote remove <remote_name>  # リモートリポジトリの削除
```
## git fetch
リモートリポジトリから最新の変更を取得するコマンド．

```bash
git fetch origin
```
## git reset
変更をリセットするコマンド．

```bash
git reset --hard HEAD  # 変更をすべてリセット
git reset --soft HEAD~1  # 最後のコミットをリセット（変更は残す）
```
## git revert
コミットを元に戻すコマンド．

```bash
git revert <commit_hash>
```
## git tag
タグを管理するコマンド．

```bash
git tag <tag_name>  # タグの作成
git tag -d <tag_name>  # タグの削除
```
## git diff
変更点を比較するコマンド．

```bash
git diff  # ワーキングツリーとステージングエリアの差分
git diff --staged  # ステージングエリアと最後のコミットの差分
git diff <commit_hash1> <commit_hash2>  # 2つのコミットの差分
git diff <commit_hash >  # 特定のコミットとワーキングツリーの差分, commit hash はgit logで確認できるコミットのハッシュ値
```
## git log --oneline
コミット履歴を簡潔に表示するコマンド．

```bash
git log --oneline
```
## git log --graph
コミット履歴をグラフ形式で表示するコマンド．

```bash
git log --graph --oneline
```
