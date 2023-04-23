# print(abs(1));

numbers = [1, 2, 3, 4, 5]

print(len(numbers))

for i in range(1, 5):
    print(i)

print(sum(numbers))

squared_numbers = map(lambda x: x ** 2, numbers)

print(f'result when numbers are squared: {list(squared_numbers)}')

even_numbers = filter(lambda num: num % 2 == 0, numbers)

print(f'even numbers are {list(even_numbers)}')

print(f'the smallest number is {min(numbers)}')

print(f'the biggest number is {max(numbers)}')

# supposed that you are given a number, from that number you have to create a list in a desc order

number = 10
print(list(range(number, 0, -1)))
