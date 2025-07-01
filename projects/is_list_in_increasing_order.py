# 7/1/25


def is_increasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            print("not increasing")
    print("proper list")

is_increasing([45,50,55])