n = int(input("input n "))
i,nxt = 0,1
count = 0
while i < n:
    print(i)
    i,nxt = nxt,nxt + 1
    count += 1
