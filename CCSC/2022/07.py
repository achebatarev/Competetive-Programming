# need to convert this input into a tree, need to make sure that my treee is binary, which it should be
# where leafs are either ints or a variables
# this seems to be a very good approach for recursive postorder traversal
# it also seems that each operator node must have exactly two outgoing edges to be valid
# So yeah, I just do post order traversal, and try to return the sorted expression, since it will be easier
# to put into dict
# assuming the valid expression the above idea should work
# I need to store indecies for all repeated expressions
# how do I want to encode those elements, okay,can just use hashlib if all else fails 
# very laxy code so high chance of TLE and MLE

import sys
from collections import defaultdict
from pprint import pprint
try:
    sys.stdin = open('07.in')
except:
    pass

def check(seq, node):
    global memo, ans
    if seq in memo:
        for e in memo[seq]:
            a = sorted([int(e), int(node)])
            ans.append(a)

def postorder(node):
    global mapping, tree, memo
    if node not in tree:
        check(mapping[node], node)
        memo[mapping[node]].append(node)
        return mapping[node]
    a = []
    for child in tree[node]:
        a.append(postorder(child))
    if mapping[node] in ('+', '*'):
        a = sorted(a)
    a = ','.join(a)
    check(a, node)
    memo[a].append(node)
    return a 

T = int(input())
for _ in range(T):
    A = input().split()
    ans = []
    # each node has an id and a value associated with them
    start = A[0]
    mapping = {}
    tree = defaultdict(list)
    # need to identify the cases
    for i in range(1, len(A)):
        B = A[i].split(':')
        parent_id = B[0]
        for i, e in enumerate(B[1].split(',')):
            if i == 0:
                mapping[parent_id] = e
            else:
                tree[parent_id].append(e)
    memo = defaultdict(list) 
    postorder(start)
    if ans:
        ans.sort()
        ans = [f"{{{','.join(map(str, e))}}}" for e in ans]
        print(*ans,sep=', ' )
    else:
        print('No equivalent nodes')


