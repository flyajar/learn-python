# if statement

number = 10

if number > 0:
    print(f'The number {number} is greater than 0')
elif number == 10:
    print(f'The number is exactly {number}')
else:
    print(f'The number {number} is less than 0')

def lovefunc( flower1, flower2 ):
    return flower1 % 2 != 0 and flower2 % 2 != 0 