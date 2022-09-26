import sys
sys.stdin = open('03.in')

mapping = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

while True:
    s = input()
    if s == 'quit': break
    ans = mapping[s[-1]]
    for i in range(len(s)-2, -1, -1):
        if mapping[s[i+1]] > mapping[s[i]]:
            ans -= mapping[s[i]]
        else:
            ans += mapping[s[i]]
    print(ans)