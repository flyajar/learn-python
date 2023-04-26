# for loop

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)


print("=======")

# while loop

count = 1
while count <= 5:
    print(count)
    count += 1


def repeat(number, string):
    initial_number = 1
    new_string = ''
    while initial_number <= number:
        new_string += string
        initial_number += 1

    return new_string


output = repeat(10, 'a')
print(output)