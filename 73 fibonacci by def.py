def fibonacci(n):
    a = 1
    b = 1
    c = 0
    fibseries = [1,1]
    for c in range(0,n-2):
        c = a + b
        if c >= n:
            break
        fibseries.append(c)
        a = b
        b = c
    return fibseries
def fibonacci1(n):
    fibseries = [1,1]
    for i in range(2,n):
        fibseries.append(fibseries[-1]+fibseries[-2])
    return fibseries[:n]#??
num = int(input("n is: "))
print(fibonacci(num))
print(fibonacci1(num))
print(len(fibonacci(num)),len(fibonacci1(num)))
