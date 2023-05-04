# sort dictionary keys

new_dict = {'b':1, 'c':4, 'e':3, 'a':5, 'd':2}

print(sorted(new_dict))


# sort dictionary values

new_dict = dict(sorted(new_dict.items(), key=lambda item: item[1]))
print(new_dict)