#基本操作
import sys
from heapq import *
input = sys.stdin.readline


#入力処理
dianum, bagnum = map(int, input().split())#宝石の数、カバンの数
dialist = []#宝石を入れるlist
baglist = []#カバンを入れるlist

for _ in range(dianum):
    heavy, cst = map(int, input().split())
    dialist.append((heavy, cst))
dialist.sort(key = lambda x : x[0])#重さ基準でソート

for _ in range(bagnum):
    capacity = int(input())
    baglist.append(capacity)
baglist.sort()

ans = 0
diapivot = 0

#Greedy
heap = []#今カバンに入れる宝石の価値
for i in range(bagnum):
    while diapivot < dianum and baglist[i] >= dialist[diapivot][0]:#カバンに入れるんだったら
        heappush(heap, -dialist[diapivot][1])#push
        diapivot += 1#次の宝石も確認する
    if len(heap) != 0:
        ans += -heappop(heap)#いまカバンに入れる宝石の中で一番価値高い物を入れる

print(ans)