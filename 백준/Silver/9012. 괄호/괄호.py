import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    now = input().rstrip()
    flag = 1
    piv = 0
    for i in range(len(now)):
        now_word = now[i]
        if piv < 0:
            print('NO')
            flag = 0
            break
        if now_word == '(':
            piv += 1
        else:
            piv -=1
    if not flag:
        continue
    if not piv:
        print('YES')
    else:
        print('NO')