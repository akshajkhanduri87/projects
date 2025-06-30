# 6/30/25

def sum_until_negative(lst):
    sum = 0
    for i in range(0,len(lst)):
        if lst[i] > 0:
            sum += lst[i]
        elif lst[i] < 0:
            break
    print(sum)


sum_until_negative([1,2,3,-1,4,5,6])