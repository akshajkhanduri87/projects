# 7/1/25

def remove_zeros(lst):
    result = []
    for x in lst:
        if x != 0:
            result.append(x)
    return result

print(remove_zeros([1,00,1,2,3,0,0,0]))