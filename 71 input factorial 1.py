def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)#wnen it comes to functions , we give something and the function returns something.
    # so we must use return to get something to place in the variable [factorial(n)] instead of using print
num = int(input('number: '))
print(f'{num} factorial:',factorial(num))