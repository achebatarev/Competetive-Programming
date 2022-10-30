# I am thinking of something like topological sorting in here, we simply construct a graph of all unknowns, and then just try to traverse it, using topological sorting
# topological sorting will help with identifying the order of operations
# I assume that we can only write to each register once, otherwise, it is impossible to identify the order of operations
# Another thing that I need to identify how I am going to calculate values of the registers
# This problem might even be easier to solve with an event loop
# order of operations matter
# this problem is so much easier to solve with the software engineering tools, rather than as an algorithmic question
# why dont I just build a graph, then traverse it in the topological order, and as I go I just will be evaluating registers to certain values
# so I need to store 3 pieces of info about each register: operation, y and z
# and then as we traverse our graph we check if can evaluate current register, if not we stop
# I think this problem is easier to think about if solved using the iterative approach of finding a topological sorting, 
# because it allows us to immediately evaluate values of our registers, rather then creating topological sorting first
# Even though both versions are viable, I am a bit more rusty with iterative approach so thats what I am going to go with
# If I got an element in queue it means that we already fullfiled the requirements for it and it can be processed
from collections import defaultdict, deque
from pprint import pprint
import sys
try:
    sys.stdin = open('04.in')
except:
    pass

def evaluate(r):
    global ops, values
    op, y, z = ops[r]
    if y[0] == 'r':
        y = values[y]
    else:
        y = int(y[1:])
    
    if z[0] == 'r':
        z = values[z]
    else:
        z = int(z[1:])

    if op == 'add':
        return y + z
    if op == 'mul':
        return y * z
    if op == 'sub':
        return y - z
    # could cause probelms with negative numbers, also if z is 0, we will have a problem
    if op == 'div':
        return y // z

while True:
    T = int(input())
    if T < 0: break
    values = {} 
    indegree = defaultdict(int)
    q = deque()
    ops = {}
    graph = defaultdict(list)
    for _ in range(T):
        op, x, y, z = input().split()
        # get rid of ',' at the end of x and y
        x, y = x[:-1], y[:-1]
        ops[x] = (op, y, z)
        # handles the case where y and z are the same register
        if y[0] == 'r' and y == z:
            indegree[x] += 1
            graph[y].append(x)
        else:
            if y[0] == 'r':
                indegree[x] += 1
                graph[y].append(x)
            if z[0] == 'r':
                indegree[x] += 1
                graph[z].append(x)
        if indegree[x] <= 0:
            q.append(x)
    while q:
        node = q.popleft()
        values[node] = evaluate(node)
        for child in graph[node]:
            indegree[child] -= 1
            if child not in values and indegree[child] <= 0:
                q.append(child)
    if values:
        print(' '.join([f'{r}={val}'for r, val in sorted(values.items(), key=lambda x: x[0])]))
    else:
        print('No known constants')





