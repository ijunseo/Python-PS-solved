import sys
n = int(input())
lst = [int(input()) for _ in range(n)]
mx = 20001
ans = 0

while lst:
    num = lst.pop()
    if num < mx:
        mx = num
    else:
        ans += num - mx + 1
        mx -= 1
print(ans)