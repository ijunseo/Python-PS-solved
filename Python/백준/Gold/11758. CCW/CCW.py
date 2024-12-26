import sys
input = sys.stdin.readline
dotlist = []
for _ in range(3):
    a, b = map(int, input().split())
    dotlist.append([a, b])
ans = (dotlist[1][0] - dotlist[0][0]) * (dotlist[2][1] - dotlist[0][1]) - (dotlist[1][1] - dotlist[0][1]) * (dotlist[2][0] - dotlist[0][0])
if ans < 0:
    print('-1')
elif ans == 0:
    print('0')
else:
    print('1')