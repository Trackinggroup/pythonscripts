# -*- coding: utf-8 -*-
# inetdudpserver.py
import socket, time, sys

udpsocket = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_DGRAM)
message, address = udpsocket.recvfrom(8192)
udpsocket.connect(address)
for i in range(10):
    udpsocket.send("Reply %d: %s" % ((i + 1), message))
    time.sleep(2)
udpsocket.send("OK, I'm done sending replies.\n")
