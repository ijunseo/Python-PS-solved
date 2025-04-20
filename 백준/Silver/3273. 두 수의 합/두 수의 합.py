#基本操作
import sys
input = sys.stdin.readline

#input 
n = int(input())
lst = sorted(list(map(int, input().split())))
target = int(input())
lft = 0
rgt = n - 1
ans = 0

while lft < rgt:
    now_ans = lst[lft] + lst[rgt]
    if now_ans < target:
        lft += 1

    elif now_ans == target:
        ans += 1
        lft += 1
        rgt -= 1
    else:
        rgt -=1
print(ans)