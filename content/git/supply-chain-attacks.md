---
title: "How supply-chain attacks actually happen"
weight: 7
---

## Table of Contents
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

