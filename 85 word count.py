with open('sample.txt','r') as file:
    content = file.read()

splitcontent = content.split()
print(splitcontent)
print(len(splitcontent))