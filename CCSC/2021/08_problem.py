import sys
sys.stdin = open('08.in')
T = int(input())
for _ in range(T):
    snap, s = input().split()
    snap = int(snap)
    ans = []
    reserve = []
    for i, l in enumerate(s):
        if i % snap == 0:
            reserve.append(l)
        else:
            ans.append(l)
    print(''.join(ans) + ''.join(reserve[::-1]))

