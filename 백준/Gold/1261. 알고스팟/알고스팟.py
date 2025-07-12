import sys 
import heapq
input = sys.stdin.readline

n, m = map(int ,input().split())

map = [list(str(input().rstrip())) for _ in range(m)]
wentset = set()

q = [[0, 0, 0]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    cost, x, y = heapq.heappop(q)
    if (x, y) in wentset:
        continue
    wentset.add((x, y))
    if x == m - 1 and y == n - 1:
        print(cost)
        sys.exit()
    for i in range(4):
        nextx, nexty = x + dx[i], y + dy[i]
        if 0 <= nextx < m and 0 <= nexty < n:
            if map[nextx][nexty] == '1':
                heapq.heappush(q, [cost + 1, nextx, nexty])
            else:
                heapq.heappush(q, [cost, nextx, nexty])