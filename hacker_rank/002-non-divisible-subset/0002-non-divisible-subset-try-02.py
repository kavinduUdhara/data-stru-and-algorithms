# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

#time complexity: O(n³)
def nonDivisibleSubset(k, s):
    sub = [{i} for i in s]
    for i in s:
        j = 0
        while j < len(sub):
            add = checkAdd(sub[j], i, k)
            if add:
                sub[j].add(i)
            else:
                if j == len(sub) - 1:
                    sub.append({i})
                    j = len(sub)
            j += 1
    print(sub)
    max = 0
    for i in sub:
        if len(i) > max:
            max = len(i)
    print(max)

def checkAdd(list:list, j:int , k:int) -> bool:
    for i in list:
        if (i + j) % k == 0:
            return False
    return True

k = 5
s = [int(i) for i in "770528134 663501748 384261537 800309024 103668401 538539662 385488901 101262949 557792122 46058493".split(" ")]
sub = []
touched = set()
nonDivisibleSubset(k, s)


