word = 'hello'

# len
print(len(word))

# str.upper
print(word.upper())

# str.lower
print(word.lower())

# str.strip
print(word.strip())

# str.split
print(word.split('l'))

# str.replace
print(word.replace('hello', 'bacon'))

# str.title
print(word.title())

# str.swapcase
print(word.swapcase())

# str.join

name = 'John Doe'
print('.'.join(name.split(' ')))
print('.'.join(name.split(' ')).lower())