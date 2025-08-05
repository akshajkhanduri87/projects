# 8/5/25

def remove_negatives(lst):
    positives_only = []
    for i in range(0,len(lst)):
        if lst[i] >= 0:
            positives_only.append(lst[i])
    print(positives_only)

remove_negatives([1,2,3,-1,-2,-3])