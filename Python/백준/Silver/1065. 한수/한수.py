num = int(input())

ans = 0
for i in range(1, num+1):
    numlist = list(map(int, str(i)))
    if i < 100:
        ans += 1  
    elif numlist[0] - numlist[1] == numlist[1] - numlist[2]:
        ans += 1  
print(ans)