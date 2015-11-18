# -*- coding: UTF-8 -*-
# 得到素数
'''
i = 2
maxvalue = raw_input('请输入一个数字:').strip()
if maxvalue.isalnum():
    while(i < maxvalue):
        j = 2
        while(j <= (i/j)):
            if not (i%j):
                break
            j = j + 1
        if (j > i/j) :
            print i, " 是素数"
        i = i + 1

print "Good bye!"

'''
i = 2
#maxvalue = raw_input('请输入一个数字:').strip()
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not (i%j):
          break
      j = j + 1
   if (j > i/j):
       print i, ":是素数"
   i = i + 1
print "结束..."












'''
i = 2
while(i<100):
    j = 2
    while(j <= (i/j)):
        if not (i%j):
            break
            j = j + 1
            if (j > i/j):
                print i,"是素数"
                i = i + 1
print "xxxxxx"
'''