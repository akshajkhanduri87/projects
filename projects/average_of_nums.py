# 7/2/25

def average(lst):
    sum_of_nums = 0
    for i in range(0,len(lst)):
        sum_of_nums += lst[i]
    print(sum_of_nums / len(lst))

average([1,2,3,4,5,6])