#基本操作
import sys
import bisect
input = sys.stdin.readline

#入力
n, m, k = map(int, input().split())
cardlist = sorted(list(map(int, input().split()))) #二分探索するのでソートする
cardtruelist = [False] * m #既に出してたカードかを確認する
enemycard = list(map(int, input().split()))

#solve
ans = []
for i in range(k):
    target = enemycard[i]
    piv = bisect.bisect_right(cardlist, target)
    if cardtruelist[piv]:
        while cardtruelist[piv] == True:
            piv += 1
    ans.append(cardlist[piv])
    cardtruelist[piv] = True
for i in ans:
    print(i)