# -*- coding: utf-8 -*-
import socket, traceback
host = ''
port = 8000
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket1.bind((host, port))
socket1.listen(1)
print "Server is up on port", port, ",waiting for connections..."

while 1:
    try:
        clientsock, clientaddr = socket1.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    try:
        print u"Got connection from", clientsock.getpeername()
        while 1:
            data = clientsock.recv(4096)
            if not len(data):
                break
                clientsock.sendall(data)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

try:
    clientsock.close()
except KeyboardInterrupt:
    raise
except:
    traceback.print_exc()

