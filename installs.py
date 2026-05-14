import os
import sys
import time
import subprocess

G, C, W, R, Y = '\033[92m', '\033[96m', '\033[0m', '\033[91m', '\033[93m'

def clear():
    os.system('clear')

def abdul_mateen_banner():
    clear()
    print(f"""{C}
    ###########################################################################
    #                                                                         #
    #      █████╗ ██████╗ ██████╗ ██╗   ██╗██╗         ███╗   ███╗███╗   ██╗    #
    #     ██╔══██╗██╔══██╗██╔══██╗██║   ██║██║         ████╗ ████║████╗  ██║    #
    #     ███████║██████╔╝██║  ██║██║   ██║██║         ██╔████╔██║██╔██╗ ██║    #
    #     ██╔══██║██╔══██╗██║  ██║██║   ██║██║         ██║╚██╔╝██║██║╚██╗██║    #
    #     ██║  ██║██████╔╝██████╔╝╚██████╔╝███████╗    ██║ ╚═╝ ██║██║ ╚████║    #
    #     ╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═══╝    #
    #                                                                         #
    #   {G}---       VIP TOOL INSTALLER | ELITE EVIL-TWIN SETUP        ---{C}    #
    #   {W}---           DEVELOPER & TECHNICIAN: ABDUL MATEEN           ---{C}    #
    #                                                                         #
    ###########################################################################{W}
    """)

def run_install():
    if os.getuid() != 0:
        print(f"{R}[!] ERROR: Run with 'sudo'{W}")
        sys.exit(1)

    abdul_mateen_banner()
    print(f"{Y}[*] Initializing Elite Setup...{W}")
    time.sleep(1)

    tools = [
        "aircrack-ng", "airgeddon", "xterm", "dnsmasq", "hostapd", 
        "lighttpd", "php-cgi", "macchanger", "reaver", "pixiewps", 
        "bully", "python3-pip", "git", "curl"
    ]

    print(f"{C}[+] Updating Repositories...{W}")
    subprocess.run(["sudo", "apt", "update", "-y"], capture_output=False)

    for tool in tools:
        print(f"{Y}[*] Installing: {tool}{W}")
        subprocess.run(["sudo", "apt", "install", tool, "-y"])
    
    # Updated filename with Capital M
    target_script = "Mateen's script.py"
    
    if os.path.exists(target_script):
        script_path = os.path.abspath(target_script)
        os.chmod(script_path, 0o755)
        print(f"{G}[+] Permissions set for {target_script}{W}")
    else:
        print(f"{R}[!] Warning: {target_script} not found in this folder!{W}")

    abdul_mateen_banner()
    print(f"{G}SUCCESS: Setup Completed.{W}")
    print(f"\n{Y}[>] Launch: {C}sudo python3 \"{target_script}\"{W}\n")

if __name__ == "__main__":
    try:
        run_install()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped by user.{W}")
        sys.exit()