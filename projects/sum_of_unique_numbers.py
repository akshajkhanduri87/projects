# 7/9/25    

def sum_unique_numbers(numbers):
    total = 0
    for num in numbers:
        if numbers.count(num) == 1:
            total += num
    print(total)

sum_unique_numbers([1,2,2,3,4,5,5,6])