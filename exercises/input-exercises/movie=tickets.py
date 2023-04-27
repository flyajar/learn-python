# write a program that asks the user their age and depending on that ticket, you will charge how much

prompt = '\n Please tell me your age: '
prompt += '\n Enter "quit" to end the program '

while True:
    age = input(prompt)

    if age != 'quit':
        if int(age) < 3:
            print('Your ticket is free')
        elif 12 >= int(age) >= 3:
            print('You\'ll be charged $10')
        else:
            print('You\'ll be charged $15')
    else:
        break



