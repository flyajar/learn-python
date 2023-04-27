name = input('What\'s your name? ')

print(f'\nHello, {name}')

age = int(input('How old are you? '))

is_teenager = f'\nYou\'re a teenager' if age <= 19 else f'\n You\'re not a teenager'

print(is_teenager)

height = int(input('How tall are you? in inches: '))

if height >= 48:
    print('\nYou\'re tall enough to ride')
else:
    print('\nYou\'re not tall enough to ride')
