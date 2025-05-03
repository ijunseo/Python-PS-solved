import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
ans_lst = []
ansset = set()
for i in range(n):
    now = lst[i]
    if now in ansset:
        for j in range(len(ans_lst)):
            if ans_lst[j][0] == now:
                ans_lst[j][1] += 1
                break
    else:
        ans_lst.append([now, 1])
        ansset.add(now)
ans_lst.sort(key = lambda x : -x[1])

for i in range(len(ans_lst)):
    nownum, num = ans_lst[i]
    for _ in range(num):
        print(nownum, end = ' ')