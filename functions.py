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
