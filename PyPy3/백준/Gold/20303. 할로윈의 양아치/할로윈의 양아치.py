#基本操作
import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

#入力
num, linenum, limit = map(int, input().split())
candylist = [0] + list(map(int, input().split()))
line = [[]for _ in range(num + 1)]
for _ in range(linenum):
	a, b = map(int, input().split())
	line[a].append(b)
	line[b].append(a)
	
#友達確認用DFS
def dfs(now):
	global isfriend
	global candy
	global child
	if isfriend[now]:
		return
	isfriend[now] = True
	candy += candylist[now]
	child += 1
	for i in line[now]:
		if not isfriend[i]:
			dfs(i)

#友達グループを確認してリスト化して効率順にheapに入れる
isfriend = [False] * (num + 1)
friendlist = []
for i in range(1, num + 1):
	candy = 0
	child = 0
	dfs(i)
	if child != 0:
		friendlist.append((child, candy))

#knapsack
dp = [0] * limit
for i in range(1, len(friendlist) + 1):
	weight, value = friendlist.pop()
	for j in range(limit - 1, weight - 1, -1):
		dp[j] = max(dp[j], dp[j - weight] + value)
print(dp[-1])