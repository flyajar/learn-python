def greet(name):
    print(f"hello! my name is {name}")


greet('john')


def favorite_food(food='fried chicken'):
    print(f'my favorite is {food}')


favorite_food('lasagna')


# define a type hint, python doesn't perform strict type checking
def number(num: int):
    print(num)


number(1)


# keyword arguments

def describe_pet(animal_type, animal_name):
    print(f'\nI have a {animal_type}')
    print(f'\nMy {animal_type}\'s name is {animal_name}')

describe_pet(animal_name='Fyodor', animal_type='cat')
