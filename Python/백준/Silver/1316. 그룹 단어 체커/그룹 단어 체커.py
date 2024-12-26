import sys
input = sys.stdin.readline
num = int(input())
ans = 0
for i in range(num):
    anslist = list(input().strip())
    imsilist = []
    now = ''
    while anslist:
        a = anslist.pop()
        if a not in imsilist:
            imsilist.append(a)
        if a in imsilist and imsilist[-1] == a:
           if len(anslist) == 0:
              ans += 1
              break
           else:
            continue
        elif a in imsilist and imsilist[-1] != a:
            break
print(ans)

