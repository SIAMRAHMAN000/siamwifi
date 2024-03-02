import os
import time
import random
import subprocess

# ANSI color escape codes
CYAN = '\033[96m'
RESET_COLOR = '\033[0m'  # Reset color to default

def check_dependencies():
    dependencies = ["root-repo", "git", "tsu", "python", "wpa-supplicant", "pixiewps", "iw"]
    missing_dependencies = []
    for dependency in dependencies:
        try:
            subprocess.run(["which", dependency], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            missing_dependencies.append(dependency)
    return missing_dependencies

def install_dependencies(dependencies):
    for dependency in dependencies:
        if dependency == "root-repo":
            os.system("sudo apt-get install root-repo -y")
        elif dependency == "git":
            os.system("sudo apt-get install git -y")
        elif dependency == "tsu":
            os.system("sudo apt-get install tsu -y")
        elif dependency == "python":
            os.system("sudo apt-get install python -y")
        elif dependency == "wpa-supplicant":
            os.system("sudo apt-get install wpa-supplicant -y")
        elif dependency == "pixiewps":
            os.system("sudo apt-get install pixiewps -y")
        elif dependency == "iw":
            os.system("sudo apt-get install iw -y")

def crack_wifi():
    os.system("sudo python cracker.py -i wlan0 --iface-down -K")

def main_menu():
    banner = f"""
{CYAN}
  ██████  ██▓ ▄▄▄       ███▄ ▄███▓    █     █░ ██▓  █████▒██▓
▒██    ▒ ▓██▒▒████▄    ▓██▒▀█▀ ██▒   ▓█░ █ ░█░▓██▒▓██   ▒▓██▒
░ ▓██▄   ▒██▒▒██  ▀█▄  ▓██    ▓██░   ▒█░ █ ░█ ▒██▒▒████ ░▒██▒
  ▒   ██▒░██░░██▄▄▄▄██ ▒██    ▒██    ░█░ █ ░█ ░██░░▓█▒  ░░██░
▒██████▒▒░██░ ▓█   ▓██▒▒██▒   ░██▒   ░░██▒██▓ ░██░░▒█░   ░██░
▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░░ ▒░   ░  ░   ░ ▓░▒ ▒  ░▓   ▒ ░   ░▓  
░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░░  ░      ░     ▒ ░ ░   ▒ ░ ░      ▒ ░
░  ░  ░   ▒ ░  ░   ▒   ░      ░        ░   ░   ▒ ░ ░ ░    ▒ ░
      ░   ░        ░  ░       ░          ░     ░          ░  
                                                             
{RESET_COLOR}
"""
    while True:
        print(banner)
        print("\nPlease select an option:")
        print(f"{CYAN}[1]{RESET_COLOR} {CYAN}Crack WiFi{RESET_COLOR}")
        print(f"{CYAN}[2]{RESET_COLOR} {CYAN}Exit{RESET_COLOR}")
        choice = input(f"{CYAN}Enter your choice: {RESET_COLOR}")

        if choice == '1':
            missing_dependencies = check_dependencies()
            if missing_dependencies:
                print("Missing dependencies: ", ", ".join(missing_dependencies))
                install_dependencies(missing_dependencies)
            os.system('clear') 
            time.sleep(1)
            crack_wifi()
        elif choice == '2':
            print("Byeee...")
            break
        else:
            for _ in range(1):
                time.sleep(0.5)
            time.sleep(0.5)
            os.system('clear') 

if __name__ == "__main__":
    main_menu()
