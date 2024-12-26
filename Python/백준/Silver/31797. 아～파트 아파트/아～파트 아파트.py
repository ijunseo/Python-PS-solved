import sys
input = sys.stdin.readline
num , peo = map(int, input().split())
while num > peo * 2:
    num -= peo * 2
numlist =[]
for i in range(peo):
    a,b = map(int, input().split())
    numlist.append([a,i + 1])
    numlist.append([b,i + 1])
numlist.sort(key = lambda x : x[0])
ans = numlist[num - 1]
print(ans[1])