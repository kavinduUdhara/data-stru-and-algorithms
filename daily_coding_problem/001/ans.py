#time complexity: O(n²)
def findAddUpNums(list, k):
    for i in list:
        for j in list:
            if i + j == k:
                print(f"i: {i}, j: {j}")
                return True
    return False

#time complexity: O(n)
def findAddUpNums1(list, k):
    list = set(list)
    for i in list:
        if k - i in list:
            return True
    return False

print(findAddUpNums([10, 15, 3, 7], 17))
print(findAddUpNums1([10, 15, 3, 7], 17))