import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())

q = []

dot_lst = []

for i in range(n):
    x, y = map(int, input().split())
    dot_lst.append((x, y))

parlst = [i for i in range(n)]
lenglst = []

for i in range(m):
    d1, d2 = map(int, input().split())
    lenglst.append((0, d1 - 1, d2 - 1))

for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        leng = math.dist(dot_lst[i], dot_lst[j])
        lenglst.append((leng, i, j))

ans = 0

def find(a):
    if parlst[a] != a:
        parlst[a] = find(parlst[a])
    return parlst[a]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    if ra > rb:
        parlst[ra] = rb
    else:
        parlst[rb] = ra
        
lenglst.sort(reverse = True)

while lenglst:
    nowlen, dot1, dot2 = lenglst.pop()
    if find(dot1) == find(dot2):
        continue
    else:
        union(dot1, dot2)
        ans += nowlen

print("{:.2f}".format(ans))