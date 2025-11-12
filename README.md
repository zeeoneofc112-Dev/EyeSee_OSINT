# 👁️ EYESEE v1.0 - The All-Seeing OSINT Tool

![EYESEE](https://img.shields.io/badge/EYESEE-v1.0_Hybrid-blue)
![Python](https://img.shields.io/badge/Python-3.6%2B-green)
![JavaScript](https://img.shields.io/badge/JavaScript-Node.js-yellow)
![License](https://img.shields.io/badge/License-GrayHat_Ethical-orange)

**EYESEE** adalah tools OSINT (Open Source Intelligence) hybrid yang menggabungkan kekuatan Python dan JavaScript dalam satu base code. Tools ini dirancang untuk investigasi digital yang etis dan legal.

## 🎯 Filosofi
- **👁️ Mata** - Melihat kebenaran melalui data digital
- **🔍 Intelligence** - Mengumpulkan informasi dari sumber publik  
- **⚖️ Ethical** - Untuk keadilan dan perlindungan

## 🚀 Cara Menjalankan Tools

### **Persiapan Sistem:**
```bash
# Untuk Termux (Android)
pkg update && pkg upgrade
pkg install python nodejs -y

# Untuk Linux
sudo apt update && sudo apt install python3 python3-pip nodejs npm

# Install Python dependencies
pip install requests beautifulsoup4 phonenumbers

# Install JavaScript dependencies (Optional)
npm install google-libphonenumber

Jalankan EYESEE:

```bash
# Cara 1: Langsung run
python eyesee.py

# Cara 2: Dengan installer
python Installer.py
```

Menu Utama EYESEE:

```
🎯 EYESEE INVESTIGATION MENU:
══════════════════════════════════════════════
1. 🆔  NIK Analyzer - Identitas Digital
2. 📞  Number Tracker - Jejak Telekomunikasi 
3. 🌐  IP Tracer - Geolokasi & ISP
4. 👤  Social Scanner - Digital Footprint
5. 📧  Email Investigator - Digital Identity
6. 🚀  Quick Scan - Auto Multi-Scan
7. ℹ️   Credits & Disclaimer
8. 🚪  Keluar
```

✨ Fitur-Fitur Tools

🔍 Core Investigation Features:

1. NIK Analyzer

· Validasi format NIK Indonesia (16 digit)
· Ekstrak informasi: provinsi, tanggal lahir, jenis kelamin
· Teknologi: Python + JavaScript validation

2. Number Lookup

· Tracking nomor telepon Indonesia
· Deteksi operator (Telkomsel, Indosat, XL, dll)
· Validasi format internasional & nasional
· Teknologi: Hybrid Python + Google LibPhoneNumber

3. IP Tracer

· Geolokasi IP address
· Informasi ISP dan organisasi
· Data koordinat latitude & longitude

4. Social Media Scanner

· Digital footprint analysis
· Check username across platforms:
  · Instagram, Twitter, Facebook
  · TikTok, YouTube, GitHub, Reddit

5. Email Investigator

· Validasi format email
· Gravatar profile detection
· Domain analysis

6. Quick Scan

· Auto-detection input type
· Multi-platform scanning
· Batch processing capability

⚡ Advanced Features:

· Hybrid Engine: Python core + JavaScript enhancement
· Smart Detection: Auto-fallback ketika JavaScript tidak tersedia
· Multi-threading: Concurrent scanning untuk performa optimal
· Colorful UI: User interface yang informatif

🛠️ Teknologi Yang Digunakan

Python Core:

· requests - HTTP requests
· phonenumbers - Phone number parsing
· beautifulsoup4 - HTML parsing
· socket - Network operations

JavaScript Enhancement:

· google-libphonenumber - Advanced phone validation
· Native Node.js - JavaScript runtime

Hybrid Architecture:

```python
# Single base code - dual language power
if js_engine_ready:
    # Gunakan JavaScript untuk validasi
else:
    # Fallback ke Python murni
```

⚠️ Disclaimer & Tanggung Jawab

PENGGUNAAN YANG DIJINKAN:

✅ Investigasi legal dan etis
✅ Penelitian keamanan siber
✅ Edukasi dan pembelajaran
✅ Verifikasi data publik
✅ Perlindungan dari penipuan

PENGGUNAAN YANG DILARANG:

❌ Aktivitas illegal
❌ Pelanggaran privasi
❌ Penipuan atau scam
❌ Stalking atau harassment
❌ Tujuan kriminal

PERNYATAAN TANGGUNG JAWAB:

"Tanggung jawab sepenuhnya berada pada pengguna, bukan developer."

Developer tidak bertanggung jawab atas:

· Penyalahgunaan tools untuk aktivitas illegal
· Konsekuensi hukum dari penggunaan tools
· Kerugian yang ditimbulkan oleh pengguna
· Pelanggaran privasi yang dilakukan pengguna

Setiap pengguna dianggap sudah:

· Memahami risiko dan konsekuensi
· Mematuhi hukum yang berlaku
· Menggunakan tools dengan bijaksana
· Bertanggung jawab penuh atas tindakannya

👥 Development Team

Lead Developer:

· MR-Zeeone-Grayhat

Contributors:

· Aletta Code - Security Research
· AortaVx - OSINT Specialist
· TypeByte - Code Architecture
· Haket Cyber - Cyber Intelligence

📞 Support

Untuk Bantuan Teknis:

1. Pastikan dependencies terinstall
2. Cek koneksi internet
3. Gunakan Python 3.6+
4. Node.js optional (untuk fitur JavaScript)

Untuk Issue Legal:

Konsultasi dengan ahli hukum setempat mengenai regulasi OSINT di wilayah Anda.

🔄 Changelog

v1.0 (Current)

· ✅ Hybrid Python + JavaScript architecture
· ✅ 6 core investigation features
· ✅ Auto-detection & fallback system
· ✅ Ethical guidelines integration

📜 License

GrayHat Ethical Edition - Untuk tujuan baik dengan tanggung jawab.

---

⚠️ PERINGATAN:
Tools ini dibuat untuk edukasi dan penelitian. Pengguna bertanggung jawab penuh atas penggunaan tools ini. Selalu patuhi hukum yang berlaku di wilayah Anda.
