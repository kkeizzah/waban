#!/usr/bin/env python3
import os
import random
import time
import socket
from datetime import datetime

class KeithKill:
    def __init__(self):
        self.session_id = random.randint(1000, 9999)
        self.target_ip = "192.168.1.1"  # Default target
        self.version = "v2.4.1"
        self.author = "NULLSEC"
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def typewriter(self, text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        
    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
        
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
        print(f"\033[1;31m>> ADVANCED PENETRATION FRAMEWORK {self.version} <<\033[0m")
        print(f"\033[33mSession ID: {self.session_id} | Local IP: {self.get_local_ip()}\033[0m")
        print(f"\033[36mCurrent Target: {self.target_ip} | User: {os.getlogin()}\033[0m")
        print("\033[34m" + "="*60 + "\033[0m")
        
    def fake_scan(self):
        self.typewriter("\n[+] Initializing vulnerability scan...")
        time.sleep(1)
        
        for i in range(1, 6):
            ip_part = ".".join(str(random.randint(1, 255)) for _ in range(4))
            port = random.randint(1, 65535)
            print(f"\033[33m[→] Scanning {ip_part}:{port} ", end='', flush=True)
            time.sleep(0.3)
            print("\033[32m[OPEN]\033[0m" if random.random() > 0.7 else "\033[31m[CLOSED]\033[0m")
            time.sleep(0.2)
            
        print("\n\033[35m[!] 3 potential vulnerabilities found\033[0m")
        
    def show_menu(self):
        self.show_banner()
        print("\n\033[1mMAIN MENU:\033[0m")
        print("1. Target Configuration")
        print("2. Vulnerability Scan")
        print("3. Exploit Toolkit")
        print("4. Network Sniffer")
        print("5. Exit")
        
        choice = input("\n\033[35m[?] Select option: \033[0m")
        return choice
        
    def run(self):
        while True:
            choice = self.show_menu()
            
            if choice == "1":
                self.target_ip = input("\n[+] Enter target IP: ")
                print(f"\033[32m[+] Target set to {self.target_ip}\033[0m")
                time.sleep(1)
                
            elif choice == "2":
                self.fake_scan()
                input("\nPress Enter to continue...")
                
            elif choice == "5":
                print("\n\033[31m[!] Terminating session...\033[0m")
                time.sleep(1)
                break
                
            else:
                print("\n\033[31m[!] Module not implemented yet\033[0m")
                time.sleep(1)

if __name__ == "__main__":
    try:
        tool = KeithKill()
        tool.run()
    except KeyboardInterrupt:
        print("\n\033[31m[!] Session terminated by user\033[0m")
