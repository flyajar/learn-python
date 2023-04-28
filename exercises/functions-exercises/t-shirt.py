# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size='large', message='I love python'):
    print(f'\n Your shirt size is {size} and has a message of "{message}"')


# positional arguments
make_shirt('medium', 'world peace!')

# keyword arguments
make_shirt(message='pineapple pizza', size='large')

make_shirt();

make_shirt('medium')

make_shirt(message='Woof!')
