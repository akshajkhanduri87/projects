# 7/3/25
# This function creates a list of odd numbers from 1 to n

def odd_lst(n):
    lst_of_odds = []
    for i in range(0,n):
        if i % 2 != 0:
            lst_of_odds.append(i)
    print(lst_of_odds)

odd_lst(15)