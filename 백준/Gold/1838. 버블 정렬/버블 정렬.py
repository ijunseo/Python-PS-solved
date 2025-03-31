#基本操作
import sys
input = sys.stdin.readline

#座標圧縮とhashtableを用いて解いてみた(メモリー心配あるけど)
#input 
n = int(input())
lst = list(map(int, input().split()))
llst = sorted(lst, reverse = True)

dic = {}
ans = 0

#solve 

for i in range(n):
    num = llst.pop()
    dic[num] = i

for i in range(n):
    now_num = lst[i]
    num_piv = dic[now_num]

    if i > num_piv:
        ans = max(ans, i - num_piv)
#output
print(ans)