# coding: utf8
usernames = ['tom','jack','helen','张三']
flag = 1
while(flag):
    username = raw_input("请输入用户名:").strip()
    if username in usernames:
        print '有效用户!'
        flag = 0
    else:
        print "无效用户，请重新输入 ..."