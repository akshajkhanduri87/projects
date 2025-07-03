# 7/3/25

def common_elements_in_lst(lst1,lst2):
    common_elements = []
    for item in lst1:
        if item in lst2 and item not in common_elements:
            common_elements.append(item)
    print(common_elements)

common_elements_in_lst([1,2,3],[1,2,3,4])
         