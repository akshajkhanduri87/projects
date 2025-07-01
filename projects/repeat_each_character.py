# 7/1/25

def repeat_characters(word):
    result = ""
    for char in word:
        result += char * 2
    return result

result = repeat_characters("hello")
print(result)