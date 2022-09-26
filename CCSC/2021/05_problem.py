# implemintation seems to be a little bit tricky for this one
# I can use Counter to easily find scores for each category
# but, I am not sure how I can keep track of who got what place for each of the categories
# can have a defaultdict for each category and keep track of a score for each value, thats a lot of passes, but it is O(n) and it is easy to code
# 100% sure there is a better way, but this is good enough for now 
from pprint import pprint
from collections import Counter
import sys
sys.stdin = open('05.in')

T = int(input())
for league in range(T):
    print(f'League {league+1}')
    n, m = map(int, input().split())
    owners = [0] * n
    categories = [{} for _ in range(m)]
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    # go over each category and keep track of how much points certain number scores in each of the categories
    for i, category in enumerate(zip(*arr)):
        c = Counter(category)
        total = 1
        for num, freq in sorted(c.items()):
            score =  sum(range(total, total+freq))/freq
            categories[i][num] = score 
            total += freq

    # go through all the owners and calculate their total points
    for i in range(n):
        for j in range(m):
            num = arr[i][j]
            owners[i] += categories[j][num]

    print(*owners, sep='\n') 

        

    