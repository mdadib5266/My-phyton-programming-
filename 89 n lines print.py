n = int(input("int: "))

with open('sample.txt','r') as file:
    for i in range(n):
        print(file.readline().strip())