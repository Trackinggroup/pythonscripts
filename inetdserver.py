# -*- coding: utf-8 -*-
# Program : inetdserver.py
import sys
flag = 1
while flag:
    print "Welcome."
    print "Please enter a string:"
    sys.stdout.flush()
    line = sys.stdin.readline().strip()
    print "You entered %d characters." %len(line)
