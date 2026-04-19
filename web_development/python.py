# Problem 3
def remove_first_last(s):
    result = ""
    for i in range(1, len(s) - 1):
        result += s[i]
    return result

print(remove_first_last("python"))

# Problem 2
def sum_first_half(nums):
    half = (len(nums) + 1) // 2  
    total = 0
    for i in range(half):
        total += nums[i]
    return total

print(sum_first_half([1,2,3,4]))

# Problem 1


