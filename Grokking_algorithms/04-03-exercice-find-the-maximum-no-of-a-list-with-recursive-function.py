def findMax(arr, max = 0):
    if len(arr) <= 0:
        return max
    else:
        num = arr.pop()
        if max < num:
            max = num
        return findMax(arr, max)

print(findMax([1,2,10,9,5,20,7]))