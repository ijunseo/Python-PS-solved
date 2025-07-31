import sys
input = sys.stdin.readline

n = int(input())
ans = [1,2,3]

for _ in range(n):
    x, y = map(int, input().split())
    a = ans.index(x)
    b = ans.index(y)  
    ans[a], ans[b] = ans[b], ans[a]
    
print(ans[0])