# 7/3/25

def count_capitals(word):
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_of_capitals = 0
    for letter in word:
        if letter in capitals:
            number_of_capitals += 1
    print(number_of_capitals)

count_capitals("HellOThereE")
