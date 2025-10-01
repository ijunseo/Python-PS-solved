import sys
input = sys.stdin.readline

lst = list(input().rstrip())
llst = []
flag = False

for i in range(len(lst)):
    now = lst[i]

    if now == '<':
        for j in range(len(llst)):
            print(llst[-1 - j], end='')
        llst = []
        flag = True
        print(now, end='')
        continue

    if now == '>':
        flag = False
        print(now, end='')
        continue

    if flag:
        print(now, end='')
        continue

    if now == ' ':
        for j in range(len(llst)):
            print(llst[-1 - j], end='')
        llst = []
        print(' ', end='')
    else:
        llst.append(now)

if llst:
    for j in range(len(llst)):
        print(llst[-1 - j], end='')
