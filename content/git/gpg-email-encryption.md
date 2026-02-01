---
title: "GPG for Email Encryption"
weight: 9
---

## Table of Contents
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

