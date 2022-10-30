import sys
from collections import Counter
try:
    sys.stdin = open('02.in')
except:
    pass
T = int(input())
for _ in range(T):
    words = sorted(input().split(), key=lambda w: len(w))
    fail = False
    # assume that we are given at least one word
    w = words[0]
    c = Counter(w)
    length = len(w)
    for i in range(1, len(words)):
        c2 = Counter()
        if length == len(words[i]):
            print(f'{words[i-1]} and {words[i]} are the same length')
            fail = True
            break
        for l in words[i]:
            c2[l] += 1
            if l in c and c[l] > 0:
                c[l] -= 1
                length -= 1
        if length > 0:
            temp = [key for key, val in c.items() if val > 0] 
            k = sorted(temp)[0]
            print(f'{words[i]} mising {k} (needed for {words[i-1]})')
            fail = True
            break
        length = len(words[i])
        c = c2
    if not fail:
        print('yes')