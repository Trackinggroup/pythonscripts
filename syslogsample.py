# -*- coding: utf-8 -*-
# syslogsample.py
import syslog, sys, StringIO, traceback, os
def logexeception(includetraceback = 0):
    exectype, exeception, exectraceback = sys.exc_info()
    execclass = str(exeception.__class__)
    message = str(exeception)

    if not includetraceback:
        syslog.syslog(syslog.LOG_ERR, "%s: %s" % (execclass, message))
    else:
        excfd = StringIO.StringIO()
        traceback.print_exception(exctype, exception, exctraceback, None, excfd)
        for line in excfd.getvalue().split("\n"):
            syslog.syslog(syslog.LOG_ERR, line)

def initsyslog():
    syslog.openlog("%s[%d]" % (os.path.basename(sys.argv[0]), os.getpid()), 0, syslog.LOG_DAEMON)
    syslog.syslog("Started.")

initsyslog()

try:
    raise  RuntimeError, "Exeception 1"
except:
    logexeception(0)

try:
    raise RuntimeError, "Exception 2"
except:
    logexeception(1)

syslog.syslog("I'm terminating.")

















