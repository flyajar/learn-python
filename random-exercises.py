# year to century

year = 1945

# year + 99 ensures to round up correctly
# used the integer division // which always return an integer result
print((year + 99) // 100)


# human years to cat and dog years
# 1st human year = 15 cat,dog years
# 2nd human year = 9 cat,dog years
# 3++ human year = 4 cat, 5dog years

def calculate_pet_years(human_years):
    if human_years < 1:
        raise ValueError("human_years must be a positive integer greater than or equal to 1")

    # Define a dictionary to map human_years to cat_years and dog_years
    years_map = {1: 15, 2: 24}

    # Calculate cat_years and dog_years based on human_years
    cat_years = years_map.get(human_years, 15 + 9 + 4 * (human_years - 2))
    dog_years = years_map.get(human_years, 15 + 9 + 5 * (human_years - 2))

    # Return as list [human_years, cat_years, dog_years]
    return [human_years, cat_years, dog_years]


calculate_pet_years(3)

# get the quarter of a month in where it belongs

m = 11
r = (m + 2) // 3

# make each word starts with capital letter

quote = "How can mirrors be real if our eyes aren't real"
words = quote.split(' ')
new_words = [word.capitalize() for word in words]

print(new_words)

# remove every other element in a list

numbers = [1, 2, 3, 4, 5, 6, 7]
bools = [True, True, False, False, False, True, True]

new_list = bools[::2]
print(new_list)
