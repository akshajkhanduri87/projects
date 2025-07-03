# 7/3/25


def sum_multiples_5(n):
    sum_of_multiples = 0
    for i in range(0,n):
        if i % 5 == 0:
            sum_of_multiples += i
    print(sum_of_multiples)

sum_multiples_5(20)