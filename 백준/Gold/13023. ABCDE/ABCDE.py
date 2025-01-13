import sys
input = sys.stdin.readline

#入力
dot, linenum = map(int, input().split())
line = [[] for _ in range(dot)]
wentcheck = [False] * dot
for _ in range(linenum):
    a, b = map(int, input().split())
    line[a].append(b)
    line[b].append(a)

#DFS関数
def dfs(now, cnt):
    if cnt == 5:
        print('1')
        sys.exit()
    for i in line[now]:
        if wentcheck[i] == False:
            wentcheck[i] = True
            dfs(i, cnt + 1)
            wentcheck[i] = False

for i in range(dot):
    dfs(i, 0)
print('0')