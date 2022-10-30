# is this just simply about building all of the combinations? can even use pythong library since n is so small 
# we can simply sort and then first math.ceil(n / 2) will be our best combination, so we can even use math to find those combinations
# this problem seems super simple, what am I missing
import sys
import math
try:
    sys.stdin = open('06.in')
except:
    pass

def factorial(n, memo={}):
    if n <= 1:
        return 1
    if n in memo: 
        return memo[n]
    memo[n] = factorial(n-1) * n
    return memo[n]

T = int(input())
for _ in range(T):
    words = input().split()
    words.sort(key=lambda x: len(x))
    n = len(words)
    r = math.ceil(n/2)
    ans = int((factorial(n) / (factorial(n-r) * factorial(r))))
    print(ans, ' '.join(sorted(words[:r])), sep=':')

