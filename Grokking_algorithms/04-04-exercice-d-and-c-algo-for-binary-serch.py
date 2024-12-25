def biSearch(arr, item, high, low = 0):
    mid = int((low + high) / 2)
    print(low, high, mid)
    if low > high:
        return None
    if arr[mid] == item:
        return mid
    if arr[mid] > item:
        high = mid - 1
        return biSearch(arr, item, high, low)
    if arr[mid] < item:
        low = mid + 1
        return biSearch(arr, item, high, low)
    
arr = [1,5,8,10,15,20]
print(biSearch(arr, 10, len(arr)-1))

        