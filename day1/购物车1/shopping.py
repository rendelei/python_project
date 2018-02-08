
shopping_list = [("iphone",5800),("car",20000),("books",50),("apple",10),("bike",500),("TV",3000)]
shopping_flag =False
p_list =[]
salary = int(input("input you salary>>:"))
print("welcome to our supermaket!")
print("-------------------shopping list info----------------------")
for index,i in enumerate(shopping_list):
    shopping_index = index
    shopping_name = i[0]
    shopping_price = i[1]
    print (shopping_index,'\t',shopping_name.ljust(10),'\t',shopping_price)

while not shopping_flag:
    choice = input("Boss,welcome,what do you want to buy? or you can input 'q' exit...")
    if choice =='q':
        shopping_flag = True
    elif choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(shopping_list):
            if salary >=shopping_list[choice][1]:
                salary = salary - shopping_list[choice][1]
                p_list.append(shopping_list[choice])
                choice2 = input("you still have \033[31;1m{_salary}\033[0m RMB,Do you want to buy something else?".format(_salary=salary))
                if choice2 == 'yes':
                    pass
                else:
                    print("-------------------shopping purchase info----------------------")
                    print("You got below things......")
                    for i in p_list:
                        print (i)
                    break
            else:
                choice3 = input("you  have no money to afford %s,plsease choose a cheaper one or input 'q'exit..." % shopping_list[choice][0])
                if choice3 == 'q':
                    shopping_flag = True
else:
    print("-------------------shopping purchase info----------------------")
    print("You got below things......")
    for i in p_list:
        print(i)



