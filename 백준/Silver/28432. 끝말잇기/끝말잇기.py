import sys
input = sys.stdin.readline

n = int(input())
lst = [str(input().rstrip()) for _ in range(n)]

m = int(input())
llst = [str(input().rstrip()) for _ in range(m)]

if n == 1:
    print(llst[0])
    sys.exit()

for i in range(n):
    if lst[i] == '?':
        if i == 0:
            next = lst[1][0]
            for j in range(m):
                if llst[j][-1] == next and llst[j] not in lst:
                    print(llst[j])
                    break
        elif i == n - 1:
            before = lst[n - 2][-1]
            for j in range(m):
                if llst[j][0] == before and llst[j] not in lst:
                    print(llst[j])
                    break
        else:
            next = lst[i + 1][0]
            before = lst[i - 1][-1]
            for j in range(m):
                if llst[j][-1] == next and llst[j][0] == before and llst[j] not in lst:
                    print(llst[j])
                    break