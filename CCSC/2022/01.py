import sys
try:
    sys.stdin = open('01.in')
except:
    pass

T = int(input())
for _ in range(T):
    s = list(input())
    sub = input()
    if len(sub) % 2 != 0:
        print('Wut')
        continue
    d = {}
    for i in range(0, len(sub), 2):
        # check
        d[sub[i].lower()] = sub[i+1].lower()

    for i, l in enumerate(s):
        if l.lower() in d:
            a = d[l.lower()]
            if l.isupper():
                a = a.upper() 
            s[i] = a 
    print(''.join(s))


    
