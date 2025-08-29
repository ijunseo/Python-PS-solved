n = int(input())
lst = list(map(int, input().split()))
num = int(input())
 
index = n // num
ans = []
 
for i in range(0,n,n // num):
    ans = lst[i:i + n // num]
    ans.sort()
    for j in ans:
        print(j, end=' ')