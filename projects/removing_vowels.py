# 7/3/25

def removing_vowels(word):
    vowels = "aeiouAEIOU"
    for v in vowels:
        word = word.replace(v,"")
    print(word)

removing_vowels("jet")