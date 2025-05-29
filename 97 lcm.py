import math

def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))

print(f"{num1} and {num2}'s lcm: ",lcm(num1,num2))

'''num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))'''
if num1 > num2 :
    l = num1
else:
    l = num2
while True:
    if l%num1==0 and l%num2==0:
        print(f'lcd = {l}')
        break
    else:
        l += 1