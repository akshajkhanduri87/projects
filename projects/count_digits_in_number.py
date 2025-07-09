# 7/9/25

def count_digits(n):
    if n < 0:
        n = -n
    
    if n == 0:
        print("1")
    
    count_of_digits = 0
    while n > 0:
        n = n // 10
        count_of_digits += 1
    print(count_of_digits)

count_digits(12345)