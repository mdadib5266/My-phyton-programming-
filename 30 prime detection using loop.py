num = int(input("Enter a number: "))
if num>1:
    for i in range(1,int(num/2)+1):
        if num%i == 0:
            print("Prime")
            break
    else:
        print("not prime")
else:
    print("not prime")