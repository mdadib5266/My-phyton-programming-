with open('sample.txt','r') as file:
    content = file.read()
with open('sample1.txt','a') as file1:
    content1 = file1.write(content)
with open('sample1.txt','r') as file2:
    content2 = file2.read()
print(content2)