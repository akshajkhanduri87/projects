# 7/7/25

def count_occurances(words,target):
    count_of_target = 0
    for i in range(0,len(words)):
        if words[i] == target:
            count_of_target += 1
    print(count_of_target)

count_occurances(["hi","dog","hi"],"hi")