# -*- coding: utf-8 -*-
'''
fileopen = open("test1.txt","ab+")
print "文件名:",fileopen.name
print "文件状态:",fileopen.closed
print "打开模式:",fileopen.mode
print fileopen.softspace
#print fileopen.write("这是一段测试文本!")
print fileopen.write("这也是一段测试文本!")
print fileopen.write('x' * 50 )

fileopen.close()
print 'x' * 50
print "文件状态:",fileopen.closed
'''
import codecs
fo = codecs.open('test1.txt','r+')
str = fo.read(4).decode('gb2312')
print str
fo.close()
