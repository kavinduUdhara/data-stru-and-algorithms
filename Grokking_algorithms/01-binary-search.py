def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        print(f'mid {str(mid):<2s} | low {str(low):<2s} | high {str(high):<2s}')
        guess = list[mid]
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
        if guess == item:
            return mid
    return None

print(binary_search([1,5,7,8,10], 9))