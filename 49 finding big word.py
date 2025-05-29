text = str(input('enter the text: '))
count = text.split()
longest_word = max(count,key=len)
print('longest word: ',longest_word)