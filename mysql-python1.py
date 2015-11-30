# -*- coding: utf-8 -*-
import MySQLdb, socket, traceback, sys, os, string
conn = MySQLdb.connect(host = '192.168.36.102', user = 'root', passwd ='password', db = 'mysql' )
cursor = conn.cursor()
sql = "insert into test1(name,age) values('lili',18)"
try:
    cursor.execute(sql)
    conn.commit()
except:
    cursor.rollback()
cursor.close()
conn.close
