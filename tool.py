import os
import sys
import time
import signal
import subprocess as sub
import csv

header = ('''  
     ▄████████     ███        ▄████████    ▄████████ ▀████    ▐████▀    ▄████████ 
      ███    ███ ▀█████████▄   ███    ███   ███    ███   ███▌   ████▀    ███    ███ 
      ███    ███    ▀███▀▀██   ███    ███   ███    ███    ███  ▐███      ███    ███ 
      ███    ███     ███   ▀  ▄███▄▄▄▄██▀   ███    ███    ▀███▄███▀      ███    ███ 
    ▀███████████     ███     ▀▀███▀▀▀▀▀   ▀███████████    ████▀██▄     ▀███████████ 
      ███    ███     ███     ▀███████████   ███    ███   ▐███  ▀███      ███    ███ 
      ███    ███     ███       ███    ███   ███    ███  ▄███     ███▄    ███    ███ 
      ███    █▀     ▄████▀     ███    ███   ███    █▀  ████       ███▄   ███    █▀  
                               ███    ███ Information gathering V1.0 by ZeebXanFlorb                                          
    --------------------------------------------------------------------------------''')
c = 'clear'


# this is used for installing required modules
def install_modules():
    os.system(c)
    print('Installing essential modules...')
    time.sleep(3)
    os.system("sudo apt-get install aircrack-ng")
    time.sleep(2)
    os.system("sudo apt-get install macchanger")
    time.sleep(2)
    os.system("sudo apt-get install traceroute")
    time.sleep(1)
    print('Modules installed successfully')
    time.sleep(2)
    os.system(c)
    menu()


# Wifi interface mode to monitor
def start_monitor_mode():
    os.system(c)
    print('Detecting network adapters')
    time.sleep(5)
    os.system("airmon-ng")
    time.sleep(5)
    print('Killing network services')
    os.system("airmon-ng check kill")
    os.system(c)
    print('Activating MONITOR mode on network interface')
    os.system("airmon-ng start wlan0")
    time.sleep(5)
    print('Network interface is set to MONITOR mode')
    time.sleep(3)
    os.system(c)
    menu()


# Wifi interface mode to managed
def stop_monitor_mode():
    os.system(c)
    print('Detecting network adapters')
    time.sleep(5)
    os.system("airmon-ng")
    time.sleep(5)
    os.system(c)
    print('Deactivating MONITOR mode on network interface')
    os.system("airmon-ng stop wlan0")
    time.sleep(5)
    os.system('service NetworkManager restart')
    print('Network interface is set to MANAGED mode')
    time.sleep(3)
    os.system(c)
    menu()


# Display information and status about Wifi interface
def network_interface_info():
    os.system(c)
    print('Network interface details:')
    os.system("iwconfig")
    print("=========================================================")
    print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|MAIN MENU")
    print("|   2	|PERFORM 2.4Ghz SCAN")
    print("|   3	|PERFORM 5.0Ghz SCAN")
    print("|   4	|EXIT")
    print("=========================================================")
    try:
        a = input("Type your option: ")

        if a == "1":
            os.system(c)
            menu()
        if a == "2":
            scan_network_2_4_Ghz()
        if a == "3":
            scan_network_5_Ghz()
        if a == "4":
            exit_program()
        else:
            print('Invalid option')
    finally:
        pass


# Wifi scan for 2.4Ghz networks only
def scan_network_2_4_Ghz():
    proc = sub.Popen(
        ['airodump-ng', 'wlan0', '-w', 'scan_results/Scanresult24ghz', '--output-format', 'csv', '--manufacturer'])
    print('Starting 2.4Ghz Scan...')
    time.sleep(5)
    os.kill(proc.pid, signal.SIGINT)
    time.sleep(3)
    print('Scan results are saved...')
    time.sleep(3)
    os.system(c)
    print("=========================================================")
    print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|MAIN MENU")
    print("|   2	|EXIT")
    print("|   3	|PERFORM 5Ghz SCAN")
    print("=========================================================")
    try:
        a = input("Type your option: ")
        if a == '1':
            os.system(c)
            menu()
        if a == "2":
            exit_program()
        if a == "3":
            scan_network_5_Ghz()
    except EOFError as e:
        print(e)
    menu()


# Wifi scan for 5Ghz networks only
def scan_network_5_Ghz():
    proc = sub.Popen(
        ['airodump-ng', '--band a', 'wlan0', '-w', 'scan_results/Scanresult5ghz', '--output-format', 'csv',
         '--manufacturer'])
    print('Starting 5Ghz Scan...')
    time.sleep(5)
    os.kill(proc.pid, signal.SIGINT)
    time.sleep(3)
    print('Scan results are saved...')
    time.sleep(3)
    os.system(c)
    print("=========================================================")
    print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|MAIN MENU")
    print("|   2	|EXIT")
    print("|   3	|PERFORM 2.4Ghz SCAN")
    print("=========================================================")
    try:
        a = input("Type your option: ")
        if a == '1':
            os.system(c)
            menu()
        if a == "2":
            exit_program()
        if a == "3":
            scan_network_2_4_Ghz()
    except EOFError as e:
        print(e)
    menu()


