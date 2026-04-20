def reverse_lst(lst):
    reversed_lst = []
    for i in range(len(lst),0,-1):
        reversed_lst.append(lst[i-1])
    return reversed_lst

print(reverse_lst([1,2,3,4,5]))