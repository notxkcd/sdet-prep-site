---
title: "GPG vs SSH — When to Use Which"
weight: 5
---

## Table of Contents
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

