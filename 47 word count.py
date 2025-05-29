string = str(input("Enter the string: "))
i = 0
for m in string:
    i += 1

print(i)
char_count ={}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print('charracter count: ',char_count)