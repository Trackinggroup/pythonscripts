# -*- coding: utf-8 -*-
# pollclient.py
import socket, sys, select
port = 8005
host = 'localhost'

spinsize = 10
spinpos = 0
spindir = 1

def spin():
    global spinsize, spinpos, spindir
    spindir = '.' * spinpos + '|' + '.' * (spinsize - spinpos -1)
    sys.stdout.write('\r' + spindir + ' ')
    sys.stdout.flush()

    spinpos += spindir
    if spinpos < 0:
        spindir = 1
        spinpos = 1
    elif spinpos >= spinsize:
        spinpos -= 2
        spindir = -1

    s = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
    s.connect((host, port))

    p = select.poll()
    p.register(s.fileno(), select.POLLIN | select.POLLER | select.POLLHUP)
    while 1:
        results = p.poll(50)
        if len(results):
            if results[1][1] == select.POLLIN:
                data = s.recv(4096)
                if not len(data):
                    print "\rRemote end closed connection; exiting..."
                    break
                sys.stdout.write("\rReceived: " + data)
                sys.stdout.flush()



































