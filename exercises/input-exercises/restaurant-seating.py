# write a program that asks the user how many people are in their dinner group
# if the answer is more than eight, print a message saying that they're table is not yet ready
# Otherwise, report that their table is ready

number_of_people = int(input('Hello! How many people do you need for a table? '))

if number_of_people >= 8:
    print('Your table is not yet ready')
else:
    print('Your table is now ready')