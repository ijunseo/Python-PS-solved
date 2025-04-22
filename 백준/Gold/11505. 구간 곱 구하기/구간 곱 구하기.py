#基本操作
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

#input_and_segtree
n, m , k = map(int, input().split())

piv = 0
while True:
    if n == 1:
        piv = 1
        break
    if 1 << piv < n <= 1 << (piv + 1):
        piv += 1
        break
    else:
        piv += 1

lst = [1] * (1 << piv + 1)

st = 1 << piv
for i in range(n):
    lst[st + i] = int(input())

for i in range((1 << (piv + 1)) - 1, 1, -1):
    lst[i // 2] *= lst[i]
    lst[i // 2] %= 1000000007

#solve 
def find_ans(l, r, now_index, nowl, pls_num):
    global ans
    if r < nowl or l > nowl + pls_num - 1:
        return
    
    if l <= nowl and nowl + pls_num - 1 <= r:
        ans *= lst[now_index]
        ans %= 1000000007
        return
    else:
        nn = pls_num // 2
        find_ans(l, r, now_index * 2, nowl, nn)
        find_ans(l, r, now_index * 2 + 1, nowl + nn, nn)


#output
for _ in range(m + k):
    cmd = list(map(int, input().split()))
    #print(cmd)
    if cmd[0] == 1:
        now_piv = (1 << piv) + cmd[1] - 1
        lst[now_piv] = cmd[2]
        while now_piv != 0:
            now_piv = now_piv // 2
            lst[now_piv] = (lst[now_piv * 2] * lst[now_piv * 2 + 1]) % 1000000007
            # print(now_piv, '!')
            # print(lst[now_piv], '!!!')

    else:
        ans = 1
        ans_left = cmd[1]
        ans_right = cmd[2]
        find_ans(ans_left, ans_right, 1, 1, 2 ** piv)
        print(int(ans))
    #print(lst)
    llst_piv = 1
    # for i in range(4):
    #     print(lst[llst_piv:llst_piv + 2 ** i])
    #     llst_piv += 2 ** i