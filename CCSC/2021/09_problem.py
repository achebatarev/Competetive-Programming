import sys
from collections import defaultdict
# isnt this is just a problem of finding if the entire graph is a strongly connected componenent?
# is there a case where the graph is a strongly connected component and does not have a circuit 
sys.stdin = open('09.in')
def dfs(graph, node):
    global visited
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph, child)


T = int(input())
for _ in range(T):
    visited = set() 
    arr = list(map(int, input().split())) 
    # can use this to build our graph using a list, 
    # but problem statment did not specify that all numbers are between 0 and n-1
    #n = arr[0] 
    graph = defaultdict(list)
    reversed_graph = defaultdict(list)
    for i in range(1, len(arr), 2):
        a, b = arr[i], arr[i+1]
        graph[a].append(b)
        reversed_graph[b].append(a)
    dfs(graph, 0)
    if len(visited) != len(graph):
        print('No')
        continue
    visited = set() 
    dfs(reversed_graph, 0)
    if len(visited) != len(graph):
        print('No')
        continue
    print('Yes')
    

    

        

