set1 = {1,2,3,4,5,6,7}
set2 = {3,4,5,6,7}
union = set1.union(set2)
intersect = set1.intersection(set2)
unique = union - intersect
print(unique)

symmetric_diff = set1^set2
symmetric_diff1 = set1.symmetric_difference(set2)
print(symmetric_diff,symmetric_diff1)