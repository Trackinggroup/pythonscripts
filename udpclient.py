# -*- coding: utf-8 -*-
# udpclient.py
'''
import socket, sys

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    port = int(textport)
except ValueError:
    port = socket.getservbyname(textport, 'udp')

s.connect((host, port))
print "Enter data to transmit: "
data = sys.stdin.readline().strip()
s.sendall(data)
print "Waiting for replies; press Ctrl-C or Ctrl-Break to stop."

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
'''

'''
import socket, time
port = 8002
host = '192.168.36.102'
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
flag = 1
while flag:
    udpsocket.sendto(time.ctime(),(host, port))
    print time.ctime()
    flag = 0
'''

import socket, sys, struct, time
hostname = 'time.nist.gov'
port = 37

host = socket.gethostbyname(hostname)

udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.sendto('', (host, port))

print "Looking for replies; press Ctrl-C to stop."
buf = udpsocket.recvfrom(2048)[0]
if(len(buf)) != 4:
    print "Wrong-sized reply %d: %s" %(len(buf), buf)
    sys.exit(1)

secs = struct.unpack("!I", buf)[0]
secs -= 2208988800
print time.ctime(int(secs))











