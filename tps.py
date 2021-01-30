#!/bin/python3
# -*- coding: utf-8 -*-

"""
Coded by parsa kazazi
@parsa_kazazi (Github, Twitter)

Quick and easy TCP Port Scanner (TPS)
Works on all operating systems
For legal activities only
Version: 1.0
"""

import sys
import time
import os
import socket

os_name = os.name

if (os_name == "nt"):
    os.system("cls")
    os.system("title Port Scanner")
else:
    os.system("clear")
    os.system("printf '\033]2;Port Scanner\a'")

print("""

    ████████ ██████  ███████
       ██    ██   ██ ██
       ██    ██████  ███████
       ██    ██           ██
       ██    ██      ███████

    Quick and easy TCP Port Scanner (tps)

""")

question = str("\033[94m[?]\033[0m ")
info = str("\033[94m[i]\033[0m ")
good = str("\033[92m[+]\033[0m ")
error = str("\033[91m[-]\033[0m ")

def is_port_open(ip: str, port: int):
    # check the port connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # to create connection
    try:
        sock.connect((ip, port))
    except:
        # if port was closed
        return False
    else:
        # if port was open
        return True
    sock.close()

if (__name__ == "__main__"):
    address = input(question + "Enter Target Domain or IP : ")
    time.sleep(2)
    print(info + "Checking connection to " + address + " ...")
    time.sleep(2)
    try:
        ip = socket.gethostbyname(address)
    except socket.gaierror:
        print(error + address + " : Name or service not known\n")
        sys.exit()
    except socket.error:
        print(error + "Connection failed")
        sys.exit()
    else:
        print(good + "Connected")
        time.sleep(1)
        print(info + "Host to scan : " + ip)
        print(info + "Scanning. please wait...")
        time.sleep(2)
        port = 0
        open_ports = 0
        closed_ports = 0
        try:
            for port in range(0, 65535):
                if (is_port_open(ip, port)):
                    print(good + "Port " + str(port) + " is open")
                    open_ports += 1
                else:
                    closed_ports += 1
        except KeyboardInterrupt:
            print(info + "Exiting")
            sys.exit()
        except socket.gaierror:
            print(error + address + " : Name or service not known\n")
            sys.exit()
        else:
            time.sleep(2)
            print(info + "Scan completed. result:")
            time.sleep(1)
            print(info + str(open_ports) + " Ports are open")
            if (open_ports == 0):
                print(info + "All 65535 Ports are closed\n")
            else:
                print(info + str(closed_ports) + " Ports are closed\n")
            time.sleep(1)
