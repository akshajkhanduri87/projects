# You are given a number n, and you need to print out the sum of all numbers from 0 to n
# Ex. if n = 5, then print out 15 which is 1+2+3+4+5


# CODE HERE

def add_numbers(n):
    total = 0
    for i in range(0,n+1):
        total+=i
    print(total)