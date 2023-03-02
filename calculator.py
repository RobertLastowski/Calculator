from math import *

def calculator(operation, my_list):
    sum = 0
    #add
    if operation == "+":
        for item in my_list:
            sum +=item
        return sum
    #substract
    elif operation == "-":
        sum = my_list[0]
        for item in my_list:
            if item == my_list[0]:
                continue
            else:
                sum -= item
        return sum
    #eponential
    elif operation == "exp":
        sum = []
        for item in my_list:
            sum.append(exp(item))
        return sum
    #multiply
    elif operation == "*":
        sum = 1
        for item in my_list:
            sum *= item
        return sum
    #power
    elif operation == "pow":
        sum = my_list[0]
        for num in range(len(my_list)-1):
            sum =  pow(sum,my_list[num+1])
        return sum
    #divide
    elif operation == "/":
        sum = my_list[0]
        for item in my_list:
            if item == my_list[0]:
                continue
            else:
                if item == 0:
                    print("Do not divide by 0!!")
                    continue
                else:
                    sum /= item
        return sum
    else:
        return "Unknown operation :/"


while True:
    operation_flag = False
    my_list = []
    print("This is a calculator with which you can \nadd (+),\nsubstract (-),\ndivide (/),\nmultiply (*),\ntake the number to the power (pow),\ncalculate the value of exponential function (exp)")
    while True:
        a = input("Write down the number(if you want to stop write ""stop""): ")
        if a == "stop":
            break
        elif a.isdigit() != True:
            print("It's not a number!")
        else:
            my_list.append(float(a))
    while operation_flag == False:
        operation = input("Choose the action: Write + or - or * or / or pow or exp : ")
        if operation not in ["+","-","*","/","exp","pow"]:
            print("Please choose from available operators: + , - , * , / , pow , exp: ")
        else:
            operation_flag = True
    if my_list != []:    
        print(calculator(operation, my_list))
    else:
        print("No numbers no results :)")

    choice = input("Want to calculate some more? Write yes or no: ")
    if choice == "yes" or choice == "y":
        continue
    elif choice == "no" or choice == "n":
        break