#基本操作
import sys
input = sys.stdin.readline
import bisect

#input 
n = int(input())
lst = list(map(int, input().split()))
anslst = []

for i in range(n):
    now_num = lst[i]
    if not anslst:
        anslst.append(now_num)
    else:
        if anslst[-1] > now_num:
            lft = bisect.bisect_left(anslst, now_num)
            anslst[lft] = now_num
        elif anslst[-1] < now_num:
            anslst.append(now_num)
print(len(anslst))