# 7/1/25

def count_words(sentence):
    word_count = 0
    for i in range(0,len(sentence)):
        if sentence[i] == " ":
            pass
        word_count += 1
    print(word_count)

count_words("Hello Sir")