# -*- coding : utf-8 -*-
# broadcastreceiver.py
import socket
import traceback

host = ''
port = 8004
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
print "Client is ready to receive data..."

while 1:
    try:
        message, address = s.recvfrom(8192)
        print "Got data from", address
    except (KeyboardInterrupt, SystemExit):
        s.sendto("I'm here.", address)
        raise
    except:
        traceback.print_exc()

