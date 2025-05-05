import sys
input = sys.stdin.readline

n  = sorted(str(input()).rstrip())
ans = 0
if n[0] != '0':
    print('-1')
    sys.exit()
else:
    for i in n:
        i = int(i)
        ans += i
        ans %= 3
if not ans:
    for i in n[::-1]:
        print(i, end ='')
else:
    print('-1')