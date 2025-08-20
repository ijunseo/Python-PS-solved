n = int(input())
k = int(input())

lst = [True] * (n+1)
for i in range(2, int(n ** 0.5) + 1):
    if lst[i]:
        for j in range(2 * i, n + 1, i):
            lst[j] = False
            
ans = [1]*(n + 1)
for i in range(2, n + 1):
    if lst[i] and i > k:
        for j in range(i, n + 1, i):
            ans[j] = 0
print(sum(ans) - 1)