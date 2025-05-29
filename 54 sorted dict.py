my_dict = {
    'roll':98,"earning":0,'age':21
}
my_dict = dict(sorted(my_dict.items(),key=lambda item:item[1]))
print(my_dict)