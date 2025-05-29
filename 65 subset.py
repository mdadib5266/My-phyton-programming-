set1 = {1,2,3,4,5,6,7,8,9}
set2 = {4,5,6,11,7}
'''set3 = str(set1).split(',')
set4 = str(set1).split(',')
print(set1.get())
print(set4)
if set(set3) in set(set4):
    print('yes')
else:
    print('no')'''
check = set2.issubset(set1)
if check == True:
    print('second set is a subset of fisrt set')
else:
    print('no')