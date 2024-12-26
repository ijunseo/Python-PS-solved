def find(k):
  n = 1
  if k == 1:
    return 1
  else:
    while k > n * (n + 1)/2:
      n += 1
    return n
num = int(input())
d =int( find(num) * (find(num) + 1) / 2  -  num)
e = find(num)


if e%2 == 0:
  print("{}/{}".format(e - d,1 + d))
else:
  print("{}/{}".format(1 + d,e - d))