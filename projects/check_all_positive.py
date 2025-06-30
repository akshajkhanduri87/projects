# 6/30/25

def all_positive(lst):
    for i in range(0,len(lst)):
        if lst[i] < 0:
            print("Not all values are positive in lst")
        

all_positive([5,10,15,20,-1,-2])