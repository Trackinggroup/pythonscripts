name = raw_input("Enter your name: ")
names = ["tom", "jack", "helen", "lili"]
if len(name):
    if name.lower() in names:
        print "found it"
    else:
        print "not found"
else:
    print "Please input the name: "
