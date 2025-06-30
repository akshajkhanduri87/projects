# 6/30/25

def sum_evens(lst):
    counter = 0
    for i in range(0,len(lst)):
        if lst[i] % 2 == 0:
            counter += lst[i]
    print(counter)

sum_evens([1,2,3,4,5])
