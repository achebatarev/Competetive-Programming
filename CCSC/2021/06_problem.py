import sys
sys.stdin = open('06.in')

T = int(input())

for _ in range(T):
    arr = input().split()
    n = int(arr[0])
    arr = arr[1:]
    
    for i in range(n*2 - 1):
        print(arr[i%2], end='')
    print()

