import sys
from collections import deque
sys.stdin = open('02.in')
all_vowels = set(['a', 'e', 'i', 'o', 'u']) 

while True:
    s = input()
    if s == 'quit': break
    vowels = []
    s = list(s)
    for l in s:
        l = l.lower()
        if l in all_vowels:
            vowels.append(l)

    q = deque(sorted(vowels))

    for i, l in enumerate(s):
        if l.lower() in all_vowels:
            v = q.popleft()
            if l.isupper():
                v = v.upper()
            s[i] = v

    print(''.join(s))
    