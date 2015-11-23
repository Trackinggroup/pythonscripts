import sys, socket
#result = socket.getaddrinfo(sys.argv[1], None)
while 1:
    result = socket.getaddrinfo(raw_input("Enter domain name:"), None)
    print result[0][4][0]