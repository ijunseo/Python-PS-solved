#基本操作
import sys
input = sys.stdin.readline

#solve
def dfs(st, now):
	global went
	global ans
	went.append(now)
	if numlst[now] in went:
		if numlst[now] == st:
			for i in went:
				ans.append(i)
				wentlst[i] = True
		return
	dfs(st, numlst[now])
	
#入力,solve
num = int(input())
numlst = [0]
ans  = []
wentlst = [False] * (num + 1)
for _ in range(num):
	numlst.append(int(input()))
	
for i in range(1, num + 1):
	if wentlst[i]:
		continue
	went = []
	dfs(i, i)
	
ans.sort()
print(len(ans))
for i in ans:
	print(i)