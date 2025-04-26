import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())
lst = [[math.inf, 0] for _ in range(4 * n)] #[min, max]
first_piv = 2 ** math.ceil(math.log(n, 2))

for i in range(n):
	now_num = int(input())
	lst[first_piv + i][0] = now_num
	lst[first_piv + i][1] = now_num
	nowpiv = first_piv + i
	while nowpiv != 0:
		nowpiv = nowpiv // 2
		lst[nowpiv][0] = min(lst[nowpiv][0], now_num)
		lst[nowpiv][1] = max(lst[nowpiv][1], now_num)
		
def find_ans(inp_st, inp_ed, now_node, now_st, now_read):
	global mx, mi
	gap = now_read // 2
	if now_st + now_read - 1 < inp_st or now_st > inp_ed:
		return
	if inp_st <= now_st and now_st + now_read - 1 <= inp_ed:
		mi = min(lst[now_node][0], mi)
		mx = max(lst[now_node][1], mx)
		return
	
	if inp_st <= now_st + gap - 1:
		now_gap = gap
		find_ans(inp_st, inp_ed, now_node * 2, now_st, gap)
		
	if inp_ed >= now_st + gap - 1:
		find_ans(inp_st, inp_ed, now_node * 2 + 1, now_st + gap, gap)
	
for _ in range(m):
	st, ed = map(int, input().split())
	mx = 0
	mi = math.inf
	find_ans(st, ed, 1, 1, first_piv)
	print(mi)