# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

polling_active = True
responses = {}

while polling_active:
    name = input('\nWhat is your name?')
    response = input('\nWhich place do you want to visit?')

    responses[name] = response

    repeat = input('\nWould you like to let other person respond? (yes/no)')

    if repeat == 'no':
        polling_active = False


print('\nPrinting the results:')

for name, response in responses.items():
    print(f'{name} would like to go to {response}')
