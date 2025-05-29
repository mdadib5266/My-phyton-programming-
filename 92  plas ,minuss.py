def calculator():
    num1 = float(input("enter first num "))
    num2 = float(input('num2 '))
    operation = input('+ - * / ')
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    else:
        print(num1/num2)
calculator()