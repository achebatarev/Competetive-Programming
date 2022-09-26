import sys
import math
sys.stdin = open('07.in')

T = int(input())
for _ in range(T):
    n = int(input())
    big = math.ceil(n/2)
    ans = []
    ans.extend(list(range(2,big+1))[::-1])
    if n % 2 == 0: 
        ans.extend([1, 1])
    else:
        ans.append(1)
    ans.extend(list(range(2, big+1)))
    print(*ans)