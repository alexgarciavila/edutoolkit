import os
import ctypes
import platform
import sys
import subprocess
import shutil

class NetworkModule():

    def __init__(self):
        
        utils = UtilsModule()
        osname = utils.check_os()
        utils.check_admin(osname)
        utils.clear_screen(osname)

        if (osname == "Darwin"):
            print("\nSistema operatiu detectat: MacOS\n")
        elif (osname == "Windows"):
            print("\nSistema operatiu detectat: Microsoft {0}\n" .format(platform.system()))
        elif osname == "Linux":
            print("\nSistema operatiu detectat: {0}\n" .format(platform.uname().system))
        else:
            print("\nSistema operatiu no identificat\n")
        
        self.select_dns_server(osname)

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
        self.clearing_dns_cache_win()
    
    def clearing_dns_cache_win(self):
        print("Buidant la memòria cau de les DNS")
        subprocess.call("ipconfig /flushdns")
    
    def change_dns_mac(self):
        subprocess.call("networksetup -setdnsservers Wi-Fi 208.67.222.222")

    def check_exist_netsh(self):
        if shutil.which("netsh"):
            self.select_dns_server()
        else:
            print("No existeix la comanda netsh")
    
    def select_dns_server(self, osname):
        print(osname)
        print("\n¿Quines DNS vols posar?")
        print("--------------------------------------------")
        print("1. Cloudflare (1.1.1.1 - 1.0.0.1)")		
        print("2. Google (8.8.8.8 - 8.8.4.4)")
        print("3. OpenDNS (208.67.222.222 - 208.67.220.220)")
        print("4. DNS per DHCP")
        print("5. DNS Manuals")
        print("--------------------------------------------")
        print("6. Cancelar\n")
        
        while True:
            choice_options={
                "1": ["CloudFlare","1.1.1.1","1.0.0.1"],
                "2" : ["Google","8.8.8.8","8.8.4.4"],
                "3" : ["OpenDNS","208.67.222.222","208.67.220.220"],
                "4" : "dhcp",
                "5" : ["Manual"],
                "6" : ["Cancelar"]
                }
        
            choice = input("Selecciona l'opció desitjada [1-6]")
            print("Ha seleccionat: ", choice_options[choice][0])
            print("DNS Primaria: ", choice_options[choice][1])
            print("DNS Secundaria: ", choice_options[choice][2])
            input("Pause..............")
        
        #self.change_dns_win()

class UtilsModule():

    def check_os(self):
        return platform.system()

    def clear_screen(self, osname):
        if osname == "Windows":
            subprocess.call("cls", shell=True)
        else:
        # Linux or MacOS
            subprocess.call("clear", shell=True)

    def check_admin(self, osname):
        if (osname == "Windows"):
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:
        # Linux or MacOS
            is_admin = os.getuid() == 0
        
        if (is_admin == False):
            self.clear_screen(osname)
            print("\n------------------------------------------------------")
            print ("Executa el programa amb drets d'Administrador. Gràcies")
            print("------------------------------------------------------\n")
            sys.exit()