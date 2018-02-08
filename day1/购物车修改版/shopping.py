'''
1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
7、允许查询之前的消费记录
遗留问题：如何实现判断文件追加的次数，以便记录shopping的次数
'''

import os

def shopping(salary):
    shopping_list = [("iphone", '5800'), ("car", '20000'), ("books", '50'), ("apple", '10'),
                     ("bike", '500'), ("TV", '3000')]
    shopping_flag = False
    p_list = []
    while not shopping_flag:
        print("welcome to our supermarket!")
        print("-------------------shopping list info----------------------")
        print("Good_Index".ljust(15), "\t", "Good_Name".ljust(15), "\t", "Good_Price".ljust(10))
        for index, i in enumerate(shopping_list):
            shopping_index = index
            shopping_name = i[0]
            shopping_price = i[1]
            print(str(shopping_index).ljust(15), '\t', shopping_name.ljust(15), '\t',
                  str(shopping_price).ljust(10))
        choice = input(
            "Welcome to our supermarket, input the Number of Good_Index in front of what you want to buy, or you can input 'c'to check what you buy or 'q' to exit ...\n")
        if choice.lower() == 'q':
            shopping_flag = True
        if choice.lower() == 'c':
            print("you got below thins...")
            for l in p_list:
                print(str(l[0]).ljust(15), "\t", str(l[1]).ljust(10))
            print("your balance is \033[31;1m%s\033[0m RMB" % salary)
        elif choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(shopping_list):
                price = int(shopping_list[choice][1])
                if salary >= price:
                    salary = salary - price
                    p_list.append(shopping_list[choice])
                    print(
                        "Added \033[32;1m[%s]\033[0m into your shopping list successful" %
                        shopping_list[choice][0])

                    choice2 = input(
                        "\nYou still have \033[31;1m{_salary}\033[0m RMB. Pls press 'Yes'or 'Y' to buy more, press 'C 'or 'c' to check what you buy,press 'Q' or 'q' to exit\n".format(
                            _salary=salary))
                    if choice2.lower() == 'yes' or choice2.lower() == "y":
                        continue
                    if choice2.lower() == 'c':
                        print("you got below thins...")
                        for l in p_list:
                            print(str(l[0]).ljust(15), "\t", str(l[1]).ljust(10))
                        print("your balance is \033[31;1m%s\033[0m RMB" % salary)
                        choice4 = input(
                            "if you still want buy something ,pls press 'Yes'or 'Y',or you can press 'q' or 'Q' to exit..")
                        if choice4.lower() == 'yes' or choice2.lower() == "y":
                            continue
                        if choice4.lower() == 'q':
                            shopping_flag = True
                    if choice2.lower() == 'q':
                        shopping_flag = True
                else:
                    choice3 = input(
                        "your banlance is \033[031;1m%s\033[0m ,you have no enough money to afford %s,"
                        "press any key to back and choose a cheaper one or input 'Q or q'to exit...\n" % (
                            salary, shopping_list[choice][0]))

                    if choice3.lower() == 'q':
                        shopping_flag = True
            else:
                print("You input wrong Good_Index, please check and input again!")
    else:
        print("you got below thins...")
        with open(username + "_goods_list.txt", "a+", encoding="utf-8") as g_file:
            s = ("\nyour balance is %s RMB\n" % salary)
            for i in p_list:
                t = str(i[0]).ljust(15) + "\t" + str(i[1]).ljust(10) + "\n"
                print(t)
                g_file.write(t)
            print("your balance is \033[31;1m%s\033[0m RMB" % salary)
            g_file.write(s)
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
                    if os.path.exists(username + "_goods_list.txt"):
                        with open(username + "_goods_list.txt", "r", encoding="utf-8") as new_g_file:
                            print("Last Shoppinglist>>...")
                            l3=[]
                            for line in new_g_file:
                                print (line.strip())
                                l3.append(line)
                            s = l3[-1]
                            l4= s.split(" ")
                        choice5 = input("Do you still want to buy some thing ?")
                        if choice5.lower() == 'y' or 'yes':
                            salary = int(l4[-2])
                            shopping(salary)
                        else:
                            break

                    else:
                        salary = int(input("input you salary>>:"))
                        shopping(salary)
                    break
        break

    else:

        message = input("wrong username,do you want to register it?")

        if message.lower() == "y" or "yes":
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




