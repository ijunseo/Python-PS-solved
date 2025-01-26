#基本操作
import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

#入力
dot, linenum = map(int, input().split() )
line = [[] for _ in range(dot + 1)]
for _ in range(linenum):
    a, b, c = map(int, input().split())
    line[a].append((b, c))
    line[b].append((a, c))
start, destination = map(int, input().split())

#solve
ans = -1#答

golist = [(-1_000_000_003, start)]#dfsは無理だったので優先度付きキューで実装
went = [False] * (dot + 1)#重複経路をなくす
while golist:
    nowans, now = heapq.heappop(golist)

    if went[now] or -nowans < ans:#既に行ったことあるもしくは行っても意味ないと（ansが更新できないことが分かったと）
        continue

    if now == destination:#到着したら
        ans = max(-nowans, ans)

    went[now] = True

    for i in line[now]:
        nextans = min(i[1], -nowans)
        if went[i[0]]:
            continue
        heapq.heappush(golist, (-nextans, i[0]))

print(ans)