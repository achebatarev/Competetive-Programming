import sys
sys.stdin = open('01.in')

while True:
    s = input()
    if s == 'quit': break
    arr = list(map(int, s.split()))
    if 0 in arr:
        print('Zero Value')
    else:
        positive = False
        if arr[0] > 0:
            positive = True
        for n in arr[1:]:
            if positive and n > 0:
                print('No')
                break
            elif not positive and n < 0:
                print('No')
                break
            positive = not positive
        else:
            print('Yes')


    