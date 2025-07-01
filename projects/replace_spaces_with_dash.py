# 7/1/25

def replace_spaces(sentence):
    result = ''
    for character in sentence:
        if character == ' ':
            result += '-'
        else:
            result += character
    return result

print(replace_spaces("Hello this is Akshaj"))