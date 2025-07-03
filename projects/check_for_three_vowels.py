# 7/3/25

def check_for_3_vowels(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for v in vowels:
        vowel_count += 1
    if vowel_count >= 3:
        print("Has greater than or equal to 3 vowels")
    else:
        print("Doesn't have 3 vowels")
    

check_for_3_vowels("aeiou")

