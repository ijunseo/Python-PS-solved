import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0, n]
llst = [0, m]

query_num = int(input())
for _ in range(query_num):
    cmd = input().split()
    if cmd[0] == '1':
        lst.append(int(cmd[1]))
    else:
        llst.append(int(cmd[1]))

lst.sort()
llst.sort()
x = 0
y = 0
for i in range(len(lst) - 1):
    x = max(x, lst[i + 1] - lst[i])
for i in range(len(llst) - 1):
    y = max(y, llst[i + 1] - llst[i])
print(x * y)
