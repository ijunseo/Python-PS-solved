n = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
ans = 0

for i in range(7):
    
    if n >= stick[i]:
        ans += 1
        n -= stick[i]

    if n == 0:
        break

print(ans)