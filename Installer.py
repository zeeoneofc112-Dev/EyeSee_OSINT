#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ╔═══════════════════════════════════════════╗
# ║           EYESEE QUICK INSTALLER          ║
# ║         Dependencies Fixer Script         ║
# ║          GrayHat Ethical Edition          ║
# ╚═══════════════════════════════════════════╝

import os
import sys
import subprocess
import time

class EyeSeeInstaller:
    def __init__(self):
        self.requirements = ["requests", "beautifulsoup4", "phonenumbers", "colorama"]
    
    def clear_screen(self):
        os.system('clear')
    
    def print_banner(self):
        print("\033[1;36m")
        print("╔═══════════════════════════════════════════╗")
        print("║           EYESEE QUICK INSTALLER          ║")
        print("╚═══════════════════════════════════════════╝")
        print("    ╔═╗┬ ┬┌─┐┌─┐┌─┐┬┌─  ┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐")
        print("    ║ ║│ │└─┐│  ├─┤├┴┐  │ │├┬┘├─┤│  ├┤ ├┬┘")
        print("    ╚═╝└─┘└─┘└─┘┴ ┴┴ ┴  └─┘┴└─┴ ┴└─┘└─┘┴└─")
        print("    One-Click Dependencies Installer")
        print("\033[0m")
    
    def install_dependencies(self):
        print("\033[1;33m[🚀] Installing dependencies...\033[0m")
        time.sleep(2)
        
        for package in self.requirements:
            try:
                print(f"\033[1;34m[→] Installing {package}...\033[0m")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"\033[1;32m[✓] {package} installed\033[0m")
                time.sleep(1)
            except:
                print(f"\033[1;31m[✗] Failed to install {package}\033[0m")
    
    def run_installation(self):
        self.clear_screen()
        self.print_banner()
        self.install_dependencies()
        
        print("\n\033[1;32m🎉 Installation completed!\033[0m")
        print("\033[1;36m🚀 Run: python eyesee.py\033[0m")
        
        run_now = input("\nRun EYESEE now? (y/N): ").strip().lower()
        if run_now == 'y':
            os.system('python eyesee.py')

if __name__ == "__main__":
    EyeSeeInstaller().run_installation()
