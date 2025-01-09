import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
dot = int(input())
line = [[] for _ in range(dot + 1)]
for i in range(dot):
    now = list(map(int, input().split()))
    piv = 1
    while now[piv] != -1:
        line[now[0]].append((now[piv], now[piv + 1]))
        piv += 2

ans = [0, 0]
def search(n, cst):
    global wentlist
    global ans
    wentlist[n] = True
    for i in line[n]:
        if wentlist[i[0]] == True:
            if ans[1] < cst:
                ans = [n, cst]
            continue
        newcost = cst + i[1]
        search(i[0], newcost)
wentlist = [False] * (dot + 1)
search(1, 0)
wentlist = [False] * (dot + 1)
search(ans[0], 0)
print(ans[1])