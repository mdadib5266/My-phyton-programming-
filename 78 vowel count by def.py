def vowelcount(str1):
    m = 0
    str1 = str1.lower()
    for i in str1:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            m += 1
    return m

string = str(input('input string: '))
print(vowelcount(string))