import random
list = []
list1 = [random.randint(1,100) for _ in range(10)]
list1.sort()
while True:
    random_number = random.randint(1,100)
    list.append(random_number)
    if len(list)==10:
        break
list = sorted(list)

print(list,len(list),list1,len(list1))