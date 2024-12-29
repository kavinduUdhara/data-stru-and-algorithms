# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

#time complexity O(n + k)
def nonDivisibleSubset(k, s):
    reminders = get_reminders(s, k)
    total = min(reminders.get(0, 0), 1)
    for i in range(1, int(k / 2) + 1):
        if i == k - i:
            total += min(reminders.get(i,0), 1)
        else:
            total += max(reminders.get(i,0), reminders.get(k - i,0))
    return total


def get_reminders(s:list, k:int) -> dict:
    result = {}
    for i in s:
        reminder = i % k
        result[reminder] = result.get(reminder, 0) + 1
    return result

k = 5
s = [int(i) for i in "770528134 663501748 384261537 800309024 103668401 538539662 385488901 101262949 557792122 46058493".split(" ")]
sub = []
touched = set()
nonDivisibleSubset(k, s)


