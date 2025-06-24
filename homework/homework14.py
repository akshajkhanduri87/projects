# Create a function that takes in a number and a list, and checks if that number is in the list
# then, it will return the index where the element is
# if the element is not in the list, then print out -1

# Example call: contains([1, 2, 3, 4, 5], 4)
# this call will print out 3 since 4 is located at index 3

# Example call: contains([1, 2, 3, 4, 5], 6)
# this call will print out -1 since 6 is not in the list


# What you should be thinking about:
# identify the inputs (parameters)
# what are my inputs (do I even have any inputs?)

# what am I ouputting (I need to print out the output)
# create function name and definition


# CODE GOES BELOW:


def contains(number,lst):
    for i in range(0,len(lst)):
        if lst[i] == number:
            print(i)
    print(-1)