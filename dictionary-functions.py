sample_dict = {"name": "john", "age": 24, "city": "new york"}

# len
print(len(sample_dict))

# keys
print(sample_dict.keys())

# items
print(sample_dict.items())

# get
print(sample_dict.get('name'))

# update
new_dict = {"city": "manila", "gender": "male"}
sample_dict.update(new_dict)
print(sample_dict)

# pop
print(sample_dict.pop('gender'))
