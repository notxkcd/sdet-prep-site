---
title: "GitHub Authentication Tutorial (SSH vs HTTPS)"
weight: 2
---

## Table of Contents
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

