num = int(input())

for i in range(1,num//5):
  if num //(5**i) == 0:
    how_num = i
    break
fac_num = 0
for i in range(1,4):
  fac_num += num//(5**i)
print(fac_num)