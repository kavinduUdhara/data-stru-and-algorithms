def formingMagicSquare(s):
    sum = 0
    for i in s:
        for j in i:
            sum += j
    
    expected_sum = 0
    for i in range(1, len(s) * len(s) + 1):
        expected_sum += i
    return abs(sum - expected_sum)

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
print(formingMagicSquare(s))