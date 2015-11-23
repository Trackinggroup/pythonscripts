# -*- coding: utf-8 -*-
# gethostbyaddr-basic.py
import sys, socket
while 1:
    try:
        result = socket.gethostbyaddr(raw_input("Enter IP:"))
        print result[0]
    except socket.herror, e:
        print "could not lookup name:", e