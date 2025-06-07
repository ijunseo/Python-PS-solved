n = int(input())

dot = 2
for _ in range(n):
    dot += dot - 1
print(dot ** 2)