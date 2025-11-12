#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# ╔═══════════════════════════════════════════╗
# ║                 EYESEE v1.0               ║
# ║         The All-Seeing OSINT Tool         ║
# ║          GrayHat Ethical Hacking          ║
# ╚═══════════════════════════════════════════╝

import requests
import json
import phonenumbers
from bs4 import BeautifulSoup
import socket
import re
import os
from datetime import datetime
import time
import hashlib

class EyeSee:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        self.version = "v1.0"
        self.author = "MR-Zeeone-Grayhat"
        self.contributors = [
            "Aletta Code",
            "AortaVx", 
            "TypeByte",
            "Haket Cyber"
        ]
    
    def welcome_animation(self):
        """Animasi welcome yang keren"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        welcome_text = """
╔═══════════════════════════════════════════╗
║                 EYESEE v1.0               ║
║         The All-Seeing OSINT Tools         ║
║          GrayHat Ethical Hacking          ║
╚═══════════════════════════════════════════╝
        """
        
        print("\033[1;36m")  # Cyan color
        for line in welcome_text.split('\n'):
            print(line)
            time.sleep(0.1)
        
        print("\033[1;33m")  # Yellow color
        print("Initializing System...")
        
        # Loading animation
        for i in range(3):
            for char in ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']:
                print(f"\rLoading {char} Preparing OSINT Engine...", end='', flush=True)
                time.sleep(0.1)
        
        print("\n\033[1;32m")  # Green color
        print("✓ System Ready!")
        print("✓ Modules Loaded!") 
        print("✓ Database Connected!")
        
        time.sleep(1)
        print("\033[1;35m")  # Magenta color
        print("\n" + "═" * 50)
        print("👁️  WELCOME TO EYESEE - THE ALL-SEEING EYE")
        print("═" * 50)
        
        print("\033[1;36m")
        print("Created by: \033[1;33mMR-Zeeone-Grayhat\033[1;36m")
        print("Contributors Team:")
        for contributor in self.contributors:
            print(f"  • \033[1;32m{contributor}\033[1;36m")
        
        print("\033[1;35m")
        print("═" * 50)
        print("🔍 Your Digital Investigation Partner")
        print("⚖️  Use Responsibly & Ethically")
        print("👁️  Truth Through Digital Intelligence")
        print("═" * 50)
        
        time.sleep(2)
        print("\033[0m")  # Reset color

    def banner(self):
        print(f"""
    ╔═╗┬ ┬┌─┐┌─┐┌─┐┬┌─  ┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
    ║ ║│ │└─┐│  ├─┤├┴┐  │ │├┬┘├─┤│  ├┤ ├┬┘
    ╚═╝└─┘└─┘└─┘┴ ┴┴ ┴  └─┘┴└─┴ ┴└─┘└─┘┴└─
    
        The All-Seeing OSINT Tool {self.version}
        Created by: {self.author}
        ═══════════════════════════════════
        👁️  Mata untuk Melihat Kebenaran
        🔍  Tools Investigasi Digital
        ⚖️  Ethical GrayHat Edition
        """)
    
    def show_credits(self):
        print("""
        ═══════════════════════════════════
        CREDITS:
        👁️  EYESEE Philosophy:
          - Mata yang Melihat Kebenaran
          - Pengawasan untuk Keadilan  
          - Intelligence untuk Perlindungan
        
        🛠️ DEVELOPMENT TEAM:
          Lead Developer: MR-Zeeone-Grayhat
          Security Research: Aletta Code
          OSINT Specialist: AortaVx
          Code Architecture: TypeByte  
          Cyber Intelligence: Haket Cyber
        
        ⚠️  DISCLAIMER:
        Gunakan dengan bijak dan legal!
        Tanggung jawab sepenuhnya ada pada user.
        Hanya untuk tujuan edukasi dan investigasi legal.
        """)

    def nik_parser(self, nik):
        print(f"\n[👁️] EYESEE Analyzing NIK: {nik}")
        
        # Validasi format NIK (16 digit)
        if not re.match(r'^\d{16}$', nik):
            return "❌ Format NIK tidak valid"
        
        try:
            # Extract info dari NIK
            kode_provinsi = nik[0:2]
            kode_kabupaten = nik[0:4]
            tgl_lahir = int(nik[6:8])
            bulan_lahir = int(nik[8:10])
            tahun_lahir = int(nik[10:12])
            
            # Adjust tahun lahir
            if tahun_lahir <= 23:
                tahun_lahir += 2000
            else:
                tahun_lahir += 1900
            
            # Jenis kelamin (tgl lahir > 40 = perempuan)
            if tgl_lahir > 40:
                jenis_kelamin = "Perempuan"
                tgl_lahir -= 40
            else:
                jenis_kelamin = "Laki-laki"
            
            # Mapping kode provinsi (contoh)
            provinsi_map = {
                '11': 'Aceh', '12': 'Sumatera Utara', '13': 'Sumatera Barat',
                '14': 'Riau', '15': 'Jambi', '16': 'Sumatera Selatan',
                '17': 'Bengkulu', '18': 'Lampung', '19': 'Kepulauan Bangka Belitung',
                '21': 'Kepulauan Riau', '31': 'DKI Jakarta', '32': 'Jawa Barat',
                '33': 'Jawa Tengah', '34': 'DI Yogyakarta', '35': 'Jawa Timur',
                '36': 'Banten', '51': 'Bali', '52': 'Nusa Tenggara Barat',
                '53': 'Nusa Tenggara Timur', '61': 'Kalimantan Barat',
                '62': 'Kalimantan Tengah', '63': 'Kalimantan Selatan', 
                '64': 'Kalimantan Timur', '65': 'Kalimantan Utara',
                '71': 'Sulawesi Utara', '72': 'Sulawesi Tengah',
                '73': 'Sulawesi Selatan', '74': 'Sulawesi Tenggara',
                '75': 'Gorontalo', '76': 'Sulawesi Barat',
                '81': 'Maluku', '82': 'Maluku Utara',
                '91': 'Papua Barat', '92': 'Papua'
            }
            
            provinsi = provinsi_map.get(kode_provinsi, "Tidak Diketahui")
            
            result = {
                'NIK': nik,
                'Provinsi': f"{provinsi} ({kode_provinsi})",
                'Kabupaten/Kota': f"Kode {kode_kabupaten}",
                'Tanggal Lahir': f"{tgl_lahir:02d}-{bulan_lahir:02d}-{tahun_lahir}",
                'Jenis Kelamin': jenis_kelamin,
                'Status': "✅ Valid (Format NIK)",
                'Keterangan': 'Data berdasarkan format NIK Indonesia'
            }
            
            return result
            
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def number_lookup(self, number):
        print(f"\n[👁️] EYESEE Tracking Number: {number}")
        
        try:
            # Format number
            parsed = phonenumbers.parse(number, "ID")
            format_intl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            format_national = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            
            # Deteksi operator Indonesia
            national_num = str(parsed.national_number)
            prefix = national_num[:4] if len(national_num) >= 4 else national_num[:3]
            
            operators = {
                '0811': 'Telkomsel (Halo)', '0812': 'Telkomsel (Simpati)', '0813': 'Telkomsel (Simpati)',
                '0821': 'Telkomsel (Simpati)', '0822': 'Telkomsel (Simpati)', '0823': 'Telkomsel (AS)',
                '0852': 'Telkomsel (AS)', '0853': 'Telkomsel (AS)', '0814': 'Telkomsel (AS)',
                '0815': 'Indosat', '0816': 'Indosat', '0817': 'Indosat', '0855': 'Indosat', 
                '0856': 'Indosat', '0857': 'Indosat', '0858': 'Indosat', '0859': 'XL',
                '0818': 'XL', '0819': 'XL', '0877': 'XL', '0878': 'XL', '0879': 'XL',
                '0895': 'Three', '0896': 'Three', '0897': 'Three', '0898': 'Three', '0899': 'Three',
                '0881': 'Smartfren', '0882': 'Smartfren', '0883': 'Smartfren', '0884': 'Smartfren',
                '0885': 'Smartfren', '0886': 'Smartfren', '0887': 'Smartfren', '0888': 'Smartfren',
                '0889': 'Smartfren'
            }
            
            operator = operators.get(prefix, "❓ Unknown Operator")
            
            result = {
                'Number': format_intl,
                'National Format': format_national,
                'Operator': operator,
                'Valid': '✅ Ya' if phonenumbers.is_valid_number(parsed) else '❌ Tidak',
                'Prefix': prefix,
                'Region': 'Indonesia',
                'Keterangan': 'Data operator berdasarkan prefix Indonesia'
            }
            
            return result
            
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def ip_parser(self, ip):
        print(f"\n[👁️] EYESEE Tracing IP: {ip}")
        
        try:
            # Validasi IP format
            if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
                return "❌ Format IP tidak valid"
            
            # Geolocation sederhana
            response = self.session.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            
            if data['status'] == 'success':
                result = {
                    'IP Address': ip,
                    'Country': data.get('country', 'N/A'),
                    'Region': data.get('regionName', 'N/A'),
                    'City': data.get('city', 'N/A'),
                    'ISP': data.get('isp', 'N/A'),
                    'Organization': data.get('org', 'N/A'),
                    'AS Number': data.get('as', 'N/A'),
                    'Latitude': data.get('lat', 'N/A'),
                    'Longitude': data.get('lon', 'N/A'),
                    'Timezone': data.get('timezone', 'N/A'),
                    'ZIP Code': data.get('zip', 'N/A')
                }
                return result
            else:
                return "❌ IP tidak valid atau tidak ditemukan"
                
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def social_lookup(self, username):
        print(f"\n[👁️] EYESEE Scanning Digital Footprint: {username}")
        
        platforms = {
            'Instagram': f'https://www.instagram.com/{username}',
            'Twitter': f'https://twitter.com/{username}',
            'Facebook': f'https://facebook.com/{username}',
            'TikTok': f'https://tiktok.com/@{username}',
            'YouTube': f'https://youtube.com/@{username}',
            'GitHub': f'https://github.com/{username}',
            'Reddit': f'https://reddit.com/user/{username}'
        }
        
        results = {}
        
        for platform, url in platforms.items():
            try:
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    results[platform] = {
                        'URL': url,
                        'Exists': '✅ Mungkin Ada',
                        'Status Code': response.status_code
                    }
                elif response.status_code == 404:
                    results[platform] = {
                        'URL': url,
                        'Exists': '❌ Tidak Ditemukan',
                        'Status Code': response.status_code
                    }
                else:
                    results[platform] = {
                        'URL': url,
                        'Exists': '⚠️ Tidak Dapat Diakses',
                        'Status Code': response.status_code
                    }
            except Exception as e:
                results[platform] = {
                    'URL': url,
                    'Exists': '🚫 Error/Gagal Check',
                    'Error': str(e)
                }
        
        return results

    def main_menu(self):
        self.welcome_animation()  # Panggil welcome animation
        time.sleep(1)
        self.banner()
        
        while True:
            print("\n" + "═" * 60)
            print("🎯 EYESEE INVESTIGATION MENU:")
            print("═" * 60)
            print("1. 🆔  NIK Analyzer - Identitas Digital")
            print("2. 📞  Number Tracker - Jejak Telekomunikasi") 
            print("3. 🌐  IP Tracer - Geolokasi & ISP")
            print("4. 👤  Social Scanner - Digital Footprint")
            print("5. 📧  Email Investigator - Digital Identity")
            print("6. 🚀  Quick Scan - Auto Multi-Scan")
            print("7. ℹ️   Credits & Disclaimer")
            print("8. 🚪  Keluar")
            print("═" * 60)
            
            choice = input("\n[EYESEE] Pilih investigasi [1-8]: ").strip()
            
            if choice == '1':
                nik = input("[🆔] Masukkan NIK target: ").strip()
                result = self.nik_parser(nik)
                self.print_result(result, "NIK FORENSIC ANALYSIS")
                
            elif choice == '2':
                number = input("[📞] Masukkan Nomor target: ").strip()
                result = self.number_lookup(number)
                self.print_result(result, "COMMUNICATION INTELLIGENCE")
                
            elif choice == '3':
                ip = input("[🌐] Masukkan IP Address target: ").strip()
                result = self.ip_parser(ip)
                self.print_result(result, "DIGITAL GEO-LOCATION")
                
            elif choice == '4':
                username = input("[👤] Masukkan Username target: ").strip()
                result = self.social_lookup(username)
                self.print_result(result, "SOCIAL MEDIA RECON")
                
            elif choice == '5':
                email = input("[📧] Masukkan Email target: ").strip()
                result = self.email_osint(email)
                self.print_result(result, "EMAIL INVESTIGATION")
                
            elif choice == '6':
                target = input("[🚀] Masukkan target (NIK/Nomor/IP/Username/Email): ").strip()
                result = self.quick_scan(target)
                self.print_result(result, "QUICK SCAN RESULT")
                
            elif choice == '7':
                self.show_credits()
                
            elif choice == '8':
                print("\n👁️  EYESEE signing off... Stay Vigilant!")
                print("   Truth is the ultimate weapon! 🔍")
                break
            else:
                print("❌ Perintah tidak dikenali!")
    
    def email_osint(self, email):
        print(f"\n[👁️] EYESEE Email Investigation: {email}")
        
        try:
            # Basic email validation
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return "❌ Format email tidak valid"
            
            domain = email.split('@')[-1]
            
            # Gravatar check
            gravatar_hash = hashlib.md5(email.encode().lower()).hexdigest()
            gravatar_url = f"https://gravatar.com/avatar/{gravatar_hash}?d=404"
            
            gravatar_exists = self.session.get(gravatar_url).status_code == 200
            
            result = {
                'Email': email,
                'Domain': domain,
                'Gravatar Available': '✅ Ya' if gravatar_exists else '❌ Tidak',
                'Gravatar URL': gravatar_url if gravatar_exists else 'N/A',
                'Data Breach Check': '🔍 Fitur Premium Required',
                'Social Media Links': '🔍 Scanning Available in Pro Version'
            }
            
            return result
            
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def quick_scan(self, target):
        """Multi-scan untuk investigasi cepat"""
        print(f"\n[👁️] EYESEE Quick Scan: {target}")
        
        results = {}
        
        # Auto-detect type
        if '@' in target:
            results['Email Analysis'] = self.email_osint(target)
        elif re.match(r'^\d{16}$', target):
            results['NIK Analysis'] = self.nik_parser(target)  
        elif re.match(r'^(\+62|62|0)\d+$', target):
            results['Phone Analysis'] = self.number_lookup(target)
        elif re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', target):
            results['IP Analysis'] = self.ip_parser(target)
        else:
            results['Social Media Analysis'] = self.social_lookup(target)
        
        return results

    def print_result(self, result, title):
        print(f"\n{'═' * 70}")
        print(f"👁️  EYESEE RESULT: {title}")
        print(f"{'═' * 70}")
        
        if isinstance(result, dict):
            for key, value in result.items():
                print(f"  🔹 {key}: {value}")
        elif isinstance(result, str):
            print(f"  {result}")
        else:
            print(json.dumps(result, indent=2))
        
        print(f"{'═' * 70}")
        print("📋 Investigasi selesai. Lanjutkan dengan bijak!")

# RUN EYESEE
if __name__ == "__main__":
    try:
        tool = EyeSee()
        tool.main_menu()
    except KeyboardInterrupt:
        print("\n\n👁️  EYESEE interrupted... Stay safe!")
    except Exception as e:
        print(f"\n\n💥 EYESEE Error: {str(e)}")

