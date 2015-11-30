# -*- coding: utf-8 -*-
# timeoutserver.py
import socket, sys, traceback

host = '192.168.36.102'
port = 8003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
print "Server %s is up and listening on %d ,waiting for connections..." % (host, port)

while 1:
    try:
        clientsock ,clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    #clientsock.settimeout(5)

    try:
        print "Got connection from ", clientsock.getpeername()
        while 1:
            data = clientsock.recv(4096)
            if not len(data):
                break
            clientsock.sendall(data)
    except (KeyboardInterrupt, SystemExit):
        raise
    #except socket.timeout:
        #print "Timed out !"
    except:
        traceback.print_exec()

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exec()



