import os
import platform
#import wmi
import time
import subprocess
import shutil

class NetworkModule():
    def change_dns_win():
        #os.system("netsh interface ip set dns \"Ethernet\" static 8.8.8.8")
        subprocess.call("netsh interface ip set dns \"Ethernet\" static 8.8.8.8 primary")
        subprocess.call("netsh interface ip add dns \"Ethernet\" addr=8.8.4.4 index=2")
    def check_exist_netsh():
        if shutil.which("netsh"):
            NetworkModule.select_dns_server()
        else:
            print("No existeix la comanda netsh")
    
    def select_dns_server():
        subprocess.call("cls", shell=True)
        print("\n¿Quines DNS vols posar?")
        print("--------------------------------------------")
        print("1. Cloudflare (1.1.1.1 - 0.0.0.0)")		
        print("2. Google (8.8.8.8 - 8.8.4.4)")
        print("3. OpenDNS (208.67.222.222 - 208.67.220.220)")
        print("4. DNS per DHCP")
        print("5. DNS Manuals")
        print("--------------------------------------------")
        print("6. Cancelar\n")
