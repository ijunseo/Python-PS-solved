num = int(input())
for i in range(num):
  b = int(input())
  listb = [1,1,1]
  for i in range(b):
    listb.append(listb[i] + listb[i + 1])
  print(listb[b - 1])