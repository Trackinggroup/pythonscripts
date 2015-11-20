# -*- coding: utf-8 -*-
##@小五义 http://www.cnblogs.com/xiaowuyi
'''
借书方案：小明有m本新书，要借给n位小朋友，若每人每次只能借一本，则可以有多少种不同的借法。
'''

def combination(lst,n):#将lst中取出n个进行组合
    rst = []
    if n == 1:
        for i in lst:
            l = []
            l.append(i)
            rst.append(l)
    else:
        for i in combination(lst,n-1):
            for j in range(lst.index(i[-1])+1,len(lst)):
                l = i[:]
                l.append(lst[j])
                rst.append(l)
    return rst
def permute(num):#将书进行排列
    l = len(num)
    if l <= 2:
        if l == 2:
            return [num,num[1],num[0],num[1]+num[0]]
        else:
            return [num]
    else:
        list = []
        for i in range(len(num)):
            li = num[:i]+num[i+1:]
            #print 'li=',li
            for x in permute(li):
                p=num[i:i+1]+x
                list.append(p)
        return list

if __name__ == "__main__":
    count=0  #记录第几种分法
    rst = []#记录书的组合
    lst=[]#将书编号
    numlist=[]#记录数组合后的数字
    num_bool=True #用来判断小朋友数不大于书的数量
    book_list=[]#记录最后组合数
    ##判断小朋友数不大于书的数量
    while num_bool:
        try:
            books=int(raw_input('小明一共有书的数量：'))
            baby=int(raw_input('要分给的小朋友数量(不大于书的数量):'))
            if baby>books or books==0 or baby==0:
                print'输入错误，请重新输入。'
                num_bool=True
            else:
                num_bool=False
        except:
            print'输入错误，请重新输入。'
            num_bool=True
    for i in range(1,books+1):
        lst.append(str(i))
    books_com=combination(lst,baby)
    rst=rst+books_com
    for i in rst:#将得到的组合读出
        numstr=''
        for j in i:#将组合组成数字
            numstr=numstr+j
        numlist.append(numstr)
    ##print numlist
    for i in numlist:
        list1=permute(i)
        ##book_list=[''.join(x) for x in list1 if len(x)==len(i)]
        for x in list1:
            if len(x)==len(i):
                book_list.append(x)
    for i in book_list:
        count+=1
        print "第%d种：%s"%(count,i)