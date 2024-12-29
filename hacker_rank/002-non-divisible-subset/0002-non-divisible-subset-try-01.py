# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

def nonDivisibleSubset(k, s):
    pass

a = 4
x = [int(i) for i in "19 10 12 24 25 22".split(" ")]
s = []
not_included = []
touched = set()
for i in x:
    for j in x:
        if ((i,j) not in touched or (j,i) not in touched) and i != j:
            print(i,j)
            if not((i + j) % a == 0):
                print(" true")
                s.append({i, j})
            else:
                not_included.append({i,j})
            touched.add((i, j))
print(s)
print(not_included)
                    
