import os
import ctypes
import platform
import sys
import subprocess

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
        input("   Prem qualsevol tecla per tancar el programa\n")
        sys.exit()