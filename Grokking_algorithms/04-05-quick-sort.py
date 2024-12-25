def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        grater = [i for i in arr[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(grater)
    
print(quickSort([5,7,6,9,10,1,20]))