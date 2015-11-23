# -*- coding:utf-8 -*-
# udpserver.py
import socket, traceback, os
host = ''
port = 8001
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.bind((host, port))
print u"服务器(%s)端口(%d)正在监听,pid %d ,等待接入中..."%(host, port, os.getpid())
while 1:
    try:
        message, addr = udpsocket.recvfrom(8192)
        udpsocket.sendto(message, addr)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

