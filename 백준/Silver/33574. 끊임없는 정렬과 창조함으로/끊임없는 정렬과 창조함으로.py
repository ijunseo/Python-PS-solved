import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    cmd = list(map(int ,input().split()))
    if cmd[0] == 1:
        if cmd[1] == 1:
            lst.sort()
        else:
            lst.sort(reverse= True)
    else:
        lst.insert(cmd[1], cmd[2])
print(len(lst))
print(*lst)