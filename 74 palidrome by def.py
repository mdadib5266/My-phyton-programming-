def string(str):
    if str == str[::-1]:
        return True
    return False
def string1(str):
    return str == str[::-1]
str1 = str(input('enter string: ').lower().replace("",""))
print(string(str1),string1(str1))