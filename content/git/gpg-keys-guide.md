---
title: "GPG: Generate Keys + Use Passphrase"
weight: 4
---

## Table of Contents
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

