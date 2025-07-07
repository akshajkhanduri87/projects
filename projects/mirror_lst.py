# 7/7/25

def mirror_lst(lst):
    backwards = []
    for i in range(1,len(lst)+1):
        backwards.append(lst[-i])
    print(backwards)
    print(lst)

mirror_lst([1,2,3])
        