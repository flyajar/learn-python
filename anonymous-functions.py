# anonymous functions are created using the lambda keyword

is_even = lambda num: num % 2 == 0

print(is_even(5))  # false
print(is_even(2))  # true

square_root = lambda num: num ** .5

print(square_root(2))