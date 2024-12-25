def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def RecSum(arr):
    if len(arr) <= 0:
        return 0
    else:
        num = arr.pop()
        return num + RecSum(arr)

print(sum([1,5,4,10,5]))
print(RecSum([]))
print(RecSum([1,5,4,10,5]))