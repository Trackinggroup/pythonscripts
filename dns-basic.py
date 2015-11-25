import sys, DNS

while 1:
    query = raw_input("Enter domain name:")
    DNS.DiscoverNameServers()

    reqobj = DNS.Request()

    answerobj = reqobj.req(name = query, qtype = DNS.Type.ANY)
    print type(answerobj)
#if not len(answerobj):
#    print "Not found."
    for item in answerobj.answers:
        print "%-5s %s" % (item['typename'], item['data'])