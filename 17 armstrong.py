num = int(input("input number"))
sum_of_digits = sum(int(digit)**len(str(num)) for digit in str(num))
print(sum_of_digits)