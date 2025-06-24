# You are given an array of numbers (ex. [10, 5, 9, 12, 3, 1, 6])
# Print out the sum of the whole array

# Example 1:
# arr = [10, 5, 9, 12, 3, 1, 6]
# print 10 + 5 + 9 + 12 + 3 + 1 + 6 = 46

# CODE HERE:
arr = [10, 5, 9, 12, 3, 1, 6]
sum = 0
for i in range(0,7):
    sum += arr[i]

print(sum)