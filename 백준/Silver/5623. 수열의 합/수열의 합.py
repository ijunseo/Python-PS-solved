#基本操作
import sys
input =sys.stdin.readline

#input
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

#solve
#n == 2で唯一の答えを持つのは1，1のみ
if n == 2:
    print('1 1')
    sys.exit()

fir = (lst[0][1] + lst[0][2] - lst[1][2]) // 2
print(fir, end = ' ')
for i in range(1, n):
    #printans
    print(lst[0][i] - fir, end = ' ')