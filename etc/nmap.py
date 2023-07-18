import sys
import os
import time
import signal
import random
from time import sleep
from sys import argv
from platform import system


def sigint_handler(signum, frame):
    print(" [-] Keyboard Interrupt! Terminaling!")
    sys.exit()


class bcolors:
        OKGREEN = '\033[92m'
        WARNING = '\033[0;33m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        LITBU = '\033[94m'
        YELLOW = '\033[3;33m'
        CYAN = '\033[0;36'
        colors = ['\033[91m', '\033[0;33m']
        RAND = random.choice(colors)


signal.signal(signal.SIGINT, sigint_handler)

def logo():
    print(bcolors.RAND + """
███▄ ▄███▓▓██   ██▓ ████     █  ███▄ ▄███▓ ▄▄▄       ██▓███
▓██▒▀█▀ ██▒ ▒██  ██▒ ██▀██   █ ▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒
▓██    ▓██░  ▒██ ██░▓██  ▀█ ██▒▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒
▒██    ▒██   ░ ▐██▓░▓██▒  █▌██▒▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒
▒██▒   ░██▒  ░ ██▒▓░▒██░   ▓██░▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░
░ ▒░   ░  ░   ██▒▒▒ ░ ▒░   ▒ ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░
░  ░      ░ ▓██ ░▒░ ░ ░░   ░ ▒░░  ░      ░  ▒   ▒▒ ░░▒ ░
░      ░    ▒ ▒ ░░     ░   ░ ░ ░      ░     ░   ▒   ░░
       ░    ░ ░              ░        ░         ░  ░
            ░ ░

┌───────────────────────────────────────────────────────────►
| Developer: mishakorzhik
└───────────────────────────────────────► Version: 1.1.0 \033[1;m
""")

def menu():
    logo()
    print("""  01] Default Scan
  02] Host Discovery
  03] Port(SYN) Scan
  04] Port(TCP) Scan
  05] Port(UDP) Scan
  06] Port Definition 
  07] Ping Scanner
  08] Scan and detect Server/Daemon
  09] Scan a host protected by firewall
  10] Scan a firewall for MAC address spoofing
  11] Dns Brute force
  12] Service and Version Discovery
  13] OS Analysis and Version Discovery
  14] Nmap Script Engineering
  15] About Utility
  00] Exit Utility
        """)
    

def baslangic():
    os.system("clear")
    menu()

    op = input("  Diya: ")

    if op == "1" or op == "01":
        print(" Starting Default Scan (--reason <text> -oN <text>)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        birhedef = input(" While your IP: ")
        os.system("nmap --reason -d "+birhedef+" -oN "+birhedef)
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimbir = input("Option: ")
        if secimbir == "1":
            baslangic()
        if secimbir == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if op == "2" or op == "02":
        print(" Starting Host Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        ikihedef = input(" While your IP: ")
        os.system("nmap -Pn "+ikihedef+" -oN "+ikihedef)
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimiki = input("Option: ")
        if secimiki == "1":
            baslangic()
        if secimiki == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    
    if op == "3" or op == "03":
        print(" Starting Port(SYN) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        uchedef = input(" While your IP:  ")
        os.system("nmap -sS "+uchedef+" -oN "+uchedef)
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimuc = input("Option: ")
        if secimuc == "1":
            baslangic()
        if secimuc == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    
    if op == "4" or op == "04":
        print(" Starting Port(TCP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        dorthedef = input(" While your IP: ")
        os.system("nmap –sT "+dorthedef+" -oN "+dorthedef)
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimdort = input("Option: ")
        if secimdort == "1":
            baslangic()
        if secimdort == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    
    if op == "5" or op == "05":
        print(" Starting Port(UDP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        beshedef = input(" While your IP: ")
        os.system("nmap –sU "+beshedef+" -oN "+beshedef+".txt")
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimbes = input("Option: ")
        if secimbes == "1":
            baslangic()
        if secimbes == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()


    if op == "6" or op == "06":
        print(" Starting Port Definition (-sS -F)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        altihedef = input(" While your IP: ")
        os.system("nmap -sS -F "+altihedef+" -oN "+altihedef+".txt")
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimalti = input("Option: ")
        if secimalti == "1":
            baslangic()
        if secimalti == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()


    if op == "7" or op == "07":
        print(" Starting Ping Scanner (-sn)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: 142.250.201.206")
        altihedef = input(" While your IP: ")
        os.system("nmap -sn "+altihedef)
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimalti = input("Option: ")
        if secimalti == "1":
            baslangic()
        if secimalti == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if op == "8" or op == "08":
        print("  Scan and detect Server/Daemon (-PN)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        ultifhedef = input(" While your IP: ")
        os.system("nmap -PN "+ultifhedef)
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimayto = input("Option: ")
        if secimayto == "1":
            baslangic()
        if secimayto == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if op == "9" or op == "09":
        print("  Starting scan a host protected by firewall (-sV)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        oiltefhedef = input(" While your IP: ")
        os.system("nmap -sV "+oiltefhedef)
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        yecimayto = input("Option: ")
        if yecimayto == "1":
            baslangic()
        if yecimayto == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if op == "10":
        print("  Starting scan A Firewall for MAC Address Spoofing (-v -sT -PN --spoof-mac 0)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        oilkoefhidef = input(" While your IP: ")
        os.system("nmap -v -sT -PN --spoof-mac 0 "+oilkoefhidef)
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        yecimayto0 = input("Option: ")
        if yecimayto0 == "1":
            baslangic()
        if yecimayto0 == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if op == "11":
        print("  Starting dns brute force (--script dns-brute)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        oilkoefh01idef = input(" While your IP: ")
        os.system("nmap --script dns-brute  "+oilkoefh01idef)
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        y0ecimayto0 = input("Option: ")
        if y0ecimayto0 == "1":
            baslangic()
        if y0ecimayto0 == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if op == "12":
        print(" Starting Service and Version Discovery (-sS -F <text> -oN <text>)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        yedihedef = input(" While your IP: ")
        os.system("nmap –sS -F "+yedihedef+" -oN "+yedihedef+".txt")
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimyedi = input("Option: ")
        if secimyedi == "1":
            baslangic()
        if secimyedi == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if op == "13":
        print("Starting OS Analysis and Version Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        sekizhedef = input(" While your IP:  ")
        os.system("nmap –sS -O "+sekizhedef+" -oN "+sekizhedef+".txt")
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimsekiz = input("Option: ")
        if secimsekiz == "1":
            baslangic()
        if secimsekiz == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()


    if op == "14":
        print(" Starting Nmap Script Engineering...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or: example.com")
        dokuzhedef = input(" While your IP:  ")
        os.system("nmap –sC "+dokuzhedef+" -oN "+dokuzhedef+".txt")
        print("\n \033[1;91m01] Back to Main Menu \n 02] Exit \033[1;m")
        secimdokuz = input("Option: ")
        if secimdokuz == "1":
            baslangic()
        if secimdokuz == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            os.system("clear")
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    if op == "15":
        print("[^_^] Tool Name: MyNmap v1.1.0")
        print("[^_^] Menu Type: About Utility!")
        print("")
        print("[>] Developer : misha korzhik                  ")
        print("[>] Company   : Flyzero copyring 2019          ")
        print("[>] Version   : Tool version 1.1.0             ")
        print("[>] Telegram  : @MishaKorzhikTelegram          ")
        print("[>] Github    : https://github.com/mishakorzik ")
        time.sleep(7)
        baslangic()
    if op == "0" or op == "00":
        print(" \033[1;91@[^_^] Bye Bye have a nice day!\033[1;m")
        sys.exit()

    else:
        print(" [0_0] Please enter one of the options in the menu. \n You are directed to the main menu.")
        time.sleep(0.5)
        print(" Processing And Tasking: 11% \n Processing And Tasking: 24% ")
        time.sleep(0.2)
        print(" Processing And Tasking: 29% ")
        time.sleep(0.2)
        print(" Processing And Tasking: 41% ")
        time.sleep(0.1)
        print(" Processing And Tasking: 56% \n Processing And Tasking: 69% ")
        time.sleep(0.3)
        print(" Processing And Tasking: 77% ")
        time.sleep(0.1)
        print(" Processing And Tasking: 82% ")
        time.sleep(0.2)
        print(" Processing And Tasking: 91% ")
        time.sleep(0.3)
        baslangic()

baslangic()
