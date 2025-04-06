#基本操作
import sys
input = sys.stdin.readline
from collections import defaultdict
import bisect

#input 
n, m = map(int, input().split())

x_dic = defaultdict(list)
y_dic = defaultdict(list)
for _ in range(n):
    now_x, now_y = map(int, input().split())
    bisect.insort(x_dic[now_x], now_y)
    bisect.insort(y_dic[now_y], now_x)

cmd = input()

now_locate = [0, 0]
for i in range(m):
    nowcmd = cmd[i]
    if nowcmd == 'D':
        piv = bisect.bisect_left(x_dic[now_locate[0]], now_locate[1])
        piv -= 1
        now_locate[1] = x_dic[now_locate[0]][piv]

    elif nowcmd == 'U':
        piv = bisect.bisect_right(x_dic[now_locate[0]], now_locate[1])
        now_locate[1] = x_dic[now_locate[0]][piv]

    elif nowcmd == 'L':
        piv = bisect.bisect_left(y_dic[now_locate[1]], now_locate[0])
        piv -= 1
        now_locate[0] = y_dic[now_locate[1]][piv]

    elif nowcmd == 'R':
        piv = bisect.bisect_right(y_dic[now_locate[1]], now_locate[0])
        now_locate[0] = y_dic[now_locate[1]][piv]

print(*now_locate)