<div align="center">

# 🤖 MT5 AI Trading Bot

### Automated AI-Powered Trading System with MetaTrader 5 Integration

[![Python](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![MetaTrader 5](https://img.shields.io/badge/MetaTrader-5-green?logo=meta&logoColor=white)](https://www.metatrader5.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?logo=github)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Experimental-orange)]()

[📖 Dokumentasi](#-cara-penggunaan) • [🚀 Quick Start](#-instalasi) • [🐛 Laporkan Bug](../../issues) • [💡 Request Fitur](../../issues)

</div>

---

## 📋 Daftar Isi
- [Tentang Proyek](#-tentang-proyek)
- [⚠️ Disclaimer Penting](#-disclaimer-penting)
- [Fitur Utama](#-fitur-utama)
- [Tech Stack](#-tech-stack)
- [Prasyarat](#-prasyarat)
- [Instalasi](#-instalasi)
- [Konfigurasi](#-konfigurasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Struktur Proyek](#-struktur-proyek)
- [Deployment ke VPS](#-deployment-ke-vps-247)
- [Roadmap](#-roadmap)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)

---

## 🎯 Tentang Proyek

**MT5 AI Trading Bot** adalah sistem trading otomatis yang menggabungkan kekuatan **Python** dan **Machine Learning** dengan platform **MetaTrader 5**. Bot ini menganalisis data pasar secara real-time, memprediksi pergerakan harga menggunakan model AI, dan mengeksekusi order secara otomatis.

Proyek ini dirancang untuk:
- 🎓 Trader yang ingin belajar integrasi AI dengan trading
- 🧪 Riset dan eksperimen strategi trading berbasis Machine Learning
- 🤖 Otomatisasi eksekusi trading 24/7

> 💡 **Catatan:** Proyek ini bersifat **edukasi dan riset**. Jangan gunakan langsung di akun real tanpa backtesting dan forward testing yang memadai.

---

## ⚠️ Disclaimer Penting

<div align="center">

### 🚨 PERINGATAN RISIKO

</div>

**Trading forex, saham, dan instrumen keuangan lainnya memiliki tingkat risiko yang tinggi dan mungkin tidak cocok untuk semua investor.**

- ❌ Penulis **TIDAK BERTANGGUNG JAWAB** atas kerugian finansial apapun yang terjadi akibat penggunaan bot ini.
- ❌ Performa masa lalu (backtest) **TIDAK MENJAMIN** hasil di masa depan.
- ❌ Model AI **BUKANLAH** alat yang sempurna dan dapat menghasilkan prediksi yang salah.
- ✅ **SELALU** gunakan akun **DEMO** terlebih dahulu untuk pengujian.
- ✅ **SELALU** terapkan manajemen risiko yang ketat (Stop Loss, position sizing, dll).
- ✅ **SELALU** lakukan backtesting dan forward testing sebelum live trading.

**Gunakan bot ini dengan risiko Anda sendiri (Use at your own risk).**

---

## ✨ Fitur Utama

- 🔌 **Integrasi MT5 Penuh** — Koneksi langsung ke terminal MetaTrader 5 via official Python API
- 🧠 **Machine Learning** — Menggunakan Random Forest Classifier (dapat dikembangkan ke LSTM/Transformer)
- 📊 **Analisis Teknikal Otomatis** — Indikator built-in (SMA, RSI, MACD, Bollinger Bands, dll) via `pandas-ta`
- 🎯 **Auto Target Generation** — Labeling data otomatis berdasarkan pergerakan harga masa depan
- 💾 **Model Persistence** — Simpan dan muat model AI dengan `joblib`
- 🔄 **Loop Trading 24/7** — Berjalan terus-menerus di Windows VPS
- 📝 **Logging Lengkap** — Setiap keputusan AI tercatat dengan jelas
- 🛡️ **Manajemen Risiko** — SL/TP otomatis per trade

---

## 🛠️ Tech Stack

| Teknologi | Fungsi |
|-----------|--------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | Bahasa pemrograman utama |
| ![MetaTrader5](https://img.shields.io/badge/MetaTrader5-0052CC?logo=meta&logoColor=white) | Eksekusi trading & data feed |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) | Manipulasi data time-series |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white) | Machine Learning model |
| ![Pandas-TA](https://img.shields.io/badge/Pandas--TA-150458?logo=pandas&logoColor=white) | Kalkulasi indikator teknikal |
| ![Joblib](https://img.shields.io/badge/Joblib-000000?logo=python&logoColor=white) | Penyimpanan model (.pkl) |

---

## 📦 Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- [x] **Windows OS** (MT5 Python API hanya berjalan di Windows)
- [x] **MetaTrader 5** terinstal dan terkoneksi ke broker
- [x] **Python 3.8 - 3.10** ([Download di sini](https://www.python.org/downloads/))
- [x] **Git** ([Download di sini](https://git-scm.com/))
- [x] Akun broker yang mendukung MT5
- [x] *(Opsional)* **Windows VPS** untuk menjalankan bot 24/7

---

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/blackcubecode/mt5-ai-trading-bot.git
cd mt5-ai-trading-bot
