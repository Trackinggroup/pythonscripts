# -*- coding: utf8 -*-
import math
#print math.modf(5.10)

a,b = math.modf(5.10) #取出小数的小数部分和整数部分
print 'a=',a
print 'b=',b
print '做幂运算:', pow(b,a*20)#做幂运算
print '取整数部分:', math.floor(pow(b, a * 20))#取整数部分
