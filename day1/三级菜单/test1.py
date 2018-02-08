# Author rendelei
china_dict = {
    "East":{
        "Fj":["XM","NP","SM"],
        "Zj":["HF","SX","NB"],
        "SD":["JN","QD","DZ"]
    },
    "West":{
        "XZ":["LS","MT","RKZ"],
        "SC":["CD","MY","DY"],
        "GX":["NN","HZ","BH"]
    },
    "South":{
        "GZ":["SZ","HY","DG"],
        "HN":["ZS","YZ","YY"],
        "HaiNan":["HK","SY","SS"]
    },
     "Nouth":{
     "HB":["HD","BD","SJZ"],
     "SX":["TY","DT","XZ"],
     "NM":["BT","CF","HS"]
    }
}
exit_flag = False
while not exit_flag:
    for i in china_dict:
        print(i)
    choice = input("please choose one location you like>>...")
    if choice in china_dict:
        while not exit_flag:
            for j in china_dict[choice]:
                print (j)
            choice2 = input("please choose one province you like>>..")
            if choice2 in china_dict[choice]:
                while not exit_flag:
                    for k in china_dict[choice][choice2]:
                        print(k)
                    choice3 = input("This is the end menue,pls choose 'b' return or 'q' exit>>..")
                    if choice3 =="b":
                        break
                    elif choice3=="q":
                        exit_flag = True
            if choice2 =="b":
                break
            elif choice2 == "q":
                exit_flag = True
print("you exit the program!welcome next time!")
