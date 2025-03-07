#基本操作
import sys
input = sys.stdin.readline


#input
n = int(input())
lst = [input().rstrip() for _ in range(n)]
checklst = [[0] * n for _ in range(n)] #確認済みだったら1に変える
rgchecklst = [[0] * n for _ in range(n)] #R,Gの識別できない人
piv1 = 0
piv2 = 0

#bfs, solve
def bfs(x, y):
    global checklst
    global piv1
    if checklst[x][y]:
        return
    q = [[x, y]]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        nx , ny = q.pop() #今のx, y xが行 yが列であることに注意
        for i in range(4):
            newx , newy = nx + dx[i] , ny + dy[i]
            if 0 <= newx < n and 0 <= newy < n: #グラフ範囲内にあるかを確認
                nowcolor = lst[nx][ny]
                if not checklst[newx][newy] and lst[newx][newy] == nowcolor:
                    checklst[newx][newy] = 1
                    q.append([newx, newy])
    piv1 += 1

def rgbfs(x, y): #rgを識別できない人
    global rgchecklst
    global piv2
    if rgchecklst[x][y]:
        return
    q = [[x, y]]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        nx , ny = q.pop() #今のx, y xが行 yが列であることに注意
        for i in range(4):
            newx , newy = nx + dx[i] , ny + dy[i]
            if 0 <= newx < n and 0 <= newy < n: #グラフ範囲内にあるかを確認
                nowcolor = lst[nx][ny]
                if not rgchecklst[newx][newy]:
                    if nowcolor == 'R' or nowcolor == 'G':
                        if lst[newx][newy] == 'R' or lst[newx][newy] == 'G':
                            rgchecklst[newx][newy] = 1
                            q.append([newx, newy])
                    else:
                        if lst[newx][newy] == nowcolor:
                            rgchecklst[newx][newy] = 1
                            q.append([newx, newy])
    piv2 += 1

for i in range(n):
    for j in range(n):
        bfs(i, j)
        rgbfs(i, j)

print(piv1, piv2)