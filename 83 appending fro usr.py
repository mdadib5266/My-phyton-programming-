text = str(input('enter new text: '))
with open('sample.txt','a+') as my_file:
    content = my_file.write('\n'+text)
print(content)
with open('sample.txt','r') as file:
    content = file.read()
    print(content)