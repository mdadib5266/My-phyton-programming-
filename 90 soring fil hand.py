with open('sample.txt','r') as file:
    words = file.read().split()

sorted_words = sorted(words)

with open('sorted_word.txt','w') as file:
    text = file.write(' '.join(sorted_words))
with open('sorted_word.txt','r') as file:
    content = file.read()

print(content)