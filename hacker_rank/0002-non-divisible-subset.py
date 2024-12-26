# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

def nonDivisibleSubset(k, s):
    pass

k = 3
x = [int(i) for i in "19 10 12 24 25 22".split(" ")]
checked = {}
for i in x:
    for j in x:
        if i != j:
            if not((i, j) in checked or (j, i) in checked):
                checked[(i, j)] = i + j
print(checked)
true = []
false = []
for key, value in checked.items():  # Corrected `checked.items` to `checked.items()`
    if value % k == 0:  # Using the value directly instead of `checked[i]`
        true.append(key)
    else:
        false.append(key)
print(true)
print(false)