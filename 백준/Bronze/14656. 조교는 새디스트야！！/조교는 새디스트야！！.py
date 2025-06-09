n = int(input())
lst = list(map(int, input().split()))
llst = sorted(lst)

ans= n
for i in range(n):
    if lst[i] == llst[i]:
        ans -= 1
print(ans)