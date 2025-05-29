def bignum(a,b,c):
    if a>b and a>c:
        return "first number"
    elif b>c:
        return "second number"
    return "third number"

num1 = int(input("first number "))
num2 = int(input("second number "))
num3 = int(input("third number "))
print(bignum(num1,num2,num3))