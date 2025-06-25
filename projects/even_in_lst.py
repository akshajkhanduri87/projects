# 6/24/25

def print_even_nums(numbers):
    for i in range(0,len(numbers)):
        if numbers[i] % 2 == 0:
            print(numbers[i])

print_even_nums([5,10,15,20])