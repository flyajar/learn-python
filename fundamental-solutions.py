# exercise 1
person = {'name': 'John Doe', 'age': 25, 'city': 'New York', 'country': 'USA'}

name = person.get('name')
age = person.get('age')
city = person.get('city')
country = person.get('country')

print(name)
print(age)
print(city)
print(country)


# exercise 2
def area_of_rectangle(length, width):
    print(length * width)


area_of_rectangle(14, 12)


# exercise 3
def check_number(number):
    if number > 0:
        print(f'{number} is a positive number')
    elif number < 0:
        print(f'{number} is a negative number')
    else:
        print(f'number is zero')


check_number(1)
check_number(-1)
check_number(0)



# exercise 4

def fibonacci_sequence(n):

    sequence = [0, 1]  # Initialize with first two Fibonacci numbers
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]  # Calculate next Fibonacci number
        sequence.append(next_number)  # Add it to the sequence
    return sequence

n = 10
sequence = fibonacci_sequence(n)
print(sequence)