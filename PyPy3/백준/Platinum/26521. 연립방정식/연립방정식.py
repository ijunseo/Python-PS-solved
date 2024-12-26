import sys
input = sys.stdin.readline
num = int(input())
numlist = list(map(int, input().split()))
anslist = []
for i in range(num):
    ans = 1
    for j in range(num):
        if i == j:
            continue
        ans *= numlist[i] - numlist[j]
        ans = ans % 1000000007
    if num + i + 1 // 2 == 1:
        anslist.append(-ans)
    else:
        anslist.append(ans)
print(*anslist)