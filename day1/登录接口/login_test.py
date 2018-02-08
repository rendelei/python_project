# Author rendelei

list1 = []
list2 = []
count = int(3)
f = open("login.txt")
for line in f:
    hostname = str(line.split('\t')[0])
    list1.append(hostname)
    password = str(line.split("\t")[1]).strip()
    list2.append(password)
while True:
    username = input("username:")

    if username in list1:
        while True:
            passwd = input("passwd:")
            if passwd not in list2:
                count = count - 1
                print("wrong password,you have {_count} chance to login".format(_count=count))

                if count == 0:
                    print("you have no chance ,the {_username} is been locked,fuck off".format(_username=username))
                    lockfile = open("lock.txt", 'a+')
                    lockfile.write("\n"+ username)
                    lockfile.close()
                    break
            else:
                if passwd in list2 and list1.index(username) == list2.index(passwd):
                    print("welcome {_user_username} login the system".format(_user_username=username))
                    break
        break

    else:

        message = input("wrong username,do you want to register it?")

        if message == "y":
            username = input("username:")
            passwd = input("passwd:")
            f1 = open("login.txt","a+")
            f1.write("\n"+username+ "\t")
            f1.write(passwd)
            f1.flush()
            f1.close()
            print ("the {_username} is register successful,pls login again!".format(_username=username))
            break



        else:
            print("you have exit the system!")
            break
f.close()

'''
注册中。涉及新用户登录，重新读取文件（用户名，密码），47行，暂用break ，以便完成退出，后重新加载。
'''