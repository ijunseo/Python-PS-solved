import sys
input = sys.stdin.readline
testcase = int(input())
from collections import deque

for _ in range(testcase):
    
    case, dot, linenum  = map(int, input().split())
    line = [[] for _ in range(dot + 1)]
    dotlinenum = [0] * (dot + 1) 
    stra = [[] for _ in range(dot + 1)]

    for _ in range(linenum):
        a, b = map(int, input().split())
        line[a].append(b) 
        dotlinenum[b] += 1

    que = deque()
    for i in range(1, dot + 1):
        if dotlinenum[i] == 0:
            que.append(i) 
            stra[i] = [1, 0]

    while que:
        now = que.popleft()
        cst = stra[now][0] + stra[now][1]
        for i in line[now]:
            dotlinenum[i] -= 1
            if not stra[i] or stra[i][0] < cst:
                stra[i] = [cst, 0]
            elif stra[i][0] == cst:
                stra[i][1] = 1
            if dotlinenum[i] == 0:
                que.append(i)
    print(case, sum(stra[dot]))