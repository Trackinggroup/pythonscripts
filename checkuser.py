# -*- coding: utf-8 -*-
# checkuser.py
dict = {}
for line in open('/etc/passwd', 'a+'):
    username = line.strip().split(':')[0]
    userhomedir = line.strip().split(':')[5]
    dict[username] = userhomedir

flag = 1
while flag:
    user = raw_input(u"请输入用户名:").rstrip()
    if dict.has_key(user):
        print dict[user]
#       flag = 0
    else:
        print u"无效用户!"



