n, k = map(int, input().split())
coin_list = []
how_many = 0
for i in range(n):
    coin_list.append(int(input()))
for i in range(n):
    many = k // coin_list[n - 1 - i]
    k -= coin_list[n - 1 - i] * many
    how_many += many
print(how_many)