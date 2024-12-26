import sys

input = sys.stdin.readline
node = int(input())
sonlist = [[] for i in range(node)]
parlist = list(map(int, input().split()))


for i in range(node):
  if parlist[i] == -1:
    root = i
  else:
    sonlist[parlist[i]].append(i)

ans = 0
for i in range(node):
  if len(sonlist[i]) == 0:
    ans += 1
  else:
    continue

delnode = int(input())

if delnode == root:
  print(0)
  sys.exit()

def leafnum(a):
  sonleaf = 0
  if len(sonlist[a]) == 0:
    return 1
  else:
    for i in sonlist[a]:
      sonleaf += leafnum(i)
  return sonleaf

sonleaf = leafnum(delnode)

if len(sonlist[parlist[delnode]]) == 1:
  ans -= sonleaf
  ans += 1
else:
  ans -= sonleaf

print(ans)