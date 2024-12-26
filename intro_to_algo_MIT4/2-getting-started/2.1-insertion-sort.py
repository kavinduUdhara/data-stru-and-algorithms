def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    print(f'key: {key}')
    j = i - 1
    print(f'j: {j}')
    while j >= 0 and key < arr[j]:
      print(f'arr[j]: {str(arr[j]):<2s} | arr[j + 1]: {str(arr[j + 1]):<2s} | key: {key} | j: {j} | key < arr[j]: {key < arr[j]} | arr: {arr}')
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr

arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))