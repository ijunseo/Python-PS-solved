import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [str(input().rstrip()) for _ in range(n)]

check = []
for i in range(n):
    for j in range(m):
        try:
            num = int(lst[i][j])
            check.append([num, j])
            break
        except:
            continue

rank = [0 for _ in range(9)]
s = set()
for i in range(9):
    s.add(check[i][1])


for i in range(len(s)):
    s = sorted(s, reverse= True)
    now = s[i]
    for j in range(9):
        if check[j][1] == now:
            rank[check[j][0] - 1] = i + 1

for i in rank:
    print(i)