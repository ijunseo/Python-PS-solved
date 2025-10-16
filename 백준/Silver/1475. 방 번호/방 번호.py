import sys
input = sys.stdin.readline

n = input().rstrip()
ans = [0] * 10
for i in range(len(n)):
    now = int(n[i])
    if now == 6 or now == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[now] += 1
 
print(max(ans))