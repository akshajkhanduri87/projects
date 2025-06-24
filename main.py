

def num_checker(arr):
    smallest = arr[0]
    for i in range(0,len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
    return smallest

print(num_checker([5,6,7,8,2,1]))