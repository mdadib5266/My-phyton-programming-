def prime(n):
    if n>2:
        for divi in range(2,int(n/2)+1):
            if n % divi == 0:
                return False
            return True
    else:
        return False
num = int(input('enter the number: '))
print(prime(num))