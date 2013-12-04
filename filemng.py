#Justin Clark
import os
filename = raw_input("Filename?\n>>>")
path = os.getcwd() + "/"
goods = path + filename
options = int(raw_input
("\n1.Save list of all files in current directory\n\n2.Write to file\n\n\n>"))
if options == 1:
    userinfo = os.listdir(os.getcwd())
    data = open(goods, 'w')
    data.write(str(userinfo))
elif options == 2:
    userinfo = raw_input()
    data = open(goods, 'w')
    data.write(str(userinfo))
else:
    print "invalid option"
