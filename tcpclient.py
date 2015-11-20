# -*- coding: gbk -*-
import socket, sys
port = 8000
host = raw_input(u'输入服务器IP:')
data = raw_input(u'输入要发送的内容:')

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysocket.connect((host, port))
except:
    print u'连接错误!'

mysocket.send(data)
mysocket.shutdown(1)
print u"发送完成."

while 1:
    buf = mysocket.recv(4096)
    if not len(data):
        break
    sys.stdout.write(buf)