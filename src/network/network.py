import os
import platform
#import wmi
import time
import subprocess
import shutil

class NetworkModule():

    def __init__(self):
        
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

    def change_dns_win(self):
        print("DNS Actuals:")
        print("--------------------------------------------------")
        subprocess.call("netsh interface ipv4 show dnsservers \"Ethernet\"")
        print("--------------------------------------------------")
        subprocess.call("netsh interface ip set dns \"Ethernet\" static 1.1.1.1 primary")
        subprocess.call("netsh interface ip add dns \"Ethernet\" addr=1.0.0.1 index=2")
        print("DNS Canviades:")
        print("--------------------------------------------------")
        subprocess.call("netsh interface ipv4 show dnsservers \"Ethernet\"")
        print("--------------------------------------------------")
    
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
