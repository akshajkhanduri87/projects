#6/20/25

def count_vowels(word):
    counter = 0
    for i in range(0,len(word)):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            counter += 1
    print(counter)

count_vowels("banana")