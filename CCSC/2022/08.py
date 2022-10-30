import sys
try:
    sys.stdin = open('08.in')
except:
    pass

T = int(input())
for _ in range(T):
    end = 0
    vowels = set(list('aeiou'))
    ans = []
    s = input()
    for l in s:
        if l == 'z':
            ans.append('bzz')
            end += 1
        elif l in vowels:
            ans.append('Buzz!')
            ans.append('Buzz!')
        else:
            ans.append('Buzz!')
    for _ in range(end):
        ans.append('Buzz!')
    print(''.join(ans))




