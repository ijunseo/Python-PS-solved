import sys
input = sys.stdin.readline
import bisect

'''
線が交差しないように、できるだけ多くの線をつなぐ本数を求める問題。
線が交差しないためには、左側のポート番号が小さい順に、
右側の接続先も小さい順になるように選ぶ必要がある。

つまり「右側の接続先の番号」が単調増加するように部分列を選ぶことがポイント。

これはLISを求める問題と同じ考え方で解ける。
'''

n = int(input())
lst = list(map(int, input().split()))

#anslst[-1]探索時に空のリストなら、エラーが生じるため。
anslst = [0]
for i in range(n):
    nownum = lst[i]

    if anslst[-1] < nownum:
        anslst.append(nownum)
    else:
        lft = bisect.bisect_left(anslst, nownum)
        anslst[lft] = nownum

#anslst = [0]から始めたため。
print(len(anslst) - 1)