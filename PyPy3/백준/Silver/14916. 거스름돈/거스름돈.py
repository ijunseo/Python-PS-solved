import math
num = int(input())
num_list = [0] + [math.inf] * (num)

i = 1
while (5 * i) < len(num_list):
  num_list[5 * i] = i
  i += 1
for k in range (num - 1):
  num_list[k + 2] = min(num_list[k + 2], num_list[k] + 1)
if num_list[num] != math.inf:
  print(num_list[num])
else:
  print(-1)