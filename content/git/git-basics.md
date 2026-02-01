---
title: "Git Basics 101"
weight: 1
---

## Table of Contents
  - [1. Setup & Init](#1-setup-init)
  - [2. Stage & Snapshot](#2-stage-snapshot)
  - [3. Branch & Merge](#3-branch-merge)
  - [4. Share & Update](#4-share-update)
  - [5. Tracking Path Changes](#5-tracking-path-changes)
  - [6. Temporary Commits (Stash)](#6-temporary-commits-stash)
  - [7. Rewrite History](#7-rewrite-history)
  - [8. Inspect & Compare](#8-inspect-compare)
  - [9. Ignoring Patterns](#9-ignoring-patterns)


---

### 1. **Setup & Init** {#1-setup-init}

* `git config --global user.name "Your Name"`
* `git config --global user.email "you@example.com"`
* `git init` → create a new repo in a folder
* `git clone [url]` → practice cloning an existing repo

**Practice:** Create a test folder, initialize a repo, and check configs.



---

### 2. **Stage & Snapshot** {#2-stage-snapshot}

* `git status` → check what’s changed
* `git add file.txt` → stage changes
* `git reset file.txt` → unstage
* `git diff` → see unstaged changes
* `git diff --staged` → see staged changes
* `git commit -m "message"` → save snapshot

 **Practice:** Make changes to a file, add & remove from staging, then commit.



---

### 3. **Branch & Merge** {#3-branch-merge}

* `git branch` → list branches
* `git branch feature` → create a branch
* `git checkout feature` → switch to it
* `git merge feature` → merge back to main
* `git log` → check history

**Practice:** Create a feature branch, make a commit, merge it back.



---

### 4. **Share & Update** {#4-share-update}

* `git remote add origin [url]` → link remote
* `git fetch origin` → pull down changes
* `git merge origin/main` → merge remote into local
* `git push origin main` → upload changes
* `git pull` → fetch + merge

**Practice:** Make a GitHub repo, push your commits, pull from it.



---

### 5. **Tracking Path Changes** {#5-tracking-path-changes}

* `git rm file.txt` → remove tracked file
* `git mv old.txt new.txt` → rename file
* `git log --stat -M` → see moved files in history

**Practice:** Rename a file, delete another, commit both.



---

### 6. **Temporary Commits (Stash)** {#6-temporary-commits-stash}

* `git stash` → save work-in-progress
* `git stash list` → see stashes
* `git stash pop` → reapply stash
* `git stash drop` → discard stash

**Practice:** Modify a file, stash it, switch branch, come back, pop it.



---

### 7. **Rewrite History** {#7-rewrite-history}

* `git rebase branch` → replay commits on top
* `git reset --hard commitID` → reset to earlier commit

**Practice:** Make a few commits, reset to an older commit, then rebase.



---

### 8. **Inspect & Compare** {#8-inspect-compare}

* `git log` → see history
* `git log branchB..branchA` → commits in A not in B
* `git log --follow file.txt` → file history
* `git diff branchB...branchA` → difference between branches
* `git show commitID` → details of a commit

**Practice:** Explore history of your repo with these commands.



---

### 9. **Ignoring Patterns** {#9-ignoring-patterns}

* Create a `.gitignore` with things like:

  ```
  *.log
  temp/
  ```
* `git config --global core.excludesfile ~/.gitignore_global`

**Practice:** Add a `.gitignore` to your repo, commit it, and test ignored files.



---
