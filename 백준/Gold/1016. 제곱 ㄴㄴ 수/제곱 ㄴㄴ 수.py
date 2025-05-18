import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())

ansset = set([i for i in range(n, m + 1)])

mx = int(math.sqrt(m))

#sq_lst = [True for _ in range(mx + 1)]

if mx == 1:
    print(len(ansset))
    sys.exit()

for i in range(2, mx + 1):
    #if sq_lst[i]:
        sqnum = i ** 2
        st = ((n + sqnum - 1) // sqnum * sqnum)
        for j in range(st, m + 1, sqnum):
            ansset.discard(j)
        # for j in range(2, mx + 1):
        #     if j % i == 0:
        #         sq_lst[j] = False
print(len(ansset))