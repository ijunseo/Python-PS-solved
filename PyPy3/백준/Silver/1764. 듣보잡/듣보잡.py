import sys
nothear, notseen = map(int, input().split())
nothear_set = set()
notseen_set = set()
nothearseen_list = []
for i in range(nothear):
  nothear_set.add(sys.stdin.readline())
for i in range(notseen):
  notseen_set.add(sys.stdin.readline())
if nothear < notseen:
  for i in nothear_set:
    if i in notseen_set:
      nothearseen_list.append(i)
else:
  for i in notseen_set:
    if i in nothear_set:
      nothearseen_list.append(i)
nothearseen_list.sort()
print(len(nothearseen_list))
for i in nothearseen_list:
  print(i, end ="")