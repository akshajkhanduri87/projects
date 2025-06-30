# 6/30/25

def count_letter(word,letter):
    occurances = 0
    for i in range(0,len(word)):
        if word[i] == letter:
            occurances += 1
    print(occurances)

count_letter("hello","l")