#基本操作
import sys
input = sys.stdin.readline
import heapq
import math
import bisect

#入力
n, m ,k = map(int, input().split())
line = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    line[a].append((b, c))

costlist = [([math.inf] * k) for _ in range(n + 1)]#n回目最短距離を保存するリスト
costlist[1][0] = 0
q = [(1, 0)]
while q:
    now, nowcst = heapq.heappop(q)
    if nowcst > costlist[now][k - 1]:
        continue
    for i in line[now]:
        if nowcst + i[1] >= costlist[i[0]][k - 1]:#新しいk番目の距離より速い距離が更新
            continue
        bisect.insort(costlist[i[0]], nowcst + i[1])#挿入
        costlist[i[0]].pop()#k番目最短距離だったものをpop
        heapq.heappush(q, (i[0], nowcst + i[1]))


for i in range(1, n + 1):
    print('-1'if costlist[i][k - 1] == math.inf else costlist[i][k - 1])
