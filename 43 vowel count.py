string = str(input("String: "))
string = string.lower()
i = 0
for vowel in string:
    if vowel == "a" or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'e' :
        i += 1
print(i)
vowel_count = sum(1 for char in string if char in 'aeiou')
print(vowel_count)