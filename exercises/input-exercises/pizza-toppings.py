# write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value

prompt = "\nPlease enter the toppings that you want to add:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    toppings = input(prompt)
    if toppings != 'quit':
        print(f'Adding {toppings} to your pizza!')
    else:
        break
