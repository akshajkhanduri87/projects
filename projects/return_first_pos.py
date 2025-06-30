# 6/30/25

def first_positive(lst):
    for i in range(0,len(lst)):
        if lst[i] > 0:
            print(lst[i])
        

first_positive([0,-1,-2,1,2,3,4])