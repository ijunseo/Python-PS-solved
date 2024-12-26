a, b, c = map(int,input().split())
for _ in range(c):
  a = (a%b)*10
  d = a//b
print(d)