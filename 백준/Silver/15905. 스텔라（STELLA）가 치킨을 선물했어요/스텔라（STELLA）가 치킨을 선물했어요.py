N = int(input())

lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x: [- x[0] , x[1]])

ans = 0
for i in range(N):
    if lst[4][0] == lst[i][0] and lst[4][1] < lst[i][1]:
    	ans += 1

print(ans)