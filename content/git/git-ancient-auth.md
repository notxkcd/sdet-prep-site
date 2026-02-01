---
title: "Why Git still uses ancient auth"
weight: 8
---

## Table of Contents
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

