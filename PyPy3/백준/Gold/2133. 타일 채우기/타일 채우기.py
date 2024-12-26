num = int(input())
numlist = [0,3,0]
for i in range(num - 3):
  if (i + 3) % 2 == 0:
    numlist.append(0)
  else:
    numlist.append(2 + numlist[i + 1] * 3 + sum(numlist[0:i + 1] * 2))
print(numlist[num - 1])