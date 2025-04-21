#基本操作
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

#input
n, m = map(int, input().split())
parlst = [i for i in range(n + 1)]

#solve
def find(inp_num):
	if parlst[inp_num] == inp_num:
		return inp_num
	else:
		parlst[inp_num] = find(parlst[inp_num])
		return find(parlst[inp_num])

def union(dot_one, dot_two):
	par_one = find(dot_one)
	par_two = find(dot_two)
	
	if par_one <= par_two:
		parlst[par_two] = par_one
	else:
		parlst[par_one] = par_two

for _ in range(m):
	cmd = list(map(int, input().split()))
	one = cmd[1]
	two = cmd[2]
	if not cmd[0]:
		union(one, two)
	else:
		if find(one) == find(two):
			print('yes')
		else:
			print('no')