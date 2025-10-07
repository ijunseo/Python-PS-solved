import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
now = 1
anslst = []
ans = 0

for _ in range(k):
    anslst.append(int(input()))
    
for apple in anslst:
    if now <= apple and now + (m - 1) >= apple:
        pass
    elif now > apple:
        ans += abs(apple - now)
        now = apple
    else:
        ans += apple - (m - 1) - now
        now = apple - (m - 1)
print(ans)