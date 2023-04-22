# Given a non-empty array of integers, return the result of multiplying the values together in order.
# Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24


arr = [2, 2, 2, 2, 2, 2]
sum = arr.pop(0)

for num in arr:
    sum *= num

print(sum)