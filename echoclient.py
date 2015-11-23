# -*- coding: utf-8 -*-
# echoclient.py
import socket, sys
host = 'localhost'
port = 8000

data = "x" * 1048576000

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((host, port))

byteswritten = 0
while byteswritten < len(data):
    startpos = byteswritten
    endpos = min(byteswritten + 1024, len(data))
    byteswritten += socket1.send(data[startpos:endpos])
    sys.stdout.write("Wrote %d bytes\r" % byteswritten)
sys.stdout.flush()

socket1.shutdown(1)

print "All data sent."
while 1:
    buf = socket1.recv(1024)
    if not len(buf):
        sys.stdout.write(buf)

