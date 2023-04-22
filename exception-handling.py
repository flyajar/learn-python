# exception handling

value1 = 1
value2 = "string"

try:
    output = value1/value2
except TypeError as e:
    print("Error:", e)
else:
    print("Result:", output)
finally:
    print("Finished!")
