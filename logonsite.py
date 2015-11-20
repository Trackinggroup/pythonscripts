# -*- coding: utf-8 -*-
import win32com.client
import time
ie6 = win32com.client.Dispatch("InternetExplorer.Application")

ie6.Navigate("http://login.tudou.com/login.do?noreg=ok")
ie6.Visible = 1
while ie6.Busy:
  time.sleep(1)

document=ie6.Document
document.getElementById("email").value="******"  #登录账号
document.getElementById("pass").value="******"  #登录密码
document.getElementById("login_submit").click()#点击登陆


time.sleep(4)
print 'LOGIN SUCCESS'

