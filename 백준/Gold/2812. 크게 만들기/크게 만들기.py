#基本操作
import sys
input = sys.stdin.readline
from collections import deque

#input 
n, m = map(int, input().split())

string = deque(input().rstrip())

#solve - greed
ans_list = deque([])

now_m = 0


for _ in range(n):
    now_num = int(string.popleft())
    while True:

        #queueが空いてるんだったら
        if len(ans_list) == 0:
            ans_list.append(now_num)
            break

        #今の数字が前の数字より大きいと
        if now_num > ans_list[-1]:
            ans_list.pop()
            now_m += 1

            if now_m == m:

                #ans_listにある全ての要素、今の数字、まだ未探索の数字をプリントする
                for i in ans_list:
                    print(i, end = '')
                print(now_num, end = '')
                for j in string:
                    print(j, end = '')

                sys.exit()

        #今の数字が前の数字以下だったら
        else:
            ans_list.append(now_num)
            break 

#もう降順なら最後から数字を消す
for i in range(m - now_m):
    ans_list.pop()
for i in ans_list:
    print(i, end = '')