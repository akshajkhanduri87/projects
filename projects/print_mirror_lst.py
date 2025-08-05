# 8/5/25
def mirror_lst(lst):
    backwards = []
    for i in range(1,len(lst)+1):
        backwards.append(lst[-i])
    print(lst)
    print(backwards)

mirror_lst([1,2,3])