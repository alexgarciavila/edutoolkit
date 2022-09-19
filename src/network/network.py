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
            print("\n   Sistema operatiu detectat: MacOS\n")
        elif (osname == "windows"):
            print("\n   Sistema operatiu detectat: Microsoft {0}\n" .format(platform.system()))
        elif osname == "Linux":
            print("\n   Sistema operatiu detectat: {0}\n" .format(platform.uname().system))
        else:
            print("\nSistema operatiu no identificat\n")
        
        self.select_dns_server(osname, utils)
        utils.exit_program()

    def change_dns_windows(self, choice_options, choice):
        print("   DNS Actuals:")
        print("   ---------------")
        ipconfigall = subprocess.check_output('ipconfig /all', text=True)
        lines = ipconfigall.split("\n")
        primary_dns = "   " + lines[22][-15:]
        print(primary_dns)
        secondary_dns = "   " + lines[23][-15:]
        print(secondary_dns)
        print("   ---------------\n")
        print("   - Canviant les DNS...")
        subprocess.call("netsh interface ip set dns \"Ethernet\" static " + choice_options[choice][1] + " primary", stdout=False)
        subprocess.call("netsh interface ip add dns \"Ethernet\" addr=" + choice_options[choice][2] + " index=2", stdout=False)
        print("\n   Noves DNS:")
        print("   ---------------")
        ipconfigall = subprocess.check_output('ipconfig /all', text=True)
        lines = ipconfigall.split("\n")
        primary_dns = "   " + lines[22][-15:]
        print(primary_dns)
        secondary_dns = "   " + lines[23][-15:]
        print(secondary_dns)
        print("   ---------------\n")
        self.clearing_dns_cache_windows()
    
    def clearing_dns_cache_windows(self):
        print("   - Buidant la memòria cau de les DNS\n")
        try:
            subprocess.call("ipconfig /flushdns", stdout=subprocess.DEVNULL)
            print("   - Memòria cau buidada correctament\n")
        except:
            print("   - Error en buidar la memòria cau\n")
    
    def change_dns_mac(self):
        subprocess.call("networksetup -setdnsservers Wi-Fi 208.67.222.222")

    def check_exist_netsh(self):
        if shutil.which("netsh"):
            self.select_dns_server()
        else:
            print("No existeix la comanda netsh")
    
    def select_dns_server(self, osname, utils):
        print("\n   ¿Quines DNS vols posar?")
        print("   --------------------------------------------")
        print("   1. Cloudflare (1.1.1.1 - 1.0.0.1)")		
        print("   2. Google (8.8.8.8 - 8.8.4.4)")
        print("   3. OpenDNS (208.67.222.222 - 208.67.220.220)")
        print("   4. DNS per DHCP")
        print("   5. DNS Manuals")
        print("   --------------------------------------------")
        print("   6. Cancelar\n")
        
        while True:
       
            choice = input("   Selecciona l'opció desitjada [1-6]\n   > ")
            
            if choice not in list(map(str, list(range(1, 6 + 1)))):
                continue
            choice = int(choice)
            break

        choice_options={
            1 : ["CloudFlare","1.1.1.1","1.0.0.1", "self.change_dns_" + osname],
            2 : ["Google","8.8.8.8","8.8.4.4", "self.change_dns_" + osname],
            3 : ["OpenDNS","208.67.222.222","208.67.220.220", "self.change_dns_" + osname],
            4 : ["DHCP","","", "self.change_dns_" + osname],
            5 : ["Manual","","", "self.change_dns_" + osname],
            6 : ["Cancelar","Sense canvis","Sense canvis", "utils.exit_program"]
            }
            
        print("\n   Ha seleccionat: ", choice_options[choice][0])
        print("   DNS Primaria: ", choice_options[choice][1])
        print("   DNS Secundaria: ", choice_options[choice][2], "\n")
        
        # Check method to use, stored in dictionary "choice_options" in position 3
        if (choice == 6):
            eval(choice_options[choice][3] + "()")
        else:   
            eval(choice_options[choice][3] + "(choice_options, choice)")

class UtilsModule():

    def check_os(self):
        return platform.system().lower()

    def clear_screen(self, osname):
        if osname == "windows":
            subprocess.call("cls", shell=True)
        else:
        # Linux or MacOS
            subprocess.call("clear", shell=True)

    def check_admin(self, osname):
        if (osname == "windows"):
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:
        # Linux or MacOS
            is_admin = os.getuid() == 0
        
        if (is_admin == False):
            self.clear_screen(osname)
            print("\n   ------------------------------------------------------")
            print ("   Executa el programa amb drets d'Administrador. Gràcies")
            print("   ------------------------------------------------------\n")
            self.exit_program()

    def exit_program(self):
        print("\n   Que la força t'acompanyi...\n\n")
        input("   Prem qualsevol tecla per tancar el programa")
        sys.exit()