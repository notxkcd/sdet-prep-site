---
title: "Hardware-backed GPG (YubiKey)"
weight: 6
---

## Table of Contents
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
