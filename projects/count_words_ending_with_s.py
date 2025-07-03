# 7/3/25
# This function counts how many words in a list end with "s"



def count_ending_s(words):
    count = 0
    for word in words:
        if len(word) > 0 and word[-1] == 's':
            count += 1
    print(count)


count_ending_s(["cats","dogs","plane"])
