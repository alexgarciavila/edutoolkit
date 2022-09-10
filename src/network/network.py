import os
import platform
#import wmi
import time
import subprocess
import shutil

class NetworkModule():

    def __init__(self):
        subprocess.call("cls", shell=True)
        osname = self.check_os()
        if osname == "Darwin":
            print("Sistema operatiu MAC")
        elif osname == "Windows":
            print("Sistema operatiu detectat: Microsoft {0} {1} {2}" .format(platform.system(), platform.release(), platform.win32_edition()))
            self.select_dns_server()
        elif osname == "Linux":
            print("Sistema operatiu Linux")
        else:
            print("Sistema operatiu no identificat")

    def check_os(self):
        return platform.system()

    def change_dns_win(self):
        subprocess.call("netsh interface ip set dns \"Ethernet\" static 8.8.8.8 primary")
        subprocess.call("netsh interface ip add dns \"Ethernet\" addr=8.8.4.4 index=2")
    
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
