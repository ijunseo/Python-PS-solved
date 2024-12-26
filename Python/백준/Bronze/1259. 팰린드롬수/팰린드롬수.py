while True:
  num_1 = int(input())
  num = list(map(int, str(num_1)))
  # print(num[::1])
  # print(num[::-1])
  if num[0] == 0:
    break
  if num[::1] == num[::-1]:
    print("yes")
  else:
    print("no")
  