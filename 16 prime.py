num = int(input("input the number: "))
if num>1:
    for i in range(2,int(num/2) +1):
        if num%i == 0:
            print("not prime")
            break
    else:
        print("prime")
    '''elif num == 1 or num ==2 or num ==3:
            print("prime")'''
else:
    print("not prime")

print(list(range(2,2)))