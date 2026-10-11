<div align="center">

# 🤖 MT5 AI Trading Bot
### Automated AI-Powered Trading System with MetaTrader 5 Integration

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![MetaTrader 5](https://img.shields.io/badge/MetaTrader-5-green?logo=meta&logoColor=white)](https://www.metatrader5.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Working-success)]()

</div>

---

## 📋 Daftar Isi
- [⚠️ Disclaimer Penting](#-disclaimer-penting)
- [🎯 Tentang Proyek](#-tentang-proyek)
- [✨ Fitur Utama](#-fitur-utama)
- [📦 Prasyarat](#-prasyarat)
- [🚀 Instalasi Lengkap](#-instalasi-lengkap)
- [📖 Cara Penggunaan](#-cara-penggunaan)
- [📁 Struktur Proyek](#-struktur-proyek)
- [🌐 Deployment ke VPS (24/7)](#-deployment-ke-vps-247)
- [🗺️ Roadmap](#-roadmap)
- [🤝 Kontribusi](#-kontribusi)

---

## ⚠️ Disclaimer Penting

> **🚨 PERINGATAN RISIKO:** Trading forex, saham, dan instrumen keuangan lainnya memiliki tingkat risiko yang sangat tinggi. 
> - Penulis **TIDAK BERTANGGUNG JAWAB** atas kerugian finansial apapun yang terjadi akibat penggunaan bot ini.
> - Performa masa lalu (backtest) **TIDAK MENJAMIN** hasil di masa depan.
> - **SELALU** gunakan akun **DEMO** terlebih dahulu untuk pengujian.
> - Gunakan bot ini dengan risiko Anda sendiri (*Use at your own risk*).

---

## 🎯 Tentang Proyek

**MT5 AI Trading Bot** adalah sistem trading otomatis yang menggabungkan kekuatan **Python** dan **Machine Learning** dengan platform **MetaTrader 5**. Bot ini menganalisis data pasar secara real-time, memprediksi pergerakan harga menggunakan model AI (Random Forest), dan mengeksekusi order secara otomatis dengan manajemen risiko (Stop Loss & Take Profit) yang terintegrasi.

---

## ✨ Fitur Utama

- 🔌 **Integrasi MT5 Penuh** via official Python API.
- 🧠 **Machine Learning** menggunakan Random Forest Classifier untuk prediksi arah harga.
- 📊 **Analisis Teknikal Otomatis** (SMA, RSI, MACD) yang dihitung secara real-time via `pandas-ta`.
- 🔄 **Loop Trading 24/7** yang siap di-deploy ke Windows VPS.
- 🛡️ **Manajemen Risiko** dengan perhitungan Stop Loss dan Take Profit otomatis per trade.
Black Cube Code Developer
Free Public Discussion https://t.me/bcpublicchat
Bot AI Trading https://t.me/blackcubecodeAI_Bot
Daily Signal XAUUSD https://t.me/blackcubecode
---

## 📦 Prasyarat

Sebelum memulai, pastikan Anda telah menginstal software berikut di komputer Anda:
1. **Windows 10 atau 11** *(Library MetaTrader5 untuk Python hanya mendukung Windows)*.
2. **Python 3.12.x** *(Sangat direkomendasikan. Versi 3.13+ mungkin mengalami masalah kompatibilitas dengan library `numba`/`pandas-ta`)*. [Download Python 3.12](https://www.python.org/downloads/release/python-31210/)
3. **Git** untuk Windows. [Download Git](https://git-scm.com/download/win)
4. **MetaTrader 5 (MT5)** yang sudah terinstal dan Anda sudah login ke akun (Disarankan akun **DEMO** terlebih dahulu).

---

## 🚀 Instalasi Lengkap

Ikuti langkah-langkah ini secara berurutan untuk menyiapkan lingkungan pengembangan di laptop Anda.

### 1. Clone Repository
Buka **PowerShell** atau **Command Prompt**, lalu jalankan perintah berikut:
```bash
git clone https://github.com/blackcubecode/mt5-ai-bot.git
cd mt5-ai-bot
