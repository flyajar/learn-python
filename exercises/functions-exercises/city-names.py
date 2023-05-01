# Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:

def city_country(city, country):
    return f'{city.title()},{country.title()}'


print(city_country('tokyo', 'japan'))