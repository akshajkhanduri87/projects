# 7/7/25

# This function returns only positive numbers from a list

def removes_negatives(lst):
    positives_only = []
    for i in range(0,len(lst)):
        if lst[i] >= 0:
            positives_only.append(lst[i])
    print(positives_only)

removes_negatives([1,2,3,4,-1,-2])
