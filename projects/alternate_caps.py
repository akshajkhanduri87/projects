# 7/10/25

def alternate_capitals(word):
    end_result = ""
    for i in range(0,len(word)):
        if i % 2 == 0:
            end_result += word[i].upper()
        else:
            end_result += word[i].lower()
    print(end_result)

alternate_capitals("hello")