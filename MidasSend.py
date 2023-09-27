#!/usr/bin/env python3


from pythonosc import udp_client
import time
import socket
import argparse
import sys


# IP and port midas m32 default port for control is 10023
if len(sys.argv) > 1:
    ip = (sys.argv[1])
else:
    ip = "help"
    print("""To use this program first argv  is ip address of the midas
argv 2 is the port (Default 10023 to control)
argv 3 is your osc adr
argv 4 is int of float (i, f)
argv 5 is your msg""")
    exit()    
port = (sys.argv[2])
adr = (sys.argv[3])
typ = (sys.argv[4])
msg1 = (sys.argv[5])

if typ == "i":
    msg = int(msg1)
elif typ == "f":
    msg = float(msg1)

client = udp_client.SimpleUDPClient(ip, int(port)) 
time.sleep(0.5)
client.send_message(adr, msg)