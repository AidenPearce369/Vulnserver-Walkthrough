#!/usr/bin/python
from boofuzz import *
host='192.168.116.141'
port=9999
session=Session(
	target=Target(
		connection=SocketConnection(host, port, proto='tcp')
	),
	sleep_time = 3
)
s_initialize("spike")
s_string("GMON", fuzzable=False)
s_delim(" ", fuzzable=False)
s_string("vulnserver")
session.connect(s_get("spike"))
session.fuzz()
