# 6/30/25

def has_negative(lst):
        for i in range(0,len(lst)):
            if lst[i] < 0:
                print("True")

has_negative([0,1,2,3,-1,-2])