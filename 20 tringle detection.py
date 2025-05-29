a = float(input("enter the first arm"))
b = float(input("enter the second arm"))
c = float(input("enter the third arm"))
if a == b == c:
    print("the tringle will be homoarmed tringle")
elif a== b != c or b == c != a or c == a != b :
    print("its a two homoarmed tringle")
else:
    print("its a heteroarmed tringle")