# -*- coding:gbk -*-
# Python:          2.7
# Platform:        Windows & Linux
# Author:          Steven
# Program:         �˿�ɨ��
# History:         2015.11.19
 
import socket, time, thread
socket.setdefaulttimeout(3)
 
def socket_port(ip, port): # ����IP�Ͷ˿ںţ�ɨ���ж϶˿��Ƿ񿪷�
    try:
        if port>=65535:
            print u'�˿�ɨ�����'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
        if result == 0:
            lock.acquire()
            print ip, u':',port,u'�˿ڿ���'
            lock.release()
        s.close()
    except:
        print u'�˿�ɨ���쳣'
 
def ip_scan(ip): #����IP��ɨ��IP��0-65534�˿����
    try:
        print u'��ʼɨ�� %s' % ip
        start_time = time.time()
        for i in range(0,65534):
            thread.start_new_thread(socket_port,(ip,int(i)))
        print u'ɨ��˿���ɣ��ܹ���ʱ ��%.2f' %(time.time()-start_time)
        raw_input("��������˳�����...")
    except:
        print u'ɨ��ip����'

if __name__ == '__main__':
    url = raw_input('��������Ҫɨ���IP(s):\n')
    lock=thread.allocate_lock()
    ip_scan(url)
