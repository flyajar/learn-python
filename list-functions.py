my_list = [1, 2, 3, 4, 5]

# len
print(len(my_list))

# extend
my_list.extend([6, 7])
print(my_list)

# insert
my_list.insert(7, 8)
print(my_list)

# reverse
my_list.reverse()
print(my_list)

# pop
print(my_list.pop())

# append
my_list.append(1)
print(my_list)

my_list.sort()
print(my_list)

new_list = sorted(my_list)[:2]
print(new_list)
