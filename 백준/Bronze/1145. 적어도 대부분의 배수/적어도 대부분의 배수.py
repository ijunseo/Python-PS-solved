import sys 
input = sys.stdin.readline
import math
 
n = list(map(int, input().split()))
ans = math.inf
 
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
        	ans = min(ans,math.lcm(n[i], n[j], n[k]))
 
print(ans)