def wifi_scan_menu():
    print(header)
    print("=========================================================")
    print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|SCAN 2.4Ghz")
    print("|   2	|SCAN 5.0Ghz")
    print("|   99	|BACK")
    print("=========================================================")

    try:
        a = input("Type your option: ")

        if a == "1":
            scan_network_2_4_Ghz()
        if a == "2":
            scan_network_5_Ghz()
        # if a == "3":
        #     stop_monitor_mode()
        # if a == "4":
        #     network_interface_info()
        # if a == "5":
        #     scan_network()
        # if a == "6":
        #     show_results()
        if a == "99":
            menu()

        else:
            print("Please input a possible option.")
            time.sleep(1)
            wifi_scan_menu()
    except EOFError as e:
        print(e)
    menu()


# Display results of the scan
def show_results():
    with open('scan_results/Scanresult24ghz-01.csv', 'r', encoding='UTF8') as scan_result:
        csv_reader = csv.reader(scan_result)
        for line in csv_reader:
            print(line)
        print("=========================================================")
        print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
        print("=========================================================")
        print("|   1	|MAIN MENU")
        print("|   2	|EXIT")
        print("=========================================================")
        try:
            a = input("Type your option: ")
            if a == '1':
                os.system(c)
                menu()
            if a == "2":
                exit_program()
        except EOFError as e:
            print(e)
        menu()


# Menu for MAC address
def mac_changer():
    os.system(c)
    print(header)
    print("=========================================================")
    print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|PRINT MAC ADDRESS")
    print("|   2	|SET RANDOM MAC ADDRESS")
    print("|   3	|RESET MAC ADDRESS")
    print("|   99	|BACK")
    print("=========================================================")
    try:
        a = input("Type your option: ")
        if a == '1':
            os.system(c)
            print_mac()
        if a == "2":
            os.system(c)
            random_mac()
        if a == "3":
            os.system(c)
            reset_mac()
        if a == "99":
            os.system(c)
            menu()
    except EOFError as e:
        print(e)
    menu()


# Display MAC address information
def print_mac():
    os.system('macchanger -s wlan0')
    time.sleep(5)
    mac_changer()


# set random MAC adress
def random_mac():
    print('Setting random MAC address...')
    os.system('ifconfig wlan0 down')
    time.sleep(5)
    os.system('macchanger -A wlan0')
    time.sleep(5)
    os.system('ifconfig wlan0 up')
    mac_changer()


# reset random MAC address to original
def reset_mac():
    print('Restoring to original MAC...')
    os.system('ifconfig wlan0 down')
    time.sleep(5)
    os.system('macchanger -p wlan0')
    time.sleep(5)
    os.system('ifconfig wlan0 up')
    mac_changer()


# trace packets send to URL
def packet_tracer():
    os.system(c)
    url = input("Enter URL:")
    os.system(f'traceroute -I {url}')
    time.sleep(3)
    print("=========================================================")
    print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|MAIN MENU")
    print("|   2	|EXIT")
    print("=========================================================")
    try:
        a = input("Type your option: ")
        if a == '1':
            os.system(c)
            menu()
        if a == "2":
            exit_program()
    except EOFError as e:
        print(e)
    menu()


def exit_program():
    sys.exit()


def menu():
    os.system(c)
    print(header)
    print("=========================================================")
    print("|		    " + "\033[1m" + "AVAILABLE OPTIONS:" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|INSTALL ESSENTIAL MODULES")
    print("|   2	|ACTIVATE MONITOR MODE")
    print("|   3	|DEACTIVATE MONITOR MODE")
    print("|   4	|NETWORK INTERFACE STATUS")
    print("|   5	|SCAN WIFI NETWORKS")
    print("|   6	|SHOW SCAN RESULTS")
    print("|   7	|MAC CHANGER")
    print("|   8	|PACKET TRACER")
    print("|   99	|EXIT")
    print("=========================================================")

    try:
        a = input("Type your option: ")

        if a == "1":
            install_modules()
        if a == "2":
            start_monitor_mode()
        if a == "3":
            stop_monitor_mode()
        if a == "4":
            network_interface_info()
        if a == "5":
            os.system(c)
            wifi_scan_menu()
        if a == "6":
            show_results()
        if a == "7":
            mac_changer()
        if a == "8":
            os.system(c)
            packet_tracer()
        if a == "99":
            exit_program()

        else:
            pass

    finally:
        pass


menu()
