def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def devide(num1,num2):
    return num1/num2

operations_dict = {
    "+": add,
    "-" : substract,
    "*" : multiply, 
    "/" : devide
}

def calculator(): #recurssion process
    num1 = int(input("Enter the first number: "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag = True
    while continue_flag:
        symbol = input("choose symbol from above:")
        num2 = int(input("Enter the second number: "))
        calc_func = operations_dict[symbol]
        output = calc_func(num1, num2)
        print(f"{num1} {symbol} {num2} = {output}")
        should_continue = input(f"Enter 'Y' to continue calculation with {output}, 'N' to start a new calculation or 'X' to exit")

        if should_continue == "Y":
            num1 = output

        elif should_continue == "N":
            continue_flag = False
            calculator()

        else:
            continue_flag = False
            print("Calculation completed")
            
calculator()