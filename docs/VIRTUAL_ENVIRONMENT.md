<div align="center">

# 🐍 Panduan Virtual Environment Python

### Cara Membuat & Mengaktifkan Virtual Environment di Windows

[![Windows](https://img.shields.io/badge/OS-Windows-blue?logo=windows)]()
[![Python](https://img.shields.io/badge/Python-3.12+-yellow?logo=python)]()
[![Level](https://img.shields.io/badge/Level-Pemula-green)]()

</div>

---

## 🤔 Apa Itu Virtual Environment?

**Virtual Environment** (atau `venv`) adalah **ruang kerja terisolasi** untuk proyek Python Anda. Bayangkan seperti ini:

> 🏠 **Rumah Anda** = Laptop/Komputer Anda  
> 🚪 **Kamar Tidur** = Virtual Environment  
> 🛏️ **Perlengkapan di Kamar** = Library Python yang diinstal khusus untuk proyek ini

Dengan `venv`, setiap proyek Python memiliki "kamarnya sendiri" sehingga library yang diinstal untuk satu proyek **tidak akan bentrok** dengan proyek lain.

### ❓ Kenapa Harus Pakai Virtual Environment?

| Tanpa venv 😰 | Dengan venv 😎 |
|---------------|----------------|
| Library bentrok antar proyek | Setiap proyek punya library sendiri |
| Sulit deploy ke server lain | Mudah direplikasi di mana saja |
| Versi library bercampur | Versi library terkontrol |
| Sulit debugging | Mudah debugging |

---

## 📋 Prasyarat

Sebelum memulai, pastikan Anda sudah memiliki:

- [x] **Windows 10/11** terinstal
- [x] **Python 3.12+** sudah terinstal ([Download di sini](https://www.python.org/downloads/release/python-31210/))
- [x] **PowerShell** atau **Command Prompt** tersedia

### ✅ Cara Cek Python Sudah Terinstal

Buka PowerShell dan ketik:
```bash
python --version
