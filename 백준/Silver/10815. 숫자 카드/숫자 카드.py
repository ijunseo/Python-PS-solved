n = int(input())

s =set(list(map(int, input().split())))

m = int(input())

lst = list(map(int, input().split()))

for i in range(m):
    print(1 if lst[i] in s else 0)