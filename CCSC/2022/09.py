# is brute force good enough?
# could be something like bruteforce with memo, we can either place element at this position and skip over 1, or go to next, element, can it overlap thou?
# I think so, so just create one memo, for all of them
import sys
from pprint import pprint
try:
    sys.stdin = open('09.in')
except:
    pass

memo = [None] * (25 + 1)
def solve(pos=25):
    global memo
    if pos <= 0:
        return 0
    if memo[pos] is not None:
        return memo[pos]
    a = solve(pos-1)
    b = solve(pos-2) + 1
    memo[pos] = a + b
    return memo[pos] 

solve()
T = int(input())
for _ in range(T):
    n = int(input())
    # + 1 for the case when we place no zombies
    print(memo[n] + 1)
