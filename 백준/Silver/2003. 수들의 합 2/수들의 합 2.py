import sys
input = sys.stdin.readline

n,m  = map(int, input().split())
lst = list(map(int ,input().split()))
llst = [0]
for i in range(n):
    llst.append(llst[-1] + lst[i])
l = 0
r = 1
ans = 0

while l < r and r < n + 1:
    nowans = llst[r] - llst[l]
    if nowans == m:
        ans += 1
        r += 1
    elif nowans < m:
        r += 1
    else:
        if l == r - 1:
            r += 1
        l += 1
print(ans)