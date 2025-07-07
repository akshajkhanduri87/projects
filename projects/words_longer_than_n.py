# 7/7/25

def long_words(words,n):
    longer_words = []
    for i in range(0,len(words)):
        if len(words[i]) > n:
            longer_words.append(words[i])
    print(longer_words)

long_words(["hi","hello","pencil","eraser"],5)