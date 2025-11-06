# 🔒 Hash Function Security Visualizer

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)]()

---

## 🧩 Overview
**Hash Function Security Visualizer** is a Python-based interactive tool for visualizing the **avalanche behavior in cryptographic hash functions**.
It quantifies and visualizes how single-bit changes in input propagate through the output space of selected hash algorithms.

Developed as part of an applied study in the domain of **cryptographic primitives and integrity verification**, this project bridges academic analysis and visual understanding of hash diffusion.

---

## 🎯 Motivation
Cryptographic hash functions are foundational to modern security — from password storage to integrity validation.
Their internal diffusion properties, however, often remain abstract.

This visualizer makes those properties **observable and measurable**, enabling researchers and students to explore the **Avalanche Effect** — a critical indicator of cryptographic strength and unpredictability.

---

## ⚙️ Features
- Compare multiple hash algorithms (`SHA‑1`, `SHA‑256`, `MD5`)
- Binary-level difference mapping for input perturbations
- Avalanche score computation (percentage of changed bits)
- Real‑time visualization via `Matplotlib`
- Interactive UI built with `Streamlit`


---

## 🚀 Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/Ali-Hajipour/HashFunctionSecurityVisualizer.git
cd HashFunctionSecurityVisualizer
pip install -r requirements.txt
