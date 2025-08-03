#!/usr/bin/env python3
import os
import random
import time
import socket
from datetime import datetime
import re

class WhatsAppHacker:
    def __init__(self):
        self.session_id = f"KTH-{random.randint(1000, 9999)}"
        self.target_number = ""
        self.version = "v3.1.5"
        self.author = "NULLSEC"
        self.country_code = "+1"
        self.db_loaded = False
        self.wordlist = []
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def typewriter(self, text, delay=0.03, color=None):
        color_codes = {
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m"
        }
        
        if color in color_codes:
            print(color_codes[color], end='', flush=True)
            
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
            
        print("\033[0m", end='', flush=True)  # Reset color
        
    def validate_whatsapp_number(self, number):
        """Simulate number validation"""
        pattern = r"^\+?[0-9]{10,15}$"
        return re.match(pattern, number)
        
    def load_wordlist(self):
        """Fake wordlist loading"""
        if not self.db_loaded:
            self.typewriter("[+] Loading rainbow tables...", color="yellow")
            time.sleep(2)
            self.wordlist = [
                "password", "123456", "qwerty", 
                "iloveyou", "admin", "welcome"
            ]
            self.db_loaded = True
            self.typewriter(f"[+] Loaded {len(self.wordlist)} common passwords", color="green")
            time.sleep(1)
        
    def fake_bruteforce(self):
        """Simulate password cracking"""
        self.load_wordlist()
        
        self.typewriter(f"\n[+] Starting brute-force on {self.target_number}", color="red")
        self.typewriter("[+] Bypassing WhatsApp encryption...", color="yellow")
        time.sleep(3)
        
        print("\n[PROGRESS]:")
        for i in range(1, 101):
            time.sleep(0.05 * random.random())
            print(f"\r\033[35m[{'█'*(i//2)}{' '*(50-(i//2))}] {i}%", end='', flush=True)
            
        print("\n\n[+] Analyzing results...")
        time.sleep(2)
        
        if random.random() > 0.7:  # 30% success rate
            password = random.choice(self.wordlist)
            self.typewriter(f"\n[SUCCESS] Found password: {password}", color="green")
            self.typewriter(f"[+] Session key extracted: WA-{random.randint(100000,999999)}", color="green")
        else:
            self.typewriter("\n[FAILED] No vulnerabilities found", color="red")
            self.typewriter("[!] Target may have 2FA enabled", color="yellow")
        
    def show_banner(self):
        banner = f"""
  ██╗  ██╗███████╗██╗████████╗██╗  ██╗    ██╗  ██╗██╗██╗     ██╗     
  ██║ ██╔╝██╔════╝██║╚══██╔══╝██║  ██║    ██║ ██╔╝██║██║     ██║     
  █████╔╝ █████╗  ██║   ██║   ███████║    █████╔╝ ██║██║     ██║     
  ██╔═██╗ ██╔══╝  ██║   ██║   ██╔══██║    ██╔═██╗ ██║██║     ██║     
  ██║  ██╗███████╗██║   ██║   ██║  ██║    ██║  ██╗██║███████╗███████╗
  ╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
        """
        self.clear_screen()
        print("\033[31m" + banner + "\033[0m")
        print(f"\033[1;31m>> WHATSAPP CRACKING SUITE {self.version} <<\033[0m")
        print(f"\033[33mSession: {self.session_id} | Time: {datetime.now().strftime('%H:%M:%S')}\033[0m")
        print("\033[34m" + "="*60 + "\033[0m")
        
    def show_menu(self):
        self.show_banner()
        print("\n\033[1mMAIN MENU:\033[0m")
        print("1. Set Target WhatsApp Number")
        print("2. Brute Force Attack")
        print("3. SIM Clone Attack")
        print("4. Message Interception")
        print("5. Exit")
        
        choice = input("\n\033[35m[?] Select option: \033[0m")
        return choice
        
    def run(self):
        while True:
            choice = self.show_menu()
            
            if choice == "1":
                self.clear_screen()
                self.show_banner()
                num = input("\n[+] Enter WhatsApp number (e.g. +1234567890): ")
                
                if self.validate_whatsapp_number(num):
                    self.target_number = num
                    self.typewriter(f"[+] Target set: {self.target_number}", color="green")
                    time.sleep(1)
                else:
                    self.typewriter("[!] Invalid WhatsApp number format", color="red")
                    time.sleep(1)
                    
            elif choice == "2":
                if not self.target_number:
                    self.typewriter("[!] No target number set", color="red")
                    time.sleep(1)
                    continue
                    
                self.clear_screen()
                self.show_banner()
                self.fake_bruteforce()
                input("\nPress Enter to continue...")
                
            elif choice == "5":
                self.typewriter("\n[!] Wiping traces...", color="yellow")
                time.sleep(2)
                self.typewriter("[+] Session terminated", color="red")
                break
                
            else:
                self.typewriter("\n[!] Module under development", color="yellow")
                time.sleep(1)

if __name__ == "__main__":
    try:
        tool = WhatsAppHacker()
        tool.run()
    except KeyboardInterrupt:
        print("\n\033[31m[!] Emergency exit triggered\033[0m")
