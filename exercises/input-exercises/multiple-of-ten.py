# ask the user for a number,
# and then report whether the number is a multiple of ten

number = int(input('Please give me a number: '))

print(f'{number} is a multiple of ten') if number % 10 == 0 else print(f'{number} is not a multiple of ten')