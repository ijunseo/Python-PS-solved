#基本操作
import sys
input = sys.stdin.readline

#input 
n = int(input())
lst = sorted(list(map(int, input().split())), reverse = True)
piv1 = 0
min_ans = 0
max_ans = 0

for i in range(n):
    if lst[i] < 0:
        if (piv1 + 1) * (max_ans + lst[i]) > piv1 * max_ans + lst[i]:
            piv1 += 1
            max_ans += lst[i]
        else:
            min_ans += lst[i]
    else:
        piv1 += 1
        max_ans += lst[i]

print(piv1 * max_ans + min_ans)