a, b = map(int, input().split())
a = a - 1
b = b + 1
c = a % b
if c == 0:
    print("Can't win")
else:
    print("Can win")