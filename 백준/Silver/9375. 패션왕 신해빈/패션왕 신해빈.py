#基本操作
import sys
input = sys.stdin.readline

#input
testcase = int(input().strip())
for _ in range(testcase):
    n = int(input().strip())
    dic = {}
    ans = 1
    for _ in range(n):
        a, b = map(str, input().strip().split())
        if b in dic:
            dic[b].append(a)
        else:
            dic[b] = [a]
    for i in dic:
        ans *= (len(dic[i]) + 1)
    print(ans - 1)