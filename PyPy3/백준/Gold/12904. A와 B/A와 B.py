import sys
input = sys.stdin.readline
s = input().strip()
t = input().strip()
lens = len(s)
def dfs(qu):
    if s == qu:
        print('1')
        sys.exit()
    if len(qu) < lens:
        return
    if qu[-1] == 'A':
        dfs(qu[:-1])
    if qu[-1] == 'B':
        #dfs(qu[1::-1])
        dfs(qu[:-1][::-1])
dfs(t)
print('0')
        