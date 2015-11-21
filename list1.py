# -*- coding: utf-8 -*-
'''import math
a = 25.0
print math.floor(math.pi)
print math.pi
print math.floor(-45.345)
print math.log10(-1000)
import cmath
print cmath.log10(-1000)
print cmath.log(32,2)
cmath.log()
'''
'''
import random
list1 = ['tom','jack','helen','lili']
list2 = range(1,10,2)
print random.choice(list1)
print list2
print random.choice(list2)
'''

'''
#利用随机数生成随机数种子,seed()
import random
randnumber = random.randrange(-1,1)
#print randnumber
random.seed(randnumber)
print random.random()
'''

'''
#对序列进行随机排序
import random
list1 = ['tom','jack','helen','lili']
random.shuffle(list1)
print list1
'''

'''
#随机生成下一个实数,uniform()
import random
start = 10
end = 100
randnumber = random.uniform(start,end)
print randnumber
'''

'''
#返回x(x范围-1到1)的反余弦值，acos()
import random,math
randrange = random.randrange(-1,1)
random.seed(randrange)
acos1 = math.acos(random.random())
print acos1
'''

'''
def func1(username='tom',password=2345):
    dict1 = {
        'tom':1234,
        'jack':2345,
        'helen':3456,
        'lili':4567
    }

    if (username in dict1.keys()) and (password in dict1.values()):
        print "Login success !"
        return 1
    else:
        print "Login failed !"
        return 0

func1('jack',2345)
'''


def func2(**dict1):
    print dict1
#func2(**{'tom':1234,'tim':2345,'helen':3456})

'''
def func3(*list1):
    print list1
func3('tim','jack','helen')

def func4(*arg1,**arg2):
    print 'arg1:', arg1
    print 'arg2:', arg2

#func4(1,2,3,tom=18,helen=17,lili=16)
'''

'''
sum1 = lambda arg1,arg2:arg1 * arg2
print sum1(1000000,20)
'''

total = 0
def sum2(arg1,arg2):
    total = arg1 + arg2
    print total
    return total
