# -*- coding: gbk -*-
import socket, sys
port = 8000
host = raw_input(u'���������IP:')
data = raw_input(u'����Ҫ���͵�����:')

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysocket.connect((host, port))
except:
    print u'���Ӵ���!'

mysocket.send(data)
mysocket.shutdown(1)
print u"�������."

while 1:
    buf = mysocket.recv(4096)
    if not len(data):
        break
    sys.stdout.write(buf)