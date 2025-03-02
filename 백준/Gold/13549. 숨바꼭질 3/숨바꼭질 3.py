#基本操作
import sys
input = sys.stdin.readline
from collections import deque

#input
a, b = map(int, input().split())

#solve
q = deque([(a, 0)])#BFS
lenlst = [0] * 100001

while q:
    now , cst= q.popleft()#現在の位置と費用
    if now == b:#到着したら
        break
    if cst > lenlst[now]:#もし更新されて計算する必要ないなら
        continue
    lenlst[now] = cst

    for i in [now + 1, now - 1]:
        if i < 0 or i > 100000:
            continue
        if not lenlst[i]:#未訪問なら
            lenlst[i] = cst + 1
            q.append((i, cst + 1))
        if lenlst[i] > cst + 1:#より効率よくいけるなら
            lenlst[i] = cst + 1
            q.append((i, cst + 1))
    #二倍瞬間移動は追加コスト０なので
    if now * 2 < 0 or now * 2 > 100000:
            continue
    if not lenlst[now * 2]:#未訪問なら
        lenlst[now * 2] = cst
        q.append((now * 2, cst))
    if lenlst[now * 2] > cst:#より効率よくいけるなら
        lenlst[now * 2] = cst
        q.append((now * 2, cst))

print(lenlst[b])