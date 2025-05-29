num1 = int(input("enter  first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
'''
if num1>num2:
    if num1>num3:
        print("the first number is the greatest number")
    else:
        print("the third number is the greatest number")
elif num2>num3:
    print("the second number is the greatest number")
elif num1 == num2 == num3:
    print("numbers are equal")
elif num3:
    print("the third number is the greatest number")
else:
    print("something went wrong")
'''
if num1 != num2 != num3:
    largest = max(num1,num2,num3)
    print("largest number is",largest)
else:
    print("they are equal")