n = int(input())
num = list(map(int, input().split()))
s = set(num)

print(len(num) - len(s))