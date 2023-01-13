def calculator(operation, my_list):
    sum = 0
    if operation == "+":
        for item in my_list:
            sum +=item
        return sum
    elif operation == "-":
        sum = my_list[0]
        for item in my_list:
            if item == my_list[0]:
                continue
            else:
                sum -= item
        return sum
    elif operation == "*":
        sum = 1
        for item in my_list:
            sum *= item
        return sum
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
    print("This a calculator with which you can add +, substract -, divide /, or multiply *")
    while True:
        a = input("Write down the number(if you want to stop write ""stop""): ")
        if a == "stop":
            break
        elif a.isdigit() != True:
            print("It's not a number!")
        else:
            print(type(a))
            my_list.append(float(a))
    while operation_flag == False:
        operation = input("Choose the action: Write + or - or * or / ")
        if operation not in ["+","-","*","/"]:
            print("Please choose from available operators: + , - , * , / ")
        else:
            operation_flag = True
        
    print(calculator(operation, my_list))

    wybor = input("Want to calculate some more? Write yes or no: ")
    if wybor == "yes" or wybor == "y":
        continue
    elif wybor == "no" or wybor == "n":
        break