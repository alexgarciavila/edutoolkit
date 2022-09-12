import os
import ctypes
import platform
import sys
import re
#import wmi
import time
import subprocess
import shutil

class NetworkModule():

    def __init__(self):
        
        self.check_admin()
        osname = self.check_os()
        if osname == "Darwin":
            print("Sistema operatiu detectat: MacOS")
        elif osname == "Windows":
            subprocess.call("cls", shell=True)
            print("Sistema operatiu detectat: Microsoft {0} {1}" .format(platform.system(), platform.release()))
            self.select_dns_server()
            self.change_dns_win()
        elif osname == "Linux":
            subprocess.call("clear", shell=True)
            print("Sistema operatiu detectat: {0}" .format(platform.uname().system))
        else:
            print("Sistema operatiu no identificat")

    def check_os(self):
        return platform.system()

    def check_admin(self):
        try:
            # Linux
            is_admin = os.getuid() == 0
        except AttributeError:
            # Windows
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if (is_admin == False):
            subprocess.call("cls", shell=True)
            print ("Executa el programa amb drets d'Administrador. Gràcies")
            sys.exit()



    def change_dns_win(self):
        print("DNS Actuals:")
        print("--------")
        ipconfigall = subprocess.check_output('ipconfig /all').decode(sys.stdout.encoding)
        lines = ipconfigall.split("\n")
        primary_dns = lines[22][-8:]
        print(primary_dns)
        secondary_dns = lines[23][-8:]
        print(secondary_dns)
        print("--------")
        print("Canviant les DNS...")
        subprocess.call("netsh interface ip set dns \"Ethernet\" static 1.1.1.1 primary")
        subprocess.call("netsh interface ip add dns \"Ethernet\" addr=1.0.0.1 index=2")
        print("DNS Canviades:")
        print("--------")
        ipconfigall = subprocess.check_output('ipconfig /all').decode(sys.stdout.encoding)
        lines = ipconfigall.split("\n")
        dns1 = lines[22][-8:]
        print(dns1)
        dns2 = lines[23][-8:]
        print(dns2)
        print("--------")
        self.clearing_dns_cache()
    
    def clearing_dns_cache(self):
        print("Buidant la memòria cau de les DNS")
        subprocess.call("ipconfig /flushdns")
    
    def change_dns_mac(self):
        subprocess.call("networksetup -setdnsservers Wi-Fi 208.67.222.222")

    def check_exist_netsh(self):
        if shutil.which("netsh"):
            self.select_dns_server()
        else:
            print("No existeix la comanda netsh")
    
    def select_dns_server(self):
        print("\n¿Quines DNS vols posar?")
        print("--------------------------------------------")
        print("1. Cloudflare (1.1.1.1 - 1.0.0.1)")		
        print("2. Google (8.8.8.8 - 8.8.4.4)")
        print("3. OpenDNS (208.67.222.222 - 208.67.220.220)")
        print("4. DNS per DHCP")
        print("5. DNS Manuals")
        print("--------------------------------------------")
        print("6. Cancelar\n")
