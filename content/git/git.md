---
title: "Git Basics and Workflow"
date: 2026-02-01
draft: false
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
- [0. Mental model (read this once)](#0-mental-model-read-this-once)
- [1. Check what your repo is using (ALWAYS first)](#1-check-what-your-repo-is-using-always-first)
  - [If you see:](#if-you-see)
  - [If you see:](#if-you-see)
- [2. Generate an SSH key (one-time setup)](#2-generate-an-ssh-key-one-time-setup)
- [3. Add SSH key to GitHub (one-time)](#3-add-ssh-key-to-github-one-time)
- [4. Test SSH connection (VERY IMPORTANT)](#4-test-ssh-connection-very-important)
  - [Expected output:](#expected-output)
- [5. Convert an existing repo from HTTPS → SSH](#5-convert-an-existing-repo-from-https-ssh)
- [6. Push (what should happen now)](#6-push-what-should-happen-now)
- [7. Avoid retyping passphrase (per session)](#7-avoid-retyping-passphrase-per-session)
- [8. Make SSH automatic forever (recommended)](#8-make-ssh-automatic-forever-recommended)
- [9. Common failure patterns (recognize instantly)](#9-common-failure-patterns-recognize-instantly)
  - [<span style="color: red; font-size: 0.8em;">✗</span> “GitHub asks for username/password”](#github-asks-for-usernamepassword)
  - [<span style="color: red; font-size: 0.8em;">✗</span> “Permission denied (publickey)”](#permission-denied-publickey)
  - [<span style="color: red; font-size: 0.8em;">✗</span> “Works on one machine, not another”](#works-on-one-machine-not-another)
- [10. Golden rules (tattoo these)](#10-golden-rules-tattoo-these)
- [Ultra-short checklist (panic mode)](#ultra-short-checklist-panic-mode)
- [Why GitHub killed passwords (the *actual* reasons)](#why-github-killed-passwords-the-actual-reasons)
  - [1. Passwords were a security disaster](#1-passwords-were-a-security-disaster)
  - [2. Git has no real way to do 2FA](#2-git-has-no-real-way-to-do-2fa)
  - [3. Personal Access Tokens are scoped](#3-personal-access-tokens-are-scoped)
  - [4. Open-source supply chain attacks scared everyone](#4-open-source-supply-chain-attacks-scared-everyone)
  - [5. SSH is cryptographically better (and older than GitHub)](#5-ssh-is-cryptographically-better-and-older-than-github)
- [So what GitHub actually did](#so-what-github-actually-did)
- [TL;DR (memorize this)](#tldr-memorize-this)
- [The quiet truth](#the-quiet-truth)
- [0. What GPG is actually for (mental model)](#0-what-gpg-is-actually-for-mental-model)
- [1. Check if GPG is installed](#1-check-if-gpg-is-installed)
- [2. Generate a GPG key (this is where passphrase comes in)](#2-generate-a-gpg-key-this-is-where-passphrase-comes-in)
  - [Choose these options (recommended)](#choose-these-options-recommended)
  - [🔐 Passphrase prompt (IMPORTANT)](#passphrase-prompt-important)
- [3. Verify your key exists](#3-verify-your-key-exists)
- [4. Export your public key (for GitHub)](#4-export-your-public-key-for-github)
- [5. Tell Git to use GPG (sign commits)](#5-tell-git-to-use-gpg-sign-commits)
- [6. Make a signed commit (test)](#6-make-a-signed-commit-test)
- [7. Stop passphrase popping up every time (recommended)](#7-stop-passphrase-popping-up-every-time-recommended)
  - [Enable caching](#enable-caching)
- [8. Common mistakes (avoid these)](#8-common-mistakes-avoid-these)
- [9. Backup (DO THIS ONCE)](#9-backup-do-this-once)
- [🗝️ TL;DR checklist](#tldr-checklist)
- [One-line rule (memorize this)](#one-line-rule-memorize-this)
- [💡 Mental model](#mental-model)
- [🔐 SSH — what it’s actually for](#ssh-what-its-actually-for)
  - [Primary uses](#primary-uses)
  - [What SSH does](#what-ssh-does)
  - [What SSH does NOT do](#what-ssh-does-not-do)
  - [Example](#example)
- [🔏 GPG — what it’s actually for](#gpg-what-its-actually-for)
  - [Primary uses](#primary-uses)
  - [What GPG does](#what-gpg-does)
  - [What GPG does NOT do](#what-gpg-does-not-do)
  - [Example](#example)
- [⚔️ Side-by-side (important)](#side-by-side-important)
- [🧩 Real-world Git workflow (best practice)](#real-world-git-workflow-best-practice)
- [🚨 Why GitHub doesn’t allow GPG instead of SSH](#why-github-doesnt-allow-gpg-instead-of-ssh)
- [💡 Trust model difference (this is key)](#trust-model-difference-this-is-key)
  - [SSH trust](#ssh-trust)
  - [GPG trust](#gpg-trust)
- [🎯 When to use which (cheat sheet)](#when-to-use-which-cheat-sheet)
  - [Use SSH when:](#use-ssh-when)
  - [Use GPG when:](#use-gpg-when)
- [🔥 Advanced (optional but cool)](#advanced-optional-but-cool)
- [TL;DR (tattoo this)](#tldr-tattoo-this)
- [1. They don’t fit our “password brain”](#1-they-dont-fit-our-password-brain)
- [2. You never actually send the secret](#2-you-never-actually-send-the-secret)
- [3. Passphrases protect against device theft](#3-passphrases-protect-against-device-theft)
- [4. SSH agents feel magical (and scary)](#4-ssh-agents-feel-magical-and-scary)
- [5. You can revoke without changing your life](#5-you-can-revoke-without-changing-your-life)
- [6. Automation made SSH unavoidable](#6-automation-made-ssh-unavoidable)
- [7. Why it *feels* worse on day one](#7-why-it-feels-worse-on-day-one)
- [💡 The quiet truth](#the-quiet-truth)
- [TL;DR (stick this)](#tldr-stick-this)
- [1. Git was designed for a *hostile, disconnected world*](#1-git-was-designed-for-a-hostile-disconnected-world)
- [2. Git does NOT authenticate users — transports do](#2-git-does-not-authenticate-users-transports-do)
- [3. Git’s data model predates “accounts”](#3-gits-data-model-predates-accounts)
- [4. Changing auth would break the ecosystem](#4-changing-auth-would-break-the-ecosystem)
- [5. Git optimizes for *verification*, not *permission*](#5-git-optimizes-for-verification-not-permission)
- [6. Central platforms had to adapt to Git — not vice versa](#6-central-platforms-had-to-adapt-to-git-not-vice-versa)
- [7. Why this feels painful today](#7-why-this-feels-painful-today)
- [💡 The uncomfortable truth](#the-uncomfortable-truth)
- [TL;DR (burn this in)](#tldr-burn-this-in)
  - [One-liner to remember](#one-liner-to-remember)
- [1. Maintainer account takeover (most common)](#1-maintainer-account-takeover-most-common)
  - [How it happens](#how-it-happens)
  - [Why this works](#why-this-works)
- [2. Dependency confusion (nasty & clever)](#2-dependency-confusion-nasty-clever)
  - [How it works](#how-it-works)
- [3. Typosquatting (boring but effective)](#3-typosquatting-boring-but-effective)
- [4. Malicious install scripts (very common)](#4-malicious-install-scripts-very-common)
- [5. Compromised CI/CD pipelines](#5-compromised-cicd-pipelines)
  - [Attack path](#attack-path)
- [6. Dormant backdoors (the scariest)](#6-dormant-backdoors-the-scariest)
- [7. Abandoned but popular packages](#7-abandoned-but-popular-packages)
- [💡 Why this keeps working](#why-this-keeps-working)
- [🔐 How defenses actually work (practical)](#how-defenses-actually-work-practical)
  - [1. Signed commits & tags (GPG)](#1-signed-commits-tags-gpg)
  - [2. Scoped tokens](#2-scoped-tokens)
  - [3. Dependency pinning](#3-dependency-pinning)
  - [4. Minimal install scripts](#4-minimal-install-scripts)
  - [5. Reduce dependency count](#5-reduce-dependency-count)
- [💡 The uncomfortable truth](#the-uncomfortable-truth)
- [TL;DR](#tldr)
- [Mental model (read this once)](#mental-model-read-this-once)
- [1. What you need before anything works](#1-what-you-need-before-anything-works)
- [2. Get someone’s public key](#2-get-someones-public-key)
  - [Option A: They send it to you](#option-a-they-send-it-to-you)
  - [Option B: From a keyserver](#option-b-from-a-keyserver)
- [3. Verify the key (VERY important)](#3-verify-the-key-very-important)
- [4. Encrypt + sign an email (core command)](#4-encrypt-sign-an-email-core-command)
- [5. Send it via email (how people actually do it)](#5-send-it-via-email-how-people-actually-do-it)
  - [Option A: Attach the `.gpg` file](#option-a-attach-the-gpg-file)
  - [Option B: Inline (ASCII armor)](#option-b-inline-ascii-armor)
- [6. What the recipient does](#6-what-the-recipient-does)
- [7. Reading encrypted email you receive](#7-reading-encrypted-email-you-receive)
- [8. Using GPG with real email clients (recommended)](#8-using-gpg-with-real-email-clients-recommended)
  - [Thunderbird (best support)](#thunderbird-best-support)
  - [CLI-only workflow (minimalist)](#cli-only-workflow-minimalist)
- [9. Common mistakes (learn from others’ pain)](#9-common-mistakes-learn-from-others-pain)
- [🔍 Important limitation (know this)](#important-limitation-know-this)
- [🔐 Best practices (real-world)](#best-practices-real-world)
- [TL;DR (workflow)](#tldr-workflow)
- [One-liner to remember](#one-liner-to-remember)
- [What a YubiKey actually does (not what people think)](#what-a-yubikey-actually-does-not-what-people-think)
- [Why this matters (and why software keys are weak)](#why-this-matters-and-why-software-keys-are-weak)
- [What you actually need](#what-you-actually-need)
- [Install the required junk (once)](#install-the-required-junk-once)
- [Reset the OpenPGP app (clean slate)](#reset-the-openpgp-app-clean-slate)
- [Generate keys on the hardware, not on disk](#generate-keys-on-the-hardware-not-on-disk)
- [Verify the key is actually hardware-backed](#verify-the-key-is-actually-hardware-backed)
- [Force touch confirmation (non-negotiable)](#force-touch-confirmation-non-negotiable)
- [Use it with Git (the only reason most people care)](#use-it-with-git-the-only-reason-most-people-care)
- [Add the public key to GitHub](#add-the-public-key-to-github)
- [Backups (because hardware breaks)](#backups-because-hardware-breaks)
- [What this setup protects you from](#what-this-setup-protects-you-from)
- [The takeaway](#the-takeaway)


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

some

```bash

md)
    if command -v lowdown >/dev/null 2>&1; then
        ( lowdown --parse-no-intraemph "$file" -Tms \
            | groff -mpdfmark -ms -kept -T pdf > "$base.pdf"
        )
    elif command -v groffdown >/dev/null 2>&1; then
        ( groffdown -i "$file" \
            | groff -T pdf > "$base.pdf"
        )
    else
        pandoc -t ms --highlight-style="kate" -s -o "$base.pdf" "$file"
    fi
    ;;
```


---

#  📘 GitHub Authentication Tutorial (SSH vs HTTPS)

> **Goal:**
> Make Git use **SSH keys** so you:
>
> * Don’t enter username/password every push
> * Use your **SSH key passphrase**
> * Never deal with GitHub PAT nonsense again

---

## 0. Mental model (read this once) {#0-mental-model-read-this-once}

Git has **two ways** to talk to GitHub:

| Method | What it asks     | Uses SSH key? |
| ------ | ---------------- | ------------- |
| HTTPS  | username + token | <span style="color: red; font-size: 0.8em;">✗</span> No          |
| SSH    | key + passphrase | <span style="color: green;">✓</span> Yes         |

➜ If Git asks for **username/password**,
➜ you are **NOT using SSH**.

---

## 1. Check what your repo is using (ALWAYS first) {#1-check-what-your-repo-is-using-always-first}

Inside the repo:

```bash
git remote -v
```

### If you see: {#if-you-see}

```text
https://github.com/username/repo.git
```

<span style="color: red; font-size: 0.8em;">✗</span> HTTPS (will ask for username/password)

### If you see: {#if-you-see}

```text
git@github.com:username/repo.git
```

<span style="color: green;">✓</span> SSH (will ask for passphrase)

---

## 2. Generate an SSH key (one-time setup) {#2-generate-an-ssh-key-one-time-setup}

Check first:

```bash
ls ~/.ssh
```

If you already see:

```
id_ed25519
id_ed25519.pub
```

➜ skip this step.

Otherwise:

```bash
ssh-keygen -t ed25519
```

* Press Enter for default location
* Set a **passphrase** (important)

---

## 3. Add SSH key to GitHub (one-time) {#3-add-ssh-key-to-github-one-time}

Copy your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Then on GitHub:

```
Settings → SSH and GPG keys → New SSH key
```

Paste → Save.

---

## 4. Test SSH connection (VERY IMPORTANT) {#4-test-ssh-connection-very-important}

```bash
ssh -T git@github.com
```

### Expected output: {#expected-output}

```text
Hi <username>! You've successfully authenticated...
```

If this fails → stop here and fix before continuing.

---

## 5. Convert an existing repo from HTTPS → SSH {#5-convert-an-existing-repo-from-https-ssh}

Inside the repo:

```bash
git remote set-url origin git@github.com:USERNAME/REPO.git
```

Example (yours):

```bash
git remote set-url origin git@github.com:notxkcd/sdet-prep-site.git
```

Verify:

```bash
git remote -v
```

---

## 6. Push (what should happen now) {#6-push-what-should-happen-now}

```bash
git push
```

<span style="color: green;">✓</span> Git asks for **SSH key passphrase**
<span style="color: red; font-size: 0.8em;">✗</span> No username
<span style="color: red; font-size: 0.8em;">✗</span> No password

That’s the **correct behavior**.

---

## 7. Avoid retyping passphrase (per session) {#7-avoid-retyping-passphrase-per-session}

Load key into agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

You enter passphrase **once per login**.

---

## 8. Make SSH automatic forever (recommended) {#8-make-ssh-automatic-forever-recommended}

Create/edit:

```bash
nano ~/.ssh/config
```

Add:

```ssh
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  AddKeysToAgent yes
```

Now Git just works™.

---

## 9. Common failure patterns (recognize instantly) {#9-common-failure-patterns-recognize-instantly}

### <span style="color: red; font-size: 0.8em;">✗</span> “GitHub asks for username/password” {#github-asks-for-usernamepassword}

→ Repo is HTTPS
<span style="color: green;">✓</span> Fix: `git remote set-url origin git@github.com:...`

---

### <span style="color: red; font-size: 0.8em;">✗</span> “Permission denied (publickey)” {#permission-denied-publickey}

→ SSH key not added to GitHub
<span style="color: green;">✓</span> Fix: Step 3

---

### <span style="color: red; font-size: 0.8em;">✗</span> “Works on one machine, not another” {#works-on-one-machine-not-another}

→ SSH key exists only on first machine
<span style="color: green;">✓</span> Fix: Generate key again on new machine

---

## 10. Golden rules (tattoo these) {#10-golden-rules-tattoo-these}

* 🗝️ **SSH is per machine**, not per GitHub account
* 🌐 Each cloned repo has its **own remote URL**
* 💡 Git NEVER auto-switches HTTPS → SSH
* 🔬 `git remote -v` tells the truth

---

## Ultra-short checklist (panic mode) {#ultra-short-checklist-panic-mode}

```bash
git remote -v
ssh -T git@github.com
git remote set-url origin git@github.com:user/repo.git
git push
```

---


## Why GitHub killed passwords (the *actual* reasons) {#why-github-killed-passwords-the-actual-reasons}

### 1. Passwords were a security disaster {#1-passwords-were-a-security-disaster}

People reused passwords **everywhere**.

When one random site leaked:

* Attackers tried the same password on GitHub
* Repos got hijacked
* Malware got injected into open-source projects

This is called **credential stuffing** — and it worked *way too well*.

---

### 2. Git has no real way to do 2FA {#2-git-has-no-real-way-to-do-2fa}

Git (the protocol) was designed **before** modern auth.

Over HTTPS:

* Git can only send `username + secret`
* No browser
* No OTP prompt
* No hardware key

So if passwords stayed:

> **2FA would be meaningless**

---

### 3. Personal Access Tokens are scoped {#3-personal-access-tokens-are-scoped}

Passwords give **full account access**.

PATs can be:

* Read-only
* Repo-specific
* Time-limited
* Revoked instantly

If a token leaks → **blast radius is tiny**.

Passwords? Total account takeover.

---

### 4. Open-source supply chain attacks scared everyone {#4-open-source-supply-chain-attacks-scared-everyone}

One compromised maintainer =

* Backdoored libraries
* Millions of users affected

GitHub decided:

> “Passwords are not acceptable risk anymore.”

This wasn’t theoretical — it already happened.

---

### 5. SSH is cryptographically better (and older than GitHub) {#5-ssh-is-cryptographically-better-and-older-than-github}

SSH:

* Never sends secrets over the wire
* Uses challenge–response
* Private key never leaves your machine

Even if GitHub is breached:

* Your private key is still safe

---

## So what GitHub actually did {#so-what-github-actually-did}

In 2021:

* <span style="color: red; font-size: 0.8em;">✗</span> Disabled account passwords for Git over HTTPS
* <span style="color: green;">✓</span> Forced **PATs or SSH**
* <span style="color: red; font-size: 0.8em;">✗</span> Broke old tutorials (sad but necessary)

---

## TL;DR (memorize this) {#tldr-memorize-this}

| Method   | Security   | Why               |
| -------- | ---------- | ----------------- |
| Password | <span style="color: red; font-size: 0.8em;">✗</span> Terrible | Reused, phishable |
| PAT      | ⚠️ Better  | Scoped, revocable |
| SSH      | <span style="color: green;">✓</span> Best     | Keys never sent   |

---

## The quiet truth {#the-quiet-truth}

> GitHub didn’t *kill* passwords.
> Passwords killed themselves.

---

# 🔐 GPG: Generate Keys + Use Passphrase (Practical Guide)

## 0. What GPG is actually for (mental model) {#0-what-gpg-is-actually-for-mental-model}

GPG lets you:

* 🔏 **Sign** things (prove it’s you)
* 🔒 **Encrypt** things (only intended person can read)

For devs, the **#1 use** is:
➜ **Signing Git commits & tags**

---

## 1. Check if GPG is installed {#1-check-if-gpg-is-installed}

```bash
gpg --version
```

If not installed:

**Arch / Artix**

```bash
sudo pacman -S gnupg
```

**Ubuntu / Debian**

```bash
sudo apt install gnupg
```

---

## 2. Generate a GPG key (this is where passphrase comes in) {#2-generate-a-gpg-key-this-is-where-passphrase-comes-in}

Run:

```bash
gpg --full-generate-key
```

### Choose these options (recommended) {#choose-these-options-recommended}

```
Please select what kind of key you want:
(1) RSA and RSA   ← choose this

What keysize?
4096             ← choose 4096

Key is valid for?
0                ← never expires (or set 1y if you want)

Real name:
Your Name

Email address:
you@email.com
```

### 🔐 Passphrase prompt (IMPORTANT) {#passphrase-prompt-important}

* This encrypts your **private key**
* Use a **long sentence**, not a short password

Example:

```
correct horse battery staple but longer
```

You’ll type it twice.

<span style="color: green;">✓</span> This is **normal and good**.

---

## 3. Verify your key exists {#3-verify-your-key-exists}

```bash
gpg --list-secret-keys --keyid-format=long
```

Example output:

```
sec   rsa4096/ABCD1234EFGH5678 2026-02-01
```

➜ Copy the **key ID** (`ABCD1234EFGH5678`)

---

## 4. Export your public key (for GitHub) {#4-export-your-public-key-for-github}

```bash
gpg --armor --export ABCD1234EFGH5678
```

Copy everything:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
...
-----END PGP PUBLIC KEY BLOCK-----
```

GitHub → **Settings → SSH and GPG keys → New GPG key**

---

## 5. Tell Git to use GPG (sign commits) {#5-tell-git-to-use-gpg-sign-commits}

```bash
git config --global user.signingkey ABCD1234EFGH5678
git config --global commit.gpgsign true
git config --global gpg.program gpg
```

Set your identity (must match GPG email):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
```

---

## 6. Make a signed commit (test) {#6-make-a-signed-commit-test}

```bash
git commit -m "test signed commit"
```

🔐 GPG will ask for your **passphrase**
That’s expected.

Verify:

```bash
git log --show-signature
```

You should see:

```
Good signature from "Your Name"
```

---

## 7. Stop passphrase popping up every time (recommended) {#7-stop-passphrase-popping-up-every-time-recommended}

Use **gpg-agent** (already included).

### Enable caching {#enable-caching}

```bash
echo "default-cache-ttl 3600" >> ~/.gnupg/gpg-agent.conf
echo "max-cache-ttl 86400" >> ~/.gnupg/gpg-agent.conf
```

Reload agent:

```bash
gpgconf --kill gpg-agent
```

Now:

* You enter passphrase **once**
* Cached for session/day

---

## 8. Common mistakes (avoid these) {#8-common-mistakes-avoid-these}

<span style="color: red; font-size: 0.8em;">✗</span> Using a short passphrase
<span style="color: red; font-size: 0.8em;">✗</span> Email mismatch between Git and GPG
<span style="color: red; font-size: 0.8em;">✗</span> Forgetting to add public key to GitHub
<span style="color: red; font-size: 0.8em;">✗</span> Deleting `~/.gnupg` (this deletes your identity)

---

## 9. Backup (DO THIS ONCE) {#9-backup-do-this-once}

Backup private key:

```bash
gpg --export-secret-keys --armor ABCD1234EFGH5678 > gpg-private-backup.asc
```

Store it **offline** (USB, encrypted drive).

---

## 🗝️ TL;DR checklist {#tldr-checklist}

```bash
gpg --full-generate-key
gpg --list-secret-keys
gpg --armor --export KEYID
git config --global commit.gpgsign true
```

---

# 🗝️ GPG vs SSH — When to Use Which (No BS)

## One-line rule (memorize this) {#one-line-rule-memorize-this}

> **SSH = authenticate to servers**
> **GPG = prove authorship & trust**

They solve **different problems**.

---

## 💡 Mental model {#mental-model}

| Tool | Question it answers                       |
| ---- | ----------------------------------------- |
| SSH  | “Are *you* allowed to connect right now?” |
| GPG  | “Did *you* really create this thing?”     |

---

## 🔐 SSH — what it’s actually for {#ssh-what-its-actually-for}

### Primary uses {#primary-uses}

* `git push / pull`
* `ssh user@server`
* Deploying, tunneling, port forwarding

### What SSH does {#what-ssh-does}

* Proves you own a **private key**
* Grants **access**
* Session-based authentication

### What SSH does **NOT** do {#what-ssh-does-not-do}

* <span style="color: red; font-size: 0.8em;">✗</span> Prove authorship later
* <span style="color: red; font-size: 0.8em;">✗</span> Leave permanent identity proof
* <span style="color: red; font-size: 0.8em;">✗</span> Survive copy/paste of content

### Example {#example}

```bash
git push
```

GitHub says:

> “Yes, this key is allowed to push.”

Later?

> “No idea who authored those commits.”

---

## 🔏 GPG — what it’s actually for {#gpg-what-its-actually-for}

### Primary uses {#primary-uses}

* Signing Git commits & tags
* Verifying releases
* Encrypting messages/files

### What GPG does {#what-gpg-does}

* Attaches a **cryptographic signature**
* Verifiable **forever**
* Survives mirrors, forks, copies

### What GPG does **NOT** do {#what-gpg-does-not-do}

* <span style="color: red; font-size: 0.8em;">✗</span> Authenticate network sessions
* <span style="color: red; font-size: 0.8em;">✗</span> Replace SSH for Git access

### Example {#example}

```bash
git commit -S -m "Fix race condition"
```

Anyone can later verify:

> “This commit was signed by Mohammed Shahid.”

---

## ⚔️ Side-by-side (important) {#side-by-side-important}

| Feature       | SSH          | GPG              |
| ------------- | ------------ | ---------------- |
| Purpose       | Access       | Identity         |
| Time          | Live session | Permanent        |
| Used for      | Push / login | Signing / trust  |
| Revocation    | Remove key   | Revoke signature |
| GitHub badge  | <span style="color: red; font-size: 0.8em;">✗</span>            | <span style="color: green;">✓</span> “Verified”     |
| Survives fork | <span style="color: red; font-size: 0.8em;">✗</span>            | <span style="color: green;">✓</span>                |

---

## 🧩 Real-world Git workflow (best practice) {#real-world-git-workflow-best-practice}

<span style="color: green;">✓</span> **SSH**

```bash
git push
```

<span style="color: green;">✓</span> **GPG**

```bash
git commit -S
```

You should use **both**.

---

## 🚨 Why GitHub doesn’t allow GPG instead of SSH {#why-github-doesnt-allow-gpg-instead-of-ssh}

Because:

* GPG is **slow & interactive**
* Not designed for live sessions
* Bad UX for frequent operations

SSH is optimized for:

* Fast handshakes
* Repeated connections
* Agent forwarding

---

## 💡 Trust model difference (this is key) {#trust-model-difference-this-is-key}

### SSH trust {#ssh-trust}

> “I trust this machine *right now*.”

### GPG trust {#gpg-trust}

> “I trust this identity *forever*.”

---

## 🎯 When to use which (cheat sheet) {#when-to-use-which-cheat-sheet}

### Use SSH when: {#use-ssh-when}

* Pushing/pulling code
* Logging into servers
* CI/CD auth
* Automation

### Use GPG when: {#use-gpg-when}

* Signing commits/tags
* Publishing releases
* Proving authorship
* Open-source work

---

## 🔥 Advanced (optional but cool) {#advanced-optional-but-cool}

* SSH keys can be **ephemeral**
* GPG keys should be **long-lived**
* Hardware keys (YubiKey) can do **both**

---

## TL;DR (tattoo this) {#tldr-tattoo-this}

> **SSH gets you in.**
> **GPG proves it was you.**

---

# 🔐 Why SSH keys feel annoying — but are safer

## 1. They don’t fit our “password brain” {#1-they-dont-fit-our-password-brain}

Passwords are:

* Short
* Memorable
* Reusable (bad, but familiar)

SSH keys are:

* Long
* Random
* Non-memorizable

Your brain hates that. Security loves it.

> Friction ≠ bad UX here.
> Friction = attack resistance.

---

## 2. You never actually send the secret {#2-you-never-actually-send-the-secret}

With passwords:

* You **send the secret**
* Server stores something derived from it
* Phishing works

With SSH:

* The **private key never leaves your machine**
* Server only sees proof you have it

Even if GitHub is breached:

* Your key is still safe
* Attacker gains nothing useful

This alone is huge.

---

## 3. Passphrases protect against device theft {#3-passphrases-protect-against-device-theft}

Annoying part:

> “Why do I need a passphrase if I already have a key?”

Because:

* Laptop stolen → attacker gets the key file
* Passphrase encrypts the key **at rest**

So security layers:

1. File possession
2. Passphrase knowledge

Passwords only have **one layer**.

---

## 4. SSH agents feel magical (and scary) {#4-ssh-agents-feel-magical-and-scary}

Once loaded:

```bash
ssh-add ~/.ssh/id_ed25519
```

It just works™:

* No prompts
* Fast auth
* Invisible crypto

This *feels* wrong… until you realize:

* Key is in RAM only
* Cleared on logout
* Scoped per session

That’s **better than typing secrets repeatedly**.

---

## 5. You can revoke without changing your life {#5-you-can-revoke-without-changing-your-life}

SSH keys are:

* Per machine
* Per purpose

Lose a laptop?
→ Delete **one key** on GitHub.

Passwords?
→ Change password everywhere
→ Break scripts
→ Panic

---

## 6. Automation made SSH unavoidable {#6-automation-made-ssh-unavoidable}

CI/CD, servers, deploy bots:

* No human
* No keyboard
* No browser

Passwords don’t scale here.
SSH does.

That’s why industry standardized on it.

---

## 7. Why it *feels* worse on day one {#7-why-it-feels-worse-on-day-one}

| Annoyance         | Reason               |
| ----------------- | -------------------- |
| Key generation    | One-time setup       |
| Passphrase prompt | Protects stolen keys |
| Agent setup       | Prevents retyping    |
| Config files      | Explicit trust       |

After a week:

> You forget it exists.

After a year:

> You can’t imagine going back.

---

## 💡 The quiet truth {#the-quiet-truth}

> SSH feels annoying because it refuses to lie to you.

It makes:

* Trust explicit
* Secrets non-transferable
* Compromise localized

---

## TL;DR (stick this) {#tldr-stick-this}

* Passwords optimize **convenience**
* SSH optimizes **damage containment**
* Annoyance = intentional friction
* Once set up, SSH is **less annoying than passwords**

---

# 🗿 Why **Git still uses ancient auth**

Short version:

> **Git is old, conservative, offline-first, and allergic to central authority — by design.**

That combination locks auth in time.

---

## 1. Git was designed for a *hostile, disconnected world* {#1-git-was-designed-for-a-hostile-disconnected-world}

Git was created (2005) assuming:

* No central server
* No permanent network
* People emailing patches
* Mirrors everywhere

So Git’s core rule became:

> **Never depend on an online identity system**

Modern auth (OAuth, SSO, tokens):

* Requires live servers
* Requires a central authority
* Breaks offline workflows

Git refuses all of that.

---

## 2. Git does NOT authenticate users — transports do {#2-git-does-not-authenticate-users-transports-do}

This is the most important concept people miss.

Git itself:

* <span style="color: red; font-size: 0.8em;">✗</span> Does not know users
* <span style="color: red; font-size: 0.8em;">✗</span> Does not know accounts
* <span style="color: red; font-size: 0.8em;">✗</span> Does not know permissions

Git only says:

> “Here’s some data. Send it somewhere.”

Authentication is delegated to:

* SSH
* HTTPS
* File system permissions

So when you ask:

> “Why doesn’t Git support modern auth?”

Answer:

> **Because Git isn’t doing auth at all.**

---

## 3. Git’s data model predates “accounts” {#3-gits-data-model-predates-accounts}

In Git:

* Commits don’t belong to accounts
* Commits store **name + email only**
* Anyone can write anything

Example:

```text
Author: Linus Torvalds <linus@kernel.org>
```

That string is:

* Not verified
* Not authenticated
* Just text

Git trusts **cryptographic hashes**, not people.

---

## 4. Changing auth would break the ecosystem {#4-changing-auth-would-break-the-ecosystem}

Git is:

* In kernels
* In embedded systems
* In routers
* In air-gapped military networks
* In ancient enterprise tooling

Adding modern auth would mean:

* New dependencies
* New protocols
* New failure modes

Git’s philosophy:

> “If it works everywhere, don’t touch it.”

---

## 5. Git optimizes for *verification*, not *permission* {#5-git-optimizes-for-verification-not-permission}

This is subtle but huge.

Git answers:

* “Has this content changed?”
* “Is this object authentic?”
* “Does this hash match?”

Git does **not** answer:

* “Who is allowed to do this?”

That’s why:

* GPG exists (verify authorship)
* SSH exists (grant access)
* Git itself stays dumb

---

## 6. Central platforms had to adapt to Git — not vice versa {#6-central-platforms-had-to-adapt-to-git-not-vice-versa}

GitHub, GitLab, Bitbucket:

* Wrapped Git
* Added identity layers
* Added permissions
* Added web auth

But under the hood:

```text
Git + SSH
Git + HTTPS
```

Same old pipes.

They *cannot* replace Git’s auth model without forking Git itself — which would kill compatibility.

---

## 7. Why this feels painful today {#7-why-this-feels-painful-today}

Modern devs expect:

* Browser login
* Tokens auto-refreshing
* Fine-grained identity

Git expects:

* Files
* Keys
* Hashes
* Pipes

So the pain isn’t accidental — it’s a **mismatch of eras**.

---

## 💡 The uncomfortable truth {#the-uncomfortable-truth}

> Git is not a user system.
> Git is a content-addressed filesystem with opinions.

Everything else is layered on top.

---

## TL;DR (burn this in) {#tldr-burn-this-in}

* Git predates modern auth
* Git doesn’t do auth at all
* Auth lives in SSH / HTTPS
* Changing this would break the world
* Platforms adapted — Git did not

---

### One-liner to remember {#one-liner-to-remember}

> **Git trusts math, not identities.**

---

# 🔥 How supply-chain attacks actually happen

> **Supply-chain attack** =
> Compromising *trust*, not code.

Attackers don’t “hack users”.
They **become someone you already trust**.

---

## 1. Maintainer account takeover (most common) {#1-maintainer-account-takeover-most-common}

### How it happens {#how-it-happens}

* Maintainer reuses password
* Phished GitHub / npm credentials
* No 2FA
* Leaked token in CI logs

Attacker gets:

* Push access
* Publish rights

They add:

```js
if (process.env.CI) stealSecrets();
```

Nobody notices — tests still pass.

### Why this works {#why-this-works}

* Maintainers are overworked
* Old projects have weak security
* One person controls releases

---

## 2. Dependency confusion (nasty & clever) {#2-dependency-confusion-nasty-clever}

### How it works {#how-it-works}

Internal company uses:

```json
"dependencies": {
  "core-utils": "^1.2.0"
}
```

Attacker publishes:

```
core-utils@99.99.99
```

Public registry wins.

Boom:

* Malware installed in CI
* Secrets exfiltrated

No exploit. Just naming.

---

## 3. Typosquatting (boring but effective) {#3-typosquatting-boring-but-effective}

Examples:

* `react-dom` → `react_d0m`
* `urllib3` → `urllib33`

One character off.

People install it **by accident**.

Malware runs during install.

---

## 4. Malicious install scripts (very common) {#4-malicious-install-scripts-very-common}

In `package.json`:

```json
"scripts": {
  "postinstall": "node backdoor.js"
}
```

Runs:

* On developer machines
* In CI
* In Docker builds

No one audits install scripts.

---

## 5. Compromised CI/CD pipelines {#5-compromised-cicd-pipelines}

### Attack path {#attack-path}

* Attacker gets CI token
* Injects step:

  * Upload env vars
  * Modify artifacts
* Releases signed binary

Users trust:

* CI
* Signatures
* Checksums

Game over.

---

## 6. Dormant backdoors (the scariest) {#6-dormant-backdoors-the-scariest}

Attacker:

* Contributes harmless PR
* Waits months or years
* Later activates logic remotely

Example pattern:

```c
if (date > 2026 && host == "prod") activate();
```

Looks innocent.
Sleeps quietly.

---

## 7. Abandoned but popular packages {#7-abandoned-but-popular-packages}

Maintainer:

* Stops caring
* Leaves email unattended

Attacker:

* Requests maintainership
* Or hijacks account
* Or buys domain tied to email

Millions of installs. Zero resistance.

---

## 💡 Why this keeps working {#why-this-keeps-working}

Because ecosystems optimize for:

* Speed
* Convenience
* Automation

Attackers exploit:

* Trust inheritance
* Invisible transitive deps
* Human fatigue

---

## 🔐 How defenses actually work (practical) {#how-defenses-actually-work-practical}

### 1. Signed commits & tags (GPG) {#1-signed-commits-tags-gpg}

Ensures:

* Author authenticity
* No silent hijacks

### 2. Scoped tokens {#2-scoped-tokens}

* CI tokens limited
* No write unless needed

### 3. Dependency pinning {#3-dependency-pinning}

Lockfiles:

```text
package-lock.json
Cargo.lock
poetry.lock
```

Stops version surprises.

---

### 4. Minimal install scripts {#4-minimal-install-scripts}

Audit:

* `preinstall`
* `postinstall`

Block in CI if possible.

---

### 5. Reduce dependency count {#5-reduce-dependency-count}

Every dependency =

> One more maintainer you trust with your system.

---

## 💡 The uncomfortable truth {#the-uncomfortable-truth}

> Most supply-chain attacks don’t exploit bugs.
> They exploit **people and process**.

---

## TL;DR {#tldr}

* Attackers don’t break crypto
* They hijack trust
* Automation amplifies damage
* GPG + SSH + minimal deps = real defense

---

# 📧 GPG for Email Encryption (How It Actually Works)

## Mental model (read this once) {#mental-model-read-this-once}

Email encryption with GPG has **two separate actions**:

1. 🔒 **Encrypt** → only the recipient can read it
2. ✍️ **Sign** → proves *you* sent it

You usually do **both**.

---

## 1. What you need before anything works {#1-what-you-need-before-anything-works}

You already need:

* Your **GPG keypair** (you have this)
* The **recipient’s public key**

Without the recipient’s public key → encryption is impossible.

---

## 2. Get someone’s public key {#2-get-someones-public-key}

### Option A: They send it to you {#option-a-they-send-it-to-you}

File ends with:

```
.asc
```

Import it:

```bash
gpg --import alice-public.asc
```

---

### Option B: From a keyserver {#option-b-from-a-keyserver}

```bash
gpg --search-keys alice@email.com
```

Pick the correct key → confirm.

⚠️ **Always verify fingerprint out-of-band**
(chat, call, website).

---

## 3. Verify the key (VERY important) {#3-verify-the-key-very-important}

```bash
gpg --fingerprint alice@email.com
```

Compare with what Alice tells you.

If it matches → trust it.

---

## 4. Encrypt + sign an email (core command) {#4-encrypt-sign-an-email-core-command}

Create your message:

```bash
nano message.txt
```

Then:

```bash
gpg --encrypt --sign -r alice@email.com message.txt
```

This produces:

```
message.txt.gpg
```

What happened:

* 🔒 Encrypted with Alice’s public key
* ✍️ Signed with your private key

---

## 5. Send it via email (how people actually do it) {#5-send-it-via-email-how-people-actually-do-it}

### Option A: Attach the `.gpg` file {#option-a-attach-the-gpg-file}

Most common & simplest.

---

### Option B: Inline (ASCII armor) {#option-b-inline-ascii-armor}

Better for copy/paste:

```bash
gpg --encrypt --sign --armor -r alice@email.com message.txt
```

Output:

```
-----BEGIN PGP MESSAGE-----
...
-----END PGP MESSAGE-----
```

Paste **directly into email body**.

---

## 6. What the recipient does {#6-what-the-recipient-does}

Alice receives encrypted message and runs:

```bash
gpg --decrypt message.txt.gpg
```

Or just opens it in her mail client.

She sees:

* Decrypted content
* Signature verification:

```
Good signature from "Your Name"
```

---

## 7. Reading encrypted email you receive {#7-reading-encrypted-email-you-receive}

When someone encrypts mail to **you**:

```bash
gpg --decrypt mail.asc
```

GPG:

* Prompts for your **passphrase**
* Decrypts
* Verifies sender signature (if signed)

---

## 8. Using GPG with real email clients (recommended) {#8-using-gpg-with-real-email-clients-recommended}

### Thunderbird (best support) {#thunderbird-best-support}

* Install **Thunderbird**
* Enable **OpenPGP**
* Import your key
* Done

No plugins required anymore.

---

### CLI-only workflow (minimalist) {#cli-only-workflow-minimalist}

Use:

* `mutt`
* `neomutt`
* `aerc`

These work *beautifully* with GPG.

---

## 9. Common mistakes (learn from others’ pain) {#9-common-mistakes-learn-from-others-pain}

<span style="color: red; font-size: 0.8em;">✗</span> Encrypting without verifying fingerprint
<span style="color: red; font-size: 0.8em;">✗</span> Forgetting to include yourself as recipient
<span style="color: red; font-size: 0.8em;">✗</span> Losing private key (no recovery)
<span style="color: red; font-size: 0.8em;">✗</span> Thinking encryption hides metadata (it doesn’t)

---

## 🔍 Important limitation (know this) {#important-limitation-know-this}

GPG **does NOT encrypt**:

* Subject line
* Headers
* Sender / recipient
* Timestamps

Only the **message body + attachments**.

---

## 🔐 Best practices (real-world) {#best-practices-real-world}

* Always **sign + encrypt**
* Use long passphrases
* Backup your private key offline
* Revoke compromised keys immediately

---

## TL;DR (workflow) {#tldr-workflow}

```bash
# import recipient key
gpg --import alice.asc

# verify fingerprint
gpg --fingerprint alice@email.com

# encrypt + sign
gpg --encrypt --sign --armor -r alice@email.com msg.txt
```

---

## One-liner to remember {#one-liner-to-remember}

> **SSH secures connections.
> GPG secures messages — forever.**

---

# Hardware-backed GPG (YubiKey) — the sane way to do crypto

Most people using GPG are doing it wrong.

If your **private key exists on your disk**, you’ve already lost the point.
Malware, backups, cloud sync, laptop theft — take your pick.

Hardware-backed GPG fixes this by doing something radical:

> **The private key never leaves the device. Ever.**

No files. No copying. No excuses.

---

## What a YubiKey actually does (not what people think) {#what-a-yubikey-actually-does-not-what-people-think}

A YubiKey is not “extra security theater.”
It’s a **hard boundary**.

* Private key lives **inside the chip**
* It cannot be exported
* GPG can only ask the device to sign
* You must **physically touch** it

If your system is compromised, the attacker still can’t sign anything without:

1. Your physical key
2. Your PIN
3. Your consent (touch)

That’s real security.

---

## Why this matters (and why software keys are weak) {#why-this-matters-and-why-software-keys-are-weak}

A software GPG key:

* Lives on disk
* Gets copied into backups
* Ends up in cloud sync
* Can be stolen silently

A hardware-backed key:

* Is useless without the device
* Cannot be exfiltrated
* Forces human presence

This is why serious developers use hardware keys and everyone else writes blog posts.

---

## What you actually need {#what-you-actually-need}

* A YubiKey (5 series is fine)
* GnuPG ≥ 2.2
* A working brain
* A few minutes of setup

That’s it.

---

## Install the required junk (once) {#install-the-required-junk-once}

On Linux:

```bash
sudo pacman -S gnupg yubikey-manager pcsclite ccid
sudo systemctl enable --now pcscd
```

Plug in the YubiKey and verify it exists:

```bash
ykman info
```

If that doesn’t work, stop here and fix your system first.

---

## Reset the OpenPGP app (clean slate) {#reset-the-openpgp-app-clean-slate}

If you’ve used the key before, wipe it.
Old keys are dead weight.

```bash
gpg --card-edit
```

Inside GPG:

```
admin
factory-reset
```

Yes, it deletes everything. That’s the point.

---

## Generate keys **on the hardware**, not on disk {#generate-keys-on-the-hardware-not-on-disk}

This is the step most guides screw up.

Do **not** generate keys on your computer and “move” them later unless you know exactly why.

Instead:

```bash
gpg --card-edit
```

Then:

```
admin
generate
```

Choose:

* RSA 4096
* No expiration (or short if you’re paranoid)

Set:

* A **PIN** (daily use)
* An **Admin PIN** (rare use)

These protect physical access.
They are not passphrases. Don’t confuse them.

---

## Verify the key is actually hardware-backed {#verify-the-key-is-actually-hardware-backed}

Run:

```bash
gpg --list-secret-keys
```

You should see:

```
sec> rsa4096/KEYID
```

That `>` matters.

It means:

> “This machine does not have the private key.”

Good.

---

## Force touch confirmation (non-negotiable) {#force-touch-confirmation-non-negotiable}

Without touch, malware can still abuse your key.

Enable it:

```bash
ykman openpgp keys set-touch sig on
ykman openpgp keys set-touch enc on
ykman openpgp keys set-touch aut on
```

Now every signature requires:

* Device present
* Finger on key

Security achieved.

---

## Use it with Git (the only reason most people care) {#use-it-with-git-the-only-reason-most-people-care}

Tell Git to sign everything:

```bash
git config --global user.signingkey KEYID
git config --global commit.gpgsign true
git config --global gpg.program gpg
```

Test it:

```bash
git commit -S -m "test"
```

The key blinks.
You touch it.
The commit signs.

This is how it should feel.

---

## Add the public key to GitHub {#add-the-public-key-to-github}

Export it:

```bash
gpg --armor --export KEYID
```

Paste it into GitHub → **SSH and GPG keys**.

Now commits show **Verified**, and that badge actually means something.

---

## Backups (because hardware breaks) {#backups-because-hardware-breaks}

Hardware is secure.
Hardware also gets lost.

Generate a revocation certificate **now**, not later:

```bash
gpg --gen-revoke KEYID > revoke.asc
```

Store it:

* Offline
* Encrypted
* Somewhere you won’t forget

If the key is lost:

* Import revocation
* Identity is dead
* Damage contained

No panic. No drama.

---

## What this setup protects you from {#what-this-setup-protects-you-from}

* Stolen laptops
* Malware stealing keys
* CI token leaks
* Silent signing
* Backup compromise

What it does **not** protect you from:

* You signing garbage
* Trusting the wrong people
* Bad judgment

Crypto can’t fix stupidity.

---

## The takeaway {#the-takeaway}

If your private key is:

* On disk
* In backups
* In the cloud

You don’t control it.

Hardware-backed GPG is the point where cryptography stops being academic and starts being real.

Anything less is convenience cosplay.

---
