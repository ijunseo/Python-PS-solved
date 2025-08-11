import sys
import math
input = sys.stdin.readline
row, col = map(int, input().split())
lst = [list(map(str, input().rstrip())) for _ in range(row)]


first = [[set(lst[0][0]), 0, 0]]
ans = 0
next = [(1 , 0), (-1 , 0), (0 , 1), (0 , -1)]

while first:
    nows , nowr, nowc = first.pop()
    ans = max(ans, len(nows))
    for i in range(4):
        nexr = nowr + next[i][0]
        nexc = nowc + next[i][1]
        if 0 <= nexr < row and 0 <= nexc < col:

            if lst[nexr][nexc] in nows:
                continue
            news = nows.copy()
            news.add(lst[nexr][nexc])
            first.append([news, nexr, nexc])

print(ans)