# this is a famous dp problem, but instead of n coins, we got fixed number, which is 5
# So the time complexity is O(5*target)
# however, there are two dp problems here, in one, not sure if I can combine them or just solve them seperatly since max target is so low
# this code can be improved, A LOT, use only to udnerstand general idea
# Top down might be even better in this case, also creating separate functions for each dp is also a better way to go about this
import sys
from pprint import pprint
try:
    sys.stdin = open('03.in')
except:
    pass

coins = [2,3,6,7,8]
dp_min = [[] for _ in range(100 + 1)]
# can do 1d dp but too much effort changin up code or writing another function
dp_ways = [[0] * len(coins) for _ in range(100+1)]
for i in range(len(coins)):
    dp_ways[0][i] = 1
i = 1
while True:
    target = int(input())
    if target < 0: break
    # top down might even be faster cause of memo
    # but bottom up is cooler, so ... 
    # actually, I can do the same thing as memo here
    # but it still goes over targets that are a failure, but that is a problem for another day
    # can use another dp_table to check for that, or not, too much extra code to handle it, will do another day, if ever ...
    for x in range(1, target+1):
        if dp_min[x]:
            continue
        check = False
        for j, c in enumerate(coins):
            if x - c >= 0: 
                dp_ways[x][j] = dp_ways[x-c][j] + dp_ways[x][j-1]
                # The smallest sequence
                if (x - c == 0 or dp_min[x-c]) and (not check or len(dp_min[x-c]) + 1 < len(dp_min[x])):
                    dp_min[x] = [c] + dp_min[x-c]
                    check = True
            else:
                dp_ways[x][j] = dp_ways[x][j-1]
    i += 1
    #pprint(dp_ways)
    print(dp_ways[target][-1], end=' ')
    print('{', ','.join(map(str, dp_min[target])) ,'}', sep='')



