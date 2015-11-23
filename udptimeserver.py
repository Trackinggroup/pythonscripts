# -*- coding: utf-8 -*-
import socket, time, traceback, struct, os

host = '192.168.36.102'
port = 8002
print "TimeServer(%s),port(%d),pid(%d) is now up and waiting for connections..." %(host, port, os.getpid())

udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udpsocket.bind((host, port))

while 1:
    try:
        message, address = udpsocket.recvfrom(8192)
        secs = int(time.time())
        secs -= 60 * 60 * 24
        secs += 2208988800
        reply = struct.pack('!I', secs)
        udpsocket.sendto(reply, address)
    except KeyboardInterrupt, SystemExit:
        raise
    except:
        traceback.print_exc()
