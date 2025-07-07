# 7/7/25

def find_first_long_word(words):
    for i in range(0,len(words)):
        if len(words[i]) > 6:
            print(words[i])
            break

find_first_long_word(["hello","airplane","cat"])