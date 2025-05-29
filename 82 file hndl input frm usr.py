text = str(input("string : "))
with open('sample1.txt','w') as file:
    content = file.write(text)
    print(content)