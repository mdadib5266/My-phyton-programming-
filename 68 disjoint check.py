set1 = {1,2,3,4,5,6,6,7,8,0}
set2 = {11,23,45}
unique = set1.intersection(set2)
print(unique)
if unique == set():
    print('disjoint')
else:
    print('not disjoint')