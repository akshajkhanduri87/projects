def transform_list(nums):
    result = []
    
    for num in nums:
        if num % 2 == 0:
            result.append(num * 2)
        else:
            result.append(num + 1)
    
    return result

def count_words(sentence):
    if sentence == "":
        return 0
    return len(sentence.split(" "))