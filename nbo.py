# -*- coding: utf-8 -*-
# nbo.py
import sys, struct
def htons(num):
    return struct.pack('!H', num)
def htnol(num):
    return struct.pack('!I', num)
def hton1(data):
    return struct.unpack('!H', data)[0]
def ntho1(data):
    return struct.unpack('!I', data)[0]
def sendstring(data):
    return hton1(len(data)) + data

print "Enter a string :"
str1 = sys.stdin.readline().rstrip()
print repr(sendstring(str1))