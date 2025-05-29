lst = [1,2,3,5,7,3,65,32,65,77,42]
max1 = max(lst)
index_max = index(max1)
popped_list = lst.pop(index_max)
max_pop_list = max(lst)
print(max_pop_list)