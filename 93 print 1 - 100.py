def prime():
    for i in range(2,100):
        for r in range(2,int(i**0.5)+1):
            if i % r == 0:
                break
        else:
            print(i)
prime()