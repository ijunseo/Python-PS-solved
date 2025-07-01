import math

n = int(input())
end = 0
ans = 0
aans = 0

    
for start in range(0, n):
    while ans < n and end < n :
        ans += end+1
        end += 1
    if ans == n:
        aans += 1
    ans -= start+1
print(aans)