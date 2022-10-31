#NOT CORRECT SOLUTION
# making meadian a root of the tree repeating the process for subrtrees seems to work for BST, but it seems that TST might need some changes to make it work
# do not have a proof that this will work, so should use the idea of balancing a BST for TST
# Does right and left rotations change the tree invariant? Seems to work, just need to implement this idea
# actually, my first idea should work like a charm
# There is some issue with this idea, since the last example supposed to be 4 
# although even using pen and paper gives me 3
import sys
from collections import Counter
from pprint import pprint
try:
    sys.stdin = open('05.in')
except:
    pass
def traverse(l, r, depth=0):
    global c, arr, ans
    if l > r:
        return 
    #if l == r:
        #ans = max(depth, depth+c[arr[l]]-1)
        #return
    mid = l + ((r - l) // 2)
    #print(l, arr[mid], r, depth)
    ans = max(depth, depth+c[arr[mid]]-1)
    traverse(l, mid-1, depth+1)
    traverse(mid+1, r, depth+1)
    
    

T = int(input())
for _ in range(T):
    temp = list(map(int,input().split()))
    c = Counter(temp)
    arr = sorted(c)
    l, r = 0, len(arr) - 1
    ans = 0
    #pprint(c)
    #pprint(arr)
    traverse(0, len(arr)-1)
    print(ans)

