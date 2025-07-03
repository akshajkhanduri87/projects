# 7/3/25

def nums_not_div_by_three(n):
    for i in range(0,n+1):
        if i % 3 != 0:
            print(i)

nums_not_div_by_three(45)