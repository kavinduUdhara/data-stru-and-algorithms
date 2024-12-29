# https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=false

def extraLongFactorials(n):
    def Factorial(n):
        if n <= 1:
            return n
        else:
            return n * Factorial(n - 1)
    fact = Factorial(n)
    print(fact)

print(extraLongFactorials(30))