#_*_coding:utf-8_*_
import  multiprocessing
import paramiko
import getpass
import ConfigParser
class MultiTask(object):
    '''handles all the multi task works'''
    def __init__(self):
        msg = self._interactive()
        self.__run_cmd(msg)
    def __show_cmd_list(self,msg):
        '''show all available cmd list'''
        help_content = '''
        run_cmd     run cmd on multiple hosts
                    run_cmd -u remote_user -g group1,group2 -cmd pwd
                    run_cmd -u remote_user -re regular expression -cmd pwd
        '''

    def _interactive(self):
        msg = []
        nodes = []
        #parse setting.conf
        Config = ConfigParser.ConfigParser()
        Config.read("./setting.conf")
        groups = Config.sections()
        print groups
        # Input group name
        while True:
            try:
                group = raw_input("\033[33;1mPlease Input Group Name:\033[0m").strip()
                if len(group) == 0 : continue
                elif group not in groups:
                    print "Wrong group name ! Please input again!"
                    continue
                else :
                    print "You have choose group %s , the children in this group are :" % group
                    break

            except (KeyboardInterrupt):
                print '\n'
                exit(1)

        items = dict(Config.items(group))
        for node in items.values():
            nodes.append(node)
            print node

        # Input command
        while True:
            try:
                cmd = raw_input("\033[33;1mPlease Input Command:\033[0m").strip()
                if len(cmd) == 0 : continue
                else: break
            except (KeyboardInterrupt):
                print '\n'
                exit(1)
        print "Command you input is %s" % cmd

      # Input username and password
        while True:
            try:
                username = raw_input("\033[33;1mPlease Input username:\033[0m").strip()
                if len(username) == 0 : continue
                else: break
            except (KeyboardInterrupt):
                print '\n'
                exit(1)
        password = getpass.getpass()
        msg = [nodes,username,password,cmd]
        print msg
        return msg
    def __run_cmd(self,msg):
        pool = multiprocessing.Pool(5)
        lock = multiprocessing.Manager().Lock()
        res_list = []
        #msg = [['10.9.214.10','haohzhang','871102_Hadoop'],['10.9.214.105','haohzhang','871102_Hadoop'],['10.9.214.106','haohzhang','871102_Hadoop']]
        for host in msg[0]:
            p = pool.apply_async(run_task, args=(host,msg[1:],lock))
            res_list.append(p)
        pool.close()
        pool.join()
        print '--------All task are finished!-------'
def run_task(host,msg,lock):
    ip = host
    username = msg[0]
    password = msg[1]
    cmd = msg[2]
    print "ip %s, username %s, passwd %s, cmd %s" % (ip, username, password, cmd)
    port = 22
    s = paramiko.SSHClient()    #绑定实例
    s.load_system_host_keys()   #加载本机know host主机文件
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        s.connect(ip,port,username,password,timeout=5)   #连接远程主机
        stdin,stdout,stderr = s.exec_command(cmd)   #执行命令
        cmd_result = stdout.read(),stderr.read()    #读取命令结果
        lock.acquire()
        print '----------- HOST:%s  IP:%s -------------' %(username,ip)
        for line in cmd_result:
            print line,
        lock.release()
        s.close()
    except Exception,e:
        print '----------- HOST:%s  IP:%s -------------' %(username,ip)
        print '\033[31;1mError:%s\033[0m' % e
# vim:ts=4:sw=4:expandtab