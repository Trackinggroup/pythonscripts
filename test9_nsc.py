'''
import socket

print "Creating socket..."
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "done."

print "Connecting to remote host..."
s.connect(("www.sina.com.cn",80))
print "done"
'''

'''
import socket
print "Creating socket..."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done."

print "Looking up port number..."
port = socket.getservbyname('http', 'tcp')
print "done"

print "Connecting to remote host on port %d..." % port
s.connect(("www.baidu.com", port))
print "done."
'''

import socket
print "Creating socket..."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done."

print "Connecting to remote host..."
port = socket.getservbyname('http','tcp')
print "done."

print "Connecting to remote host on port %d..." % port
s.connect(('www.zgsj.com', port))
print "done."









