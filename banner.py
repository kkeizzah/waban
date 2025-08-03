#!/usr/bin/env python3
import os
import random
import time
import socket
from datetime import datetime
import re
import sys
import threading
import subprocess

class WhatsAppHacker:
    def __init__(self):
        self.session_id = f"KTH-{random.randint(1000, 9999)}-{random.randint(100,999)}"
        self.target_number = ""
        self.version = "v4.2.1"
        self.author = "NULLSEC"
        self.country_code = "+1"
        self.db_loaded = False
        self.wordlist = []
        self.cmatrix_running = False
        self.stop_cmatrix = False
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def typewriter(self, text, delay=0.03, color=None, end="\n"):
        color_codes = {
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "bold": "\033[1m",
            "underline": "\033[4m"
        }
        
        if color in color_codes:
            print(color_codes[color], end='', flush=True)
            
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
            
        print("\033[0m", end='', flush=True)  # Reset color
        print(end=end)
        
    def validate_whatsapp_number(self, number):
        """Simulate number validation"""
        pattern = r"^\+?[0-9]{10,15}$"
        return re.match(pattern, number)
        
    def load_wordlist(self):
        """Fake wordlist loading"""
        if not self.db_loaded:
            self.typewriter("[+] Connecting to NULLSEC underground database...", color="cyan", delay=0.01)
            self.simulate_loading("Establishing TOR connection", 2)
            self.typewriter(f"[+] Routing through {random.randint(3,7)} TOR nodes...", color="yellow", delay=0.01)
            time.sleep(1.5)
            
            self.typewriter("[+] Loading rainbow tables...", color="yellow", delay=0.01)
            self.simulate_loading("Decrypting password hashes", 3)
            
            self.wordlist = [
                "password", "123456", "qwerty", "iloveyou", 
                "admin", "welcome", self.target_number[-6:],
                f"wa{random.randint(1000,9999)}", "root123", "pass123"
            ]
            self.db_loaded = True
            self.typewriter(f"[+] Loaded {len(self.wordlist)} common passwords + {random.randint(500,1500)} leaked hashes", color="green")
            time.sleep(1)
        
    def simulate_loading(self, message, duration):
        end_time = time.time() + duration
        symbols = ["/", "-", "\\", "|"]
        i = 0
        
        print(f"[{symbols[i]}] {message}", end='', flush=True)
        
        while time.time() < end_time:
            i = (i + 1) % len(symbols)
            print(f"\r[{symbols[i]}] {message}", end='', flush=True)
            time.sleep(0.1)
            
        print("\r[✓] " + message)
        
    def run_cmatrix(self):
        """Run cmatrix in the background"""
        if not self.cmatrix_running:
            self.cmatrix_running = True
            self.stop_cmatrix = False
            try:
                # Run cmatrix in a subprocess
                self.cmatrix_proc = subprocess.Popen(
                    ["cmatrix", "-ab"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                
                # Wait until we need to stop it
                while not self.stop_cmatrix:
                    time.sleep(0.1)
                    
            except FileNotFoundError:
                self.typewriter("[!] cmatrix not found - continuing without visual effects", color="yellow")
            finally:
                self.cmatrix_running = False
                
    def stop_cmatrix_background(self):
        """Stop the cmatrix process"""
        if self.cmatrix_running:
            self.stop_cmatrix = True
            if hasattr(self, 'cmatrix_proc'):
                self.cmatrix_proc.terminate()
                try:
                    self.cmatrix_proc.wait(timeout=1)
                except subprocess.TimeoutExpired:
                    self.cmatrix_proc.kill()
                    
    def fake_bruteforce(self):
        """Simulate password cracking with more realistic output"""
        self.load_wordlist()
        
        self.typewriter(f"\n[+] Initializing attack on target: {self.target_number}", color="red")
        self.typewriter("[+] Spoofing MAC address...", color="yellow")
        self.typewriter(f"[+] MAC: {':'.join(f'{random.randint(0,255):02x}' for _ in range(6))}", color="cyan")
        time.sleep(1.5)
        
        self.typewriter("\n[+] Bypassing WhatsApp end-to-end encryption...", color="yellow")
        self.simulate_loading("Exploiting CVE-2023-4863", 3)
        
        self.typewriter("[+] Establishing MITM position...", color="yellow")
        self.typewriter(f"[+] Using {random.choice(['CoffeeMiner', 'wifiphisher', 'airgeddon'])} framework", color="cyan")
        time.sleep(2)
        
        print("\n[PROGRESS]:")
        for i in range(1, 101):
            time.sleep(0.03 * random.random())
            # Simulate occasional "hacking" messages
            if i % 15 == 0:
                attacks = [
                    "Injecting SQL payload",
                    "Bypassing 2FA",
                    "Cracking AES-256",
                    "Decrypting message store",
                    "Intercepting OTP"
                ]
                print(f"\n\033[33m[!] {random.choice(attacks)}...\033[0m")
                
            print(f"\r\033[35m[{'█'*(i//2)}{'░'*(50-(i//2))}] {i}%", end='', flush=True)
            
        print("\n\n[+] Analyzing results...")
        time.sleep(2)
        
        if random.random() > 0.7:  # 30% success rate
            password = random.choice(self.wordlist)
            self.typewriter(f"\n[SUCCESS] Found credentials:", color="bold")
            self.typewriter(f"   Phone: {self.target_number}", color="green")
            self.typewriter(f"   Password: {password}", color="green")
            self.typewriter(f"   Session key: WA-{random.randint(100000,999999)}", color="green")
            self.typewriter(f"   Last login: {random.randint(1,28)}/{random.randint(1,12)}/202{random.randint(3,5)}", color="green")
            
            self.typewriter("\n[+] Downloading message database...", color="yellow")
            self.simulate_loading("Extracting chat history", 3)
            self.typewriter(f"[+] Retrieved {random.randint(15,150)} messages", color="green")
        else:
            self.typewriter("\n[FAILED] Exploit unsuccessful", color="red")
            self.typewriter("[!] Target may have 2FA enabled", color="yellow")
            self.typewriter("[!] Triggering anti-forensic wipe...", color="red")
            time.sleep(1)
        
    def sim_clone_attack(self):
        """Simulate SIM cloning attack"""
        self.clear_screen()
        self.show_banner()
        
        self.typewriter("\n[+] SIM CLONE ATTACK MODULE", color="red")
        self.typewriter("[!] Warning: This operation may be illegal in your country", color="yellow")
        
        if not self.target_number:
            self.typewriter("[!] No target number set", color="red")
            time.sleep(1)
            return
            
        self.typewriter(f"\n[+] Targeting: {self.target_number}", color="cyan")
        self.typewriter("[+] Scanning for nearby cell towers...", color="yellow")
        self.simulate_loading("Triangulating position", 2)
        
        carriers = ["Verizon", "T-Mobile", "AT&T", "Vodafone", "Orange"]
        self.typewriter(f"[+] Carrier identified: {random.choice(carriers)}", color="green")
        time.sleep(1)
        
        self.typewriter("\n[+] Exploiting SS7 vulnerability...", color="yellow")
        self.simulate_loading("Intercepting SMS messages", 3)
        
        self.typewriter("[+] Cloning SIM parameters...", color="yellow")
        print("\n[PROGRESS]:")
        for i in range(1, 101):
            time.sleep(0.04 * random.random())
            print(f"\r\033[36m[{'█'*(i//2)}{'▒'*(50-(i//2))}] {i}%", end='', flush=True)
            
        print("\n")
        if random.random() > 0.5:
            self.typewriter("\n[SUCCESS] SIM cloned successfully!", color="green")
            self.typewriter(f"[+] IMSI: {random.randint(310000000000000,310999999999999)}", color="cyan")
            self.typewriter(f"[+] ICCID: 89{random.randint(10,99)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(0,9)}", color="cyan")
            self.typewriter("[+] You can now receive SMS messages for this number", color="green")
        else:
            self.typewriter("\n[FAILED] SIM cloning unsuccessful", color="red")
            self.typewriter("[!] Target may be using modern SIM with encryption", color="yellow")
        
    def message_interception(self):
        """Simulate message interception"""
        self.clear_screen()
        self.show_banner()
        
        self.typewriter("\n[+] MESSAGE INTERCEPTION MODULE", color="red")
        
        if not self.target_number:
            self.typewriter("[!] No target number set", color="red")
            time.sleep(1)
            return
            
        self.typewriter(f"\n[+] Targeting: {self.target_number}", color="cyan")
        self.typewriter("[+] Activating silent SMS ping...", color="yellow")
        time.sleep(2)
        
        self.typewriter("[+] Target device is online", color="green")
        self.typewriter(f"[+] Approximate location: {random.randint(30,45)}.{random.randint(100000,999999)}, -{random.randint(70,120)}.{random.randint(100000,999999)}", color="cyan")
        time.sleep(1)
        
        self.typewriter("\n[+] Intercepting messages...", color="yellow")
        self.typewriter("[+] Press Ctrl+C to stop interception", color="red")
        
        try:
            messages = [
                "Hey, are we still meeting tomorrow?",
                "Your OTP is 784592 - expires in 5 minutes",
                "Mom: Call me when you get this",
                "Your package has been delivered",
                "Alex: Did you see the news?",
                "Security alert: New login from Android device",
                "Your Netflix subscription is due for renewal"
            ]
            
            start_time = time.time()
            while time.time() - start_time < 10:  # Run for 10 seconds
                time.sleep(random.uniform(1, 3))
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"\033[33m[{timestamp}] New message: \033[32m{random.choice(messages)}\033[0m")
                
        except KeyboardInterrupt:
            self.typewriter("\n[+] Stopping interception...", color="yellow")
            
        self.typewriter("\n[+] Captured messages saved to /tmp/.wa_logs", color="green")
        
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
        print(f"\033[36mHost: {self.hostname} ({self.ip_address}) | Threads: {random.randint(1,16)}\033[0m")
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
        try:
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
                        
                    # Start cmatrix in background
                    cmatrix_thread = threading.Thread(target=self.run_cmatrix)
                    cmatrix_thread.daemon = True
                    cmatrix_thread.start()
                    
                    self.clear_screen()
                    self.show_banner()
                    self.fake_bruteforce()
                    
                    # Stop cmatrix
                    self.stop_cmatrix_background()
                    input("\nPress Enter to continue...")
                    
                elif choice == "3":
                    if not self.target_number:
                        self.typewriter("[!] No target number set", color="red")
                        time.sleep(1)
                        continue
                        
                    # Start cmatrix in background
                    cmatrix_thread = threading.Thread(target=self.run_cmatrix)
                    cmatrix_thread.daemon = True
                    cmatrix_thread.start()
                    
                    self.sim_clone_attack()
                    
                    # Stop cmatrix
                    self.stop_cmatrix_background()
                    input("\nPress Enter to continue...")
                    
                elif choice == "4":
                    if not self.target_number:
                        self.typewriter("[!] No target number set", color="red")
                        time.sleep(1)
                        continue
                        
                    # Start cmatrix in background
                    cmatrix_thread = threading.Thread(target=self.run_cmatrix)
                    cmatrix_thread.daemon = True
                    cmatrix_thread.start()
                    
                    self.message_interception()
                    
                    # Stop cmatrix
                    self.stop_cmatrix_background()
                    input("\nPress Enter to continue...")
                    
                elif choice == "5":
                    self.typewriter("\n[!] Wiping traces...", color="yellow")
                    self.simulate_loading("Overwriting logs", 2)
                    self.typewriter("[+] Session terminated", color="red")
                    self.typewriter("[+] All connections closed", color="green")
                    break
                    
                else:
                    self.typewriter("\n[!] Invalid option", color="red")
                    time.sleep(1)

        except KeyboardInterrupt:
            self.stop_cmatrix_background()
            self.typewriter("\n\n[!] Emergency exit triggered - activating cleanup", color="red")
            self.simulate_loading("Destroying evidence", 2)
            sys.exit(0)

if __name__ == "__main__":
    try:
        tool = WhatsAppHacker()
        tool.run()
    except KeyboardInterrupt:
        print("\n\033[31m[!] Emergency exit triggered\033[0m")
