import sys
sys.stdin = open('10.in')
def difference(s1, s2):
    if len(s2) > len(s1):
        return 2
    alphabet = set(list('abcdefghiklmnopqrstuvwxyz'))
    diff = 0
    i = 0
    for l in s1:
        if l not in alphabet:
            continue
        if i >= len(s2) or l != s2[i]:
            diff += 1
            continue
        i += 1
    return diff

T = int(input())
for _ in range(T):
    s = list(map(str.lower, input().split()))
    santa = 0 
    claus = 0 
    for word in s:
        diff = difference(word, 'santa') 
        if diff == 0:
            santa = 1000
            break
        elif diff == 1:
            #print('Santa', word)
            santa += 1
        diff = difference(word, 'claus') 
        if diff == 0:
            claus = 1000
            break
        elif diff == 1:
            #print('Claus', word)
            claus += 1
    if claus + santa == 1:
        print('yes')
    else:
        print('no')

    