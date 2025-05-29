list1 = set([1,2,3,4,5,6,7])
list2 = set([5,6,7,8,9])
'''similar = list1.intersection(list2)
list1 = list(list1)
list2 = list(list2)
list3 = similar.remove(list1)
list4 = similar.remove(list2)'''
unique_values = list(list1 ^ list2)
print(unique_values)