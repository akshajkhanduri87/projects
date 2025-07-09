# 7/9/25

def count_consonants(word):
    vowels = "aeiouAEIOU"
    consonant_count = 0
    for letter in word:
        if letter.isalpha() and letter not in vowels:
            consonant_count += 1
    print(consonant_count)

count_consonants("Elephant")