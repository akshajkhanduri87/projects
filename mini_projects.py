def unique_lst(lst):
    for i in range(0,len(lst)):
        if lst[i] == lst[i-1]:
            del lst[i]
        print(lst)

unique_lst([11,2,11,3])