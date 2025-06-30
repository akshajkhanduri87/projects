# 6/30/25

def sum_lst(lst):
    counter = 0
    for i in range(0,len(lst)):
        counter += lst[i]
    print(counter)

sum_lst([5,10,15])