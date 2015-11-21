# -*- coding: utf-8 -*-
# tcpserver.py
import socket, traceback, os

host = '192.168.36.102'
port = 8000
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mysocket.bind((host, port))
mysocket.listen(100)
print "Server %s is listening on port %d ,and pid is %d , waiting for connections..." %(host, port, os.getpid())

while 1:
    try:
        clientsock, clientaddr = mysocket.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    try:
        print "Got connection from", clientsock.getpeername()
        while 1:
            data = clientsock.recv(4096)
            if not len(data):
                break
            print clientsock.getpeername()[0] + ':' + str(data)
            clientsock.sendall(data)
            clientsock.sendall('I get it !\n')
            t =raw_input('input the world:')
            clientsock.sendall(t)
    except KeyboardInterrupt,SystemExit:
        raise
    except:
        traceback.print_exc()

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()

