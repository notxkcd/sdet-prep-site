---
title: "The KaTeX Font Gallery"
date: 2026-01-30
draft: false
category: "Projects"
description: "A visual specimen of every font family available in our local KaTeX installation."
---

# The Typography of Mathematics

KaTeX doesn't just render math; it renders it with style. Below is a complete gallery of the different font families available in our local installation.

## 1. The Classics (Standard Roman)
The default font used for variables and text in math mode. It's the "Times New Roman" of the math world—reliable, serif, and academic.

**Command:** `\mathrm{...}` or default
$$ \text{Standard: } abcdefghijklmnopqrstuvwxyz $$
$$ \mathrm{Roman: } \mathrm{abcdefghijklmnopqrstuvwxyz} $$
$$ \text{Equation: } E = mc^2 + \int_0^\infty f(x) dx $$

---

## 2. Calligraphic (mathcal)
This is what you asked for. Used for sets, Lagrangians, and fancy operators. Only supports uppercase letters.

**Command:** `\mathcal{...}`
$$ \mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ} $$
$$ \text{Lagrangian: } \mathcal{L} = T - V $$
$$ \text{Set Theory: } \mathcal{P}(S) = \{ x \mid x \subseteq S \} $$

---

## 3. Blackboard Bold (mathbb)
The standard for number sets (Reals, Integers, Complex). It looks like it was written on a chalkboard with double strokes.

**Command:** `\mathbb{...}`
$$ \mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ} $$
$$ \text{The Sets: } \mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C} $$
$$ \text{Probability: } \mathbb{E}[X] = \sum x p(x) $$

---

## 4. Fraktur (mathfrak)
Old German gothic script. Used in Lie algebras and abstract algebra. It looks metal as hell.

**Command:** `\mathfrak{...}`
$$ \mathfrak{abcdefghijklmnopqrstuvwxyz} $$
$$ \mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZ} $$
$$ \text{Lie Algebra: } \mathfrak{g} \cong \mathfrak{su}(2) $$

---

## 5. Sans-Serif (mathsf)
Clean, modern, without the "feet" on the letters. Good for matrices or tensors where you want a cleaner look.

**Command:** `\mathsf{...}`
$$ \mathsf{abcdefghijklmnopqrstuvwxyz} $$
$$ \mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZ} $$
$$ \text{Matrix: } \mathsf{M} \cdot \mathsf{v} = \lambda \mathsf{v} $$

---

## 6. Typewriter (mathtt)
Monospace font. Looks like code. Used for computer science logic or category theory.

**Command:** `\mathtt{...}`
$$ \mathtt{abcdefghijklmnopqrstuvwxyz} $$
$$ \mathtt{ABCDEFGHIJKLMNOPQRSTUVWXYZ} $$
$$ \text{Turing Machine: } \mathtt{q_0} \xrightarrow{\mathtt{0/1, R}} \mathtt{q_1} $$

---

## 7. Bold Italic (boldsymbol)
When you need to shout in math.

**Command:** `\boldsymbol{...}`
$$ \boldsymbol{abcdefghijklmnopqrstuvwxyz} $$
$$ \boldsymbol{ABCDEFGHIJKLMNOPQRSTUVWXYZ} $$
$$ \text{Vector Force: } \boldsymbol{F} = m \boldsymbol{a} $$

---

## 8. Script (mathscr)
Similar to Calligraphic but often curlier. Note: In standard KaTeX, `\mathscr` usually maps to `\mathcal` unless a specific script font is loaded, but let's test it.

**Command:** `\mathscr{...}` (Requires `mathrsfs` usually, KaTeX approximates it)
$$ \mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ} $$

---

## 9. Comparison Table

| Style | Command | Sample |
| :--- | :--- | :--- |
| **Roman** | `\mathrm{A}` | $\mathrm{A}$ |
| **Calligraphic** | `\mathcal{A}` | $\mathcal{A}$ |
| **Blackboard** | `\mathbb{A}` | $\mathbb{A}$ |
| **Fraktur** | `\mathfrak{A}` | $\mathfrak{A}$ |
| **Sans-Serif** | `\mathsf{A}` | $\mathsf{A}$ |
| **Typewriter** | `\mathtt{A}` | $\mathtt{A}$ |
| **Bold** | `\mathbf{A}` | $\mathbf{A}$ |
| **Italic** | `\mathit{A}` | $\mathit{A}$ |
