dict1 = {
    'name':'adib','age':21,'roll':98
}
keys = dict1.keys()
values = dict1.values()
dictn = dict(zip(values,keys))
print(dictn)

swapped = {value:key for key,value in dict1.items()}
print(swapped)

print(dict1.items())