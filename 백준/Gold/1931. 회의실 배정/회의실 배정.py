import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    j, k = map(int,input().split())
    lst.append([j, k])

#終わる時間が早い順でソートして、始めるのが早い順で再度sort
lst.sort(key = lambda x : (x[1], x[0]), reverse = True)

now = 0
ans = 0
while lst:
    nowtime, endtime = lst.pop()
    if nowtime >= now:
        ans += 1
        now = endtime

print(ans)