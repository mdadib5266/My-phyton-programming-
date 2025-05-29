char = str(input("input the word"))
char = char.lower()
'''
if len(char) == 1:
    if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' or char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print("the word is a vowel")
    else:
        print("the word is a constant")
else:
    print("invalid input")'''
if char in 'aeiou':
    print("the alphabet is a vowel")
else:
    print("the alphabet isnt a vowel")