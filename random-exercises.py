# year to century

year = 1945

# year + 99 ensures to round up correctly
# used the integer division // which always return an integer result
print((year + 99) // 100)
