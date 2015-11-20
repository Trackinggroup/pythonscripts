# -*- coding:utf-8 -*-
# udpserver.py
import socket
host = ''
port = 8001
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.bind((host, port))
print u"正在等待接入..."
while 1:
    data, addr = udpsocket.recvfrom(1024)
    print data,addr
