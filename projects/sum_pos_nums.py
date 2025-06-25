# 6/24/25

def sum_positive(numbers):
    even_counter = 0
    for i in range(0,len(numbers)):
        if numbers[i] >= 0:
            even_counter += numbers[i]
    print(even_counter)


sum_positive([-1,-2,0,1,2])