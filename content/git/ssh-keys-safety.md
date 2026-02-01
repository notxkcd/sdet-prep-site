---
title: "Why SSH keys feel annoying — but are safer"
weight: 3
---

## Table of Contents
- [1. They don’t fit our “password brain”](#1-they-dont-fit-our-password-brain)
- [2. You never actually send the secret](#2-you-never-actually-send-the-secret)
- [3. Passphrases protect against device theft](#3-passphrases-protect-against-device-theft)
- [4. SSH agents feel magical (and scary)](#4-ssh-agents-feel-magical-and-scary)
- [5. You can revoke without changing your life](#5-you-can-revoke-without-changing-your-life)
- [6. Automation made SSH unavoidable](#6-automation-made-ssh-unavoidable)
- [7. Why it *feels* worse on day one](#7-why-it-feels-worse-on-day-one)
- [💡 The quiet truth](#the-quiet-truth)
- [TL;DR (stick this)](#tldr-stick-this)


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

