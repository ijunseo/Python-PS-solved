import sys
num = int(sys.stdin.readline())
peoplelist = []
for i in range(num):
  a, b, c, d = map(str, sys.stdin.readline().split())
  b, c, d = int(b), int(c), int(d)
  peoplelist.append([a, b, c, d])
peoplelist.sort(key = lambda x: x[0])
peoplelist.sort(key = lambda x: x[3], reverse = True)
peoplelist.sort(key = lambda x: x[2])
peoplelist.sort(key = lambda x: x[1], reverse = True)
for i in peoplelist:
  print(i[0])