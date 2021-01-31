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
import socket
import os
import time

os_name = os.name

if (os_name == "nt"):
    os.system("cls")
    os.system("title TPS Port Scanner")
else:
    os.system("clear")
    os.system("printf '\033]2;TPS Port Scanner\a'")

print("""

    ████████ ██████  ███████
       ██    ██   ██ ██
       ██    ██████  ███████
       ██    ██           ██
       ██    ██      ███████

    TCP Port Scanner. Quick and easy

""")

question = str("\033[94m[?]\033[0m ")
info = str("\033[94m[i]\033[0m ")
good = str("\033[92m[+]\033[0m ")
error = str("\033[91m[-]\033[0m ")

def is_port_open(ip: str, port: int):
    # scan the one port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # to create connection
    try:
        sock.connect((ip, port))
    except:
        # if port was closed
        return False
    else:
        # if port was open
        return True
    sock.close() # close the connection

if (__name__ == "__main__"):
    address = input(question + "Target Domain or IP address : ")
    time.sleep(2)
    print(info + "Checking connection to " + address + " ...")
    time.sleep(2)
    try:
        ip = socket.gethostbyname(address) # get target IP address
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
        print(info + "Scanning. please wait...\n")
        time.sleep(2)
        port = 0
        open_ports = 0
        closed_ports = 0
        try:
            for port in range(0, 65536):
                if (is_port_open(ip, port)):
                    try:
                        service_name = socket.getservbyport(port)
                    except OSError:
                        # if port service name is not known
                        service_name = "unknown service"
                    print(good + "Port " + str(port) + " " + service_name + " : is open")
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
            print("\n" + info + "Scan completed. result:")
            time.sleep(1)
            if (open_ports == 0):
                print(info + "All 65535 scanned ports are closed\n")
            else:
                print(info + str(open_ports) + " Ports are open")
                print(info + str(closed_ports) + " Ports are closed\n")
            time.sleep(1)
