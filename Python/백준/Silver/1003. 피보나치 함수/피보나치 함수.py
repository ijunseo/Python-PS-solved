fibolist = [0,1]
num = int(input())
for i in range(40):
  fibolist.append(fibolist[i] + fibolist[i + 1])

def fibo(d):
  if d == 0:
    print("1 0")
  else:
    print(fibolist[d - 1],fibolist[d])
for i in range(num):
  nums = int(input())
  fibo(nums)