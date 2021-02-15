#!/bin/python3
# -*- coding: utf-8 -*-
"""
Coded by parsa kazazi
GitHub: https://github.com/parsa-kazazi
Twitter: https://twitter.com/parsa_kazazi

Quick and easy TCP Port Scanner
Works on all operating systems
For legal activities only
Version: 1.0
"""

import sys
import os
import socket
import time

os_name = os.name

if (os_name == "nt"):
    os.system("title Port Scanner")
else:
    os.system("printf '\033]2;Port Scanner\a'")

print("""
TCP Port Scanner. version 1.0
""")

put = str("\033[94m[*]\033[0m ")
info = str("\033[94m[i]\033[0m ")
good = str("\033[92m[+]\033[0m ")
error = str("\033[91m[!]\033[0m ")

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
    try:
        address = sys.argv[1]
    except IndexError:
        print("Usage: python3 tps.py <domain or ip>\n")
        exit()
    time.sleep(2)
    try:
        ip = socket.gethostbyname(address) # get target IP address
        hostname = socket.gethostbyaddr(address)[0] # get target hostname
    except socket.gaierror:
        print(error + address + " : Name or service not known\n")
        sys.exit()
    except socket.error:
        print(error + "Connection failed")
        sys.exit()
    else:
        print(good + "Connected")
        time.sleep(1)
        print(info + "Host to scan: " + hostname + " (" + ip + ")")
        print(info + "Scanning. please wait...\n")
        time.sleep(2)
        port = 0
        open_ports = 0
        closed_ports = 0
        try:
            for port in range(0, 9999):
                if (is_port_open(ip, port)):
                    try:
                        service_name = socket.getservbyport(port)
                    except OSError:
                        # if the port service name was unknown
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
