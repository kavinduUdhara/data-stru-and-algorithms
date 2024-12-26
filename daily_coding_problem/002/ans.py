#time complexity O(n²)
def findProOtherElements(list:list) -> list:
    newList = []
    for i in range(len(list)):
        pro = 1
        for j in range(len(list)):
            if i != j:
                pro *= list[j]
        newList.append(pro)
    return newList

#time complexity O(n)
def findProOtherElements1(list:list) -> list:
    product = 1
    for i in list:
        product *= i
    newList = []
    for i in list:
        newList.append(int(product / i))
    return newList

def findProOtherElements2(lst):
    n = len(lst)
    if n == 0:
        return []

    # Initialize prefix and suffix products
    prefix = [1] * n
    suffix = [1] * n

    # Calculate prefix products
    for i in range(1, n):
        print(f"i: {i}, prefix[i]: {prefix[i]} | prefix[i-1]: {prefix[i-1]} | list[i-1]: {lst[i-1]}")
        prefix[i] = prefix[i-1] * lst[i-1]
    print(prefix)
    # Calculate suffix products
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * lst[i+1]
    print(suffix)
    # Calculate the result using prefix and suffix products
    result = [prefix[i] * suffix[i] for i in range(n)]

    return result


print(findProOtherElements([3,2,1]))
print(findProOtherElements([1,2,3,4,5]))
print(findProOtherElements1([3,2,1]))
print(findProOtherElements1([1,2,3,4,5]))
print(findProOtherElements2([1,2,3,4,5]))