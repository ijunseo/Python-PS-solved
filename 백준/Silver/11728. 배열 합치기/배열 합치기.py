import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))

l = []
for _ in range(len(lst)):
    now = list(map(int, input().split()))
    for i in now:
        l.append(i)
print(*sorted(l))