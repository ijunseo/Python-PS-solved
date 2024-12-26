num = int(input())
lst = [-1] * (num + 2)
i = 0
while 3 * i <= num:
  lst[3 * i + 1] = i
  i += 1
for i in range(num - 3):
  if lst[i] >= 0:
    if lst[i + 5] == -1:
      lst[i + 5] =  lst[i] + 1
    else:
      lst[i + 5] = min(lst[i + 5], lst[i] + 1)
print(lst[num + 1])