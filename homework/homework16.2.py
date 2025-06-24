# Create a function that takes in a parameter n
# This function should print out all the even numbers from 0 to n
# Ex. if n = 5, then print out 0 2 4

# CODE HERE (Make sure to write your function definition here)

def even_printer(n):
    for i in range(0,n+1):
        if i % 2 == 0:
            print(i)
