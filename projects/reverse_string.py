def reverse_string(string):
    for i in range(len(string),0,-1):
        print(string[i-1])

reverse_string("hello")