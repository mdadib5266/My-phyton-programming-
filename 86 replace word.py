
with open('sample.txt','r') as file:
    content = file.read()

print(content)
word_to_replace = str(input('word to replace: '))
new_word = str(input('new_word: '))
content = content.replace(word_to_replace,new_word)

with open('sample.txt','w') as file:
    file.write(content)

print(f'{word_to_replace},{new_word}')
print(content)