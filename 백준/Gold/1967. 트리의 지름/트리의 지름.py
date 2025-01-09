import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
dot = int(input())
line = [[] for _ in range(dot + 1)]
par  = [False] * (dot + 1)
while True:
    try:
        a, b, c = map(int, input().split())
        line[a].append((b, c))
        line[b].append((a, c))
        par[a] = True
    except:
        break
ans = 0
def search(n, cst, st):
    global wentlist
    global ans
    wentlist[n] = True
    for i in line[n]:
        if wentlist[i[0]] == True:
            ans = max(cst, ans)
            continue
        newcost = cst + i[1]
        search(i[0], newcost, st)

for i in range(1, dot + 1):
    if par[i] == False:
        wentlist = [False] * (dot + 1)
        search(i, 0, i)
print(ans)