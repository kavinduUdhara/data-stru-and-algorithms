def count(arr):
    if len(arr) <= 0:
        return 0
    else:
        num = arr.pop()
        return 1 + count(arr)
print(count([1,2,3,4,5]))