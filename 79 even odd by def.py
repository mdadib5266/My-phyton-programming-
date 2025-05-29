def evodd(n):
    if n%2 == 0:
        return 'even'
    return 'odd'

def iseven(n):
    return n%2 == 0

num = int(input('number: '))
print(evodd(num),iseven(num))