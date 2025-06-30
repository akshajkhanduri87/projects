# 6/30/25

def print_odds(lst):
    for i in range(0,len(lst)):
        if lst[i] % 2 != 0:
            print(lst[i])

print_odds([5,10,15,20])