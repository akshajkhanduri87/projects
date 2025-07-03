# 7/2/25


def reverse_lst(lst):
    lst_backwards = []
    for i in range(len(lst),0,-1):
        lst_backwards.append(lst[i-1])
    print(lst_backwards)

reverse_lst([1,2,3])