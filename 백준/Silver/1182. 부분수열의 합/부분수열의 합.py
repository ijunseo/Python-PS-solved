import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
s = []
for i in range(n):
    now = lst[i]
    if s:
        for j in range(len(s)):
            s.append(now + s[j])
    s.append(now)

print(s.count(m))