import sys 
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

lst.sort()
ans = 0
aa = 0

for i in range(n):
    a = 0
    nowa, nowb = lst[i]
    for j in range(i, n):
        if nowa > lst[j][1]:
            a += nowa
            a -= lst[j][1]
    
    if a > ans:
        aa = nowa
        ans = a
        continue

print(aa)